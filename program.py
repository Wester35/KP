from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox, QLineEdit
from ui.ui_login import Ui_Authorization as LoginUI
from ui.ui_main import Ui_MainWindow as Ui_Main
import sys
from libs.database import SessionLocal
from libs.crud import authenticate_user, save_user_session, check_if_logged_in, load_user_session


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.close()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
      


class Auth(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = LoginUI()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handle_login)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))
        self.setWindowIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))
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

        db = SessionLocal()
        user = authenticate_user(db, login, password)
        if user:
            if self.ui.checkBox.isChecked():
                save_user_session(user.id)
            self.show_main_window()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверно")

    def show_main_window(self):
        self.close()
        self.ui = MainApp()
        self.ui.show()

    def check_pwd(self):
        if self.ui.checkPassword.isChecked():
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    session_data = load_user_session()
    if session_data and session_data.get("user_id"):
        main_app = MainApp()
        main_app.show()
    else:
        main_app = Auth()
        main_app.show()

    sys.exit(app.exec())
