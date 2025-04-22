from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
from controllers.crud import create_user_with_group
from ui.ui_register import Ui_Registration as RegisterUI


class Register(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlag(Qt.Window)

        self.ui = RegisterUI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handle_register)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/app_icon.png"))
        self.setWindowIcon(QPixmap("ui/resources/app_icon.png"))
        self.background = QLabel(self.ui.frame_2)
        self.background.setGeometry(0, 0, 650, 720)

        pixmap = QPixmap("ui/resources/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

        self.ui.checkPassword.setText("👁️‍🗨️")
        self.ui.checkPassword.setCheckable(True)
        self.ui.checkPassword.clicked.connect(self.check_pwd)

    def parse_fullname(self, full_name):
        parts = full_name.strip().split()
        return (
            parts[0] if len(parts) > 0 else "",
            parts[1] if len(parts) > 1 else "",
            parts[2] if len(parts) > 2 else "",
        )

    def handle_register(self):
        login = self.ui.usernameEdit.text()
        last, first, middle = self.parse_fullname(self.ui.fioEdit.text())
        phone = self.ui.phoneEdit.text()
        password = self.ui.passwordEdit.text()
        group = self.ui.groupEdit.text().strip() or None
        is_teacher = self.ui.checkBox.isChecked()

        if not login or not last or not first or not phone or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        try:
            create_user_with_group(
                last_name=last,
                first_name=first,
                middle_name=middle,
                phone=phone,
                login=login,
                password=password,
                group_name=group,
                is_teacher=is_teacher,
                is_admin=False
            )
            QMessageBox.warning(self, "Уведомление", "Пользователь успешно зарегестрирован")
        except Exception:
            QMessageBox.warning(self, "Ошибка", "Ошибка БД")

    def check_pwd(self):
        if self.ui.checkPassword.isChecked():
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
