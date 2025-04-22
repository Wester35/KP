from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QLineEdit
from controllers.crud import authenticate_user, save_user_session
from libs.database import SessionLocal
from ui.ui_register import Ui_Registration as RegisterUI


class Register(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = RegisterUI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handle_login)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/app_icon.png"))
        self.setWindowIcon(QPixmap("ui/resources/app_icon.png"))
        self.background = QLabel(self.ui.frame_2)
        self.background.setGeometry(0, 0, 600, 600)

        pixmap = QPixmap("ui/resources/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)


    def handle_login(self):
        login = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        db = SessionLocal()
        user = authenticate_user(db, login, password)

        if user:
            if self.ui.checkBox.isChecked():
                save_user_session(user.id)
        else:
            QMessageBox.warning(self, "Ошибка", "Неверно")
