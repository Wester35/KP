import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
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
        # Создаём QLabel для фона
        self.background = QLabel(self.ui.frame_2)
        self.background.setGeometry(0, 0, 600, 600)

        # Загружаем изображение как фон
        pixmap = QPixmap("ui/resources/background.jpg")  # Укажи свой путь
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

    def handle_login(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()  # Показываем окно
    sys.exit(app.exec())
