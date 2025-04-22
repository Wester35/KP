from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
from controllers.crud import authenticate_user, save_user_session
from libs.database import SessionLocal
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
        self.background.setGeometry(0, 0, 650, 700)

        pixmap = QPixmap("ui/resources/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

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

        if not login or not last or not first or not phone or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        user = authenticate_user(db, login, password)
