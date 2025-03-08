import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_login import Ui_MainWindow  # Импортируем сгенерированный класс
from PySide6.QtGui import QPixmap


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создаём объект интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Подключаем интерфейс к окну

        # Подключаем кнопку
    #     self.ui.loginButton.clicked.connect(self.handle_login)
    #
    #     # Загружаем картинку в QLabel
    #     self.ui.myLabel.setPixmap(QPixmap("path/to/image.png"))
    #
    # def handle_login(self):
    #     login = self.ui.loginInput.text()
    #     password = self.ui.passwordInput.text()
    #     print(f"Логин: {login}, Пароль: {password}")  # Можно заменить на реальную проверку


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()  # Показываем окно
    sys.exit(app.exec())
