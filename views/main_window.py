import os
import datetime
from PIL import Image
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem, Qt
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog

from controllers.crud import get_groups_from_db, get_students_with_journal, update_or_create_journal_entry
from libs.database import SessionLocal
from models.User import User
from ui.ui_main import Ui_MainWindow as UI_Main


class MainApp(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_Main()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.ui.profileButton.setIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))
        self.setWindowIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))
        self.ui.frame.setVisible(False)
        self.ui.pushButton.clicked.connect(self.upload_image)
        self.ui.profileButton.clicked.connect(self.open_frame)
        self.ui.closeButton.clicked.connect(self.close_frame)

        self.photo = QLabel(self.ui.photo)
        self.update_photo()
        self.date_today = str(datetime.date.today())
        self.load_groups()
        self.on_group_selected()
        self.ui.comboBox.currentIndexChanged.connect(self.on_group_selected)

    def load_journal_table(self, group_id):
        """Заполняет таблицу студентами и их статусами за 7 пар."""
        students = get_students_with_journal(group_id, self.date_today)

        model = QStandardItemModel()
        model.setColumnCount(10)  # Фамилия, Имя, Отчество + 7 пар
        model.setHorizontalHeaderLabels(["Фамилия", "Имя", "Отчество"] + [f"{i + 1} пара" for i in range(7)])
        print(students.items())
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
                row.append(item)  # Добавляем в таблицу

            model.appendRow(row)

        self.ui.tableView.setModel(model)
        self.ui.tableView.model().dataChanged.connect(self.save_journal_entry)

    def save_journal_entry(self, index):
        """Сохраняет изменённую запись в базу."""
        """Сохраняет изменённую запись в базу."""
        row = index.row()
        col = index.column()

        if col < 3:
            return  # ФИО нельзя редактировать

        # Получаем данные
        model = self.ui.tableView.model()
        last_name = model.item(row, 0).text()
        first_name = model.item(row, 1).text()
        middle_name = model.item(row, 2).text()
        lesson_number = col - 2
        status = model.item(row, col).text()

        db = SessionLocal()
        success = update_or_create_journal_entry(db, last_name, first_name, middle_name,
                                                 lesson_number, status, self.date_today)
        db.close()

        if success:
            QMessageBox.information(self, "Сохранено", f"Статус на {lesson_number}-й паре обновлён.")
        else:
            QMessageBox.warning(self, "Ошибка", "Студент не найден!")

    def load_groups(self):
        groups = get_groups_from_db()
        self.ui.comboBox.clear()
        for group in groups:
            self.ui.comboBox.addItem(group.name, group.id)

    def update_photo(self):
        try:
            file_path = f"libs/user_images/{self.user_id}.jpg"
            img = Image.open(file_path)
            self.photo.setGeometry(0, 0, img.width, img.height)
            target_size = (200, 200)
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
                                                   "Выберите фото", "", "Images (*.png *.jpg *.jpeg)")
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

            self.save_image_path_to_db(save_path)

            QMessageBox.information(self, "Успешно", "Фото загружено!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить фото: {str(e)}")
        self.update_photo()


    def save_image_path_to_db(self, image_path):
        db = SessionLocal()
        user = db.query(User).filter(User.id == self.user_id).first()
        if user:
            user.photo = image_path
            db.commit()
        db.close()

    def on_group_selected(self):
        group_id = self.ui.comboBox.currentData()
        self.load_journal_table(group_id)

