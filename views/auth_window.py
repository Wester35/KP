from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QLineEdit
from controllers.crud import authenticate_user, save_user_session
from ui.ui_login import Ui_Authorization as LoginUI
from views.main_window import MainApp


class Auth(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = LoginUI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handle_login)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/app_icon.png"))
        self.setWindowIcon(QPixmap("ui/resources/app_icon.png"))
        self.background = QLabel(self.ui.frame_2)
        self.background.setGeometry(0, 0, 600, 600)

        pixmap = QPixmap("ui/resources/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

        self.ui.checkPassword.setText("👁️‍🗨️")
        self.ui.checkPassword.setCheckable(True)
        self.ui.checkPassword.clicked.connect(self.check_pwd)

    def handle_login(self):
        login = self.ui.usernameEdit.text()
        password = self.ui.passwordEdit.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        user = authenticate_user(login, password)

        if user:
            if self.ui.checkBox.isChecked():
                save_user_session(user.id)
            self.show_main_window(user.id, user.is_teacher, user.is_admin)
        else:
            QMessageBox.warning(self, "Ошибка", "Аккаунт не существует!")

    def show_main_window(self, user_id, is_teacher, is_admin):
        self.close()
        self.ui = MainApp(user_id, is_teacher, is_admin)
        self.ui.show()

    def check_pwd(self):
        if self.ui.checkPassword.isChecked():
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)