import os
import datetime
from PIL import Image
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem, Qt
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog, QSizePolicy, QVBoxLayout, QHBoxLayout
from controllers.crud import (get_groups_from_db, get_students_with_journal,
                              update_or_create_journal_entry, delete_user_session, get_user_data_by_id,
                              save_image_path_to_db, update_or_create_log_entry, get_statuses_from_logs,
                              count_statuses_by_student)
from ui.ui_main import Ui_MainWindow as UI_Main
from libs.delegates import ComboBoxDelegate


class MainApp(QWidget):
    def __init__(self, user_id, is_teacher, is_admin):
        super().__init__()
        self.ui = UI_Main()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.is_teacher = is_teacher
        self.is_admin = is_admin

        if (not self.is_admin) and (not self.is_teacher):
            self.ui.tableView.setVisible(False)
            self.ui.comboBox.setVisible(False)
            self.ui.calendarWidget.setVisible(False)
            self.ui.pair_teacher.setVisible(False)
            self.resize(800, 780)

            main_layout = QVBoxLayout(self)

            top_layout = QHBoxLayout()
            top_layout.addWidget(self.ui.profileButton)
            top_layout.addStretch()
            top_layout.addWidget(self.ui.currentDate)
            main_layout.addLayout(top_layout)

            form_layout = QHBoxLayout()
            form_layout.addWidget(self.ui.formLayoutWidget)
            form_layout.addStretch()
            main_layout.addLayout(form_layout)

            self.ui.studentLatesView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            main_layout.addWidget(self.ui.studentLatesView)

            self.setLayout(main_layout)

        else:
            if (not self.is_admin) and self.is_teacher:
                self.ui.calendarWidget.setVisible(False)
                self.ui.formLayoutWidget.setVisible(False)
                self.resize(1050, 780)
            elif self.is_admin:
                self.ui.formLayoutWidget.setVisible(False)

            self.ui.studentLatesView.setVisible(False)

            main_layout = QVBoxLayout(self)

            top_layout = QHBoxLayout()
            top_layout.addWidget(self.ui.profileButton, alignment=Qt.AlignLeft)
            top_layout.addStretch(0, 0)

            top_layout.addWidget(self.ui.currentDate)
            top_layout.addWidget(self.ui.comboBox)

            table_layout = QVBoxLayout()
            self.ui.tableView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.ui.pair_teacher.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            self.ui.pair_teacher.setFixedHeight(65)
            table_layout.addWidget(self.ui.pair_teacher)
            table_layout.addWidget(self.ui.tableView)

            center_layout = QHBoxLayout()
            center_layout.addLayout(table_layout)

            self.ui.calendarWidget.setFixedSize(341, 451)
            center_layout.addWidget(self.ui.calendarWidget)

            main_layout.addLayout(top_layout)
            main_layout.addLayout(center_layout)

            self.setLayout(main_layout)
            center_layout.setStretch(0, 3)
            center_layout.setStretch(1, 1)

        #Buttons
        self.ui.profileButton.setIcon(QPixmap("ui/resources/app_icon.png"))
        self.ui.profileButton.setFixedSize(72, 72)
        self.setWindowIcon(QPixmap("ui/resources/app_icon.png"))
        self.ui.frame.setVisible(False)

        self.ui.closeButton.setText("✖")

        self.ui.pushButton.clicked.connect(self.upload_image)
        self.ui.profileButton.clicked.connect(self.open_frame)
        self.ui.closeButton.clicked.connect(self.close_frame)
        self.ui.logoutButton.clicked.connect(self.logout_user)
        self.ui.comboBox.currentIndexChanged.connect(self.on_group_selected)
        self.ui.calendarWidget.selectionChanged.connect(self.on_group_selected)

        #Any
        self.photo = QLabel(self.ui.photo)
        self.date_today = str(datetime.date.today())
        self.load_groups()
        self.on_group_selected()
        self.load_userdata()
        self.ui.currentDate.setText(f"    Current date: {self.date_today}")
        self.ui.currentDate.setFixedSize(296, 16)

        # Frame
        self.ui.frame.setParent(self)
        self.ui.frame.setVisible(False)
        self.center_frame()
        self.resizeEvent = self.on_resize

    def center_frame(self):
        frame_size = self.ui.frame.size()
        window_size = self.size()

        x = (window_size.width() - frame_size.width()) // 2
        y = (window_size.height() - frame_size.height()) // 2

        self.ui.frame.move(x, y)

    def on_resize(self, event):
        super().resizeEvent(event)
        self.center_frame()

    def load_userdata(self):
        user = get_user_data_by_id(self.user_id)
        stats = count_statuses_by_student(self.user_id)
        self.ui.loginValue.setText(user.login)
        self.ui.surnameValue.setText(user.last_name)
        self.ui.nameValue.setText(user.first_name)
        self.ui.lastnameValue.setText(user.middle_name)
        self.ui.phoneValue.setText(user.phone)
        self.ui.groupValue.setText(user.group_name)
        self.update_photo(user.photo)
        self.ui.latesValue.setText(str(stats['о']))
        self.ui.absenceValue.setText(str(stats['н']))

    def get_date(self):
        return self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

    def logout_user(self):
        delete_user_session()
        self.close()

    def load_teacher_table(self, group_id):
        statuses = get_statuses_from_logs(group_id, self.get_date())

        model = QStandardItemModel()
        model.setColumnCount(10)
        model.setHorizontalHeaderLabels(["", "", ""] + [f"{i + 1} пара" for i in range(7)])
        row = [
            QStandardItem(""),
            QStandardItem(""),
            QStandardItem("")
        ]

        row[0].setEditable(False)
        row[1].setEditable(False)
        row[2].setEditable(False)

        for status in statuses:
            item = QStandardItem(status)
            row.append(item)

        model.appendRow(row)

        self.ui.pair_teacher.setModel(model)
        self.ui.pair_teacher.model().dataChanged.connect(self.save_log_entry)

    def load_journal_table(self, group_id):
        students = get_students_with_journal(group_id, self.get_date())

        model = QStandardItemModel()
        model.setColumnCount(10)
        model.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество"] + [f"{i + 1} пара" for i in range(7)])

        delegate = ComboBoxDelegate(self.ui.tableView)
        for col in range(3, 10):
            self.ui.tableView.setItemDelegateForColumn(col, delegate)

        for (last_name, first_name, middle_name), statuses in students.items():
            row = [
                QStandardItem(last_name),
                QStandardItem(first_name),
                QStandardItem(middle_name if middle_name else "")
            ]

            row[0].setEditable(False)
            row[1].setEditable(False)
            row[2].setEditable(False)

            for status in statuses:
                item = QStandardItem(status)
                row.append(item)

            model.appendRow(row)

        self.ui.tableView.setModel(model)
        self.ui.tableView.model().dataChanged.connect(self.save_journal_entry)

    def save_log_entry(self, index):
        col = index.column()
        row = index.row()

        if col < 3:
            return

        model = self.ui.pair_teacher.model()
        lesson_data = model.item(row, col).text()
        lesson_number = col - 2
        group_id = self.ui.comboBox.currentData()

        success = update_or_create_log_entry(self.user_id, group_id, lesson_number,
                                            self.get_date(), lesson_data)

        if success:
            QMessageBox.information(self, "Сохранено", f"Статус на {lesson_number}-й паре обновлён.")
        else:
            QMessageBox.warning(self, "Ошибка", "Студент не найден!")

    def save_journal_entry(self, index):
        row = index.row()
        col = index.column()

        if col < 3:
            return

        model = self.ui.tableView.model()
        last_name = model.item(row, 0).text()
        first_name = model.item(row, 1).text()
        middle_name = model.item(row, 2).text()
        lesson_number = col - 2
        status = model.item(row, col).text()

        success = update_or_create_journal_entry(last_name, first_name, middle_name,
                                                 lesson_number, status, self.get_date(), self.user_id)

        if success:
            QMessageBox.information(self, "Сохранено", f"Статус на {lesson_number}-й паре обновлён.")
        else:
            QMessageBox.warning(self, "Ошибка", "Студент не найден!")

    def load_groups(self):
        groups = get_groups_from_db()
        self.ui.comboBox.clear()
        for group in groups:
            self.ui.comboBox.addItem(group.name, group.id)

    def update_photo(self, file_path):
        try:
            img = Image.open(file_path)
            self.photo.setGeometry(0, 0, img.width, img.height)
            target_size = (261, 261)
            pixmap = QPixmap(file_path).scaled(*target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.photo.setPixmap(pixmap)
            self.photo.setFixedSize(*target_size)
            self.photo.setScaledContents(False)
            self.photo.setAlignment(Qt.AlignCenter)
        except Exception:
            pass

    def open_frame(self):
        self.ui.frame.setVisible(True)

    def close_frame(self):
        self.ui.frame.setVisible(False)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   "Выберите фото",
                                                   "",
                                                   "Images (*.png *.jpg *.jpeg)")
        if not file_path:
            return

        save_dir = "libs/user_images"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_path = os.path.join(save_dir, f"{self.user_id}.jpg")

        try:
            img = Image.open(file_path)
            img = img.convert("RGB")
            img.thumbnail((300, 300))
            img.save(save_path, "JPEG", quality=85)

            save_image_path_to_db(self.user_id, save_path)

            QMessageBox.information(self, "Успешно", "Фото загружено!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить фото: {str(e)}")
        finally:
            self.update_photo(save_path)

    def on_group_selected(self):
        group_id = self.ui.comboBox.currentData()
        self.load_journal_table(group_id)
        self.load_teacher_table(group_id)
