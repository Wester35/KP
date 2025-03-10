import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QMessageBox

from libs.models import RoleEnum
from ui.ui_login import Ui_MainWindow
from PySide6.QtGui import QPixmap
from libs.crud import create_user, get_user_by_username, verify_password
from libs.database import SessionLocal


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.handle_login)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))

        self.background = QLabel(self.ui.frame_2)
        self.background.setGeometry(0, 0, 600, 600)

        pixmap = QPixmap("ui/resources/background.jpg")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

        self.ui.checkPassword.setText("👁️‍🗨️")
        self.ui.checkPassword.setCheckable(True)
        self.ui.checkPassword.clicked.connect(self.check_pwd)

    def handle_login(self):
        username = self.ui.usernameEdit.text()
        password = self.ui.usernameEdit.text()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Введите логин и пароль!")
            return

        db = SessionLocal()
        user = get_user_by_username(db, username)
        db.close()

        if user and verify_password(user, password):
            QMessageBox.information(self, "Успех", f"Добро пожаловать, {user.username}!\nВаша роль: {user.role}")
            self.open_main_window(user.role)  # Открываем следующее окно по роли
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль!")
    def open_main_window(self, role):
        # Здесь открывай нужное окно в зависимости от роли
        if role == "admin":
            print("Открываю окно администратора")
        elif role == "teacher":
            print("Открываю окно учителя")
        elif role == "student":
            print("Открываю окно студента")

    def check_pwd(self):
        if self.ui.checkPassword.isChecked():
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())
