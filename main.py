import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_login import Ui_MainWindow  # Импортируем сгенерированный класс
from PySide6.QtGui import QPixmap


class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Подключение кнопок
        self.ui.pushButton.clicked.connect(self.handle_login)

        self.ui.toolButton.setIcon(QPixmap("ui/resources/free-icon-login-1674704.png"))

    def handle_login(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()  # Показываем окно
    sys.exit(app.exec())
