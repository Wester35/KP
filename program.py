from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from ui.ui_login import Ui_Authorization as LoginUI  # Ваш класс авторизации
from ui.ui_main import Ui_MainWindow  # Ваш основной класс
import sys


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация основного окна (не создаем отдельный QWidget)
        self.ui = Ui_MainWindow()  # Загружаем UI основного окна
        self.ui.setupUi(self)  # Применяем UI к основному окну

        # Получаем доступ к QStackedWidget из UI
        self.stacked_widget = self.ui.stackedWidget

        # Инициализация авторизации
        self.login_widget = QWidget()  # Создаем виджет для авторизации
        self.login_ui = LoginUI()  # Загружаем UI авторизации
        self.login_ui.setupUi(self.login_widget)  # Применяем UI к виджету

        # Добавляем оба виджета в QStackedWidget
        self.stacked_widget.addWidget(self.login_widget)  # Добавляем окно авторизации
        self.stacked_widget.addWidget(self)  # Главное окно (self.ui уже применен)

        # Устанавливаем начальный виджет (авторизация)
        self.stacked_widget.setCurrentWidget(self.login_widget)

        # Привязываем кнопку "Войти" к переключению экранов
        self.login_ui.pushButton.clicked.connect(self.show_main_window)

    def show_main_window(self):
        """Переключаем на главное окно после авторизации"""
        self.stacked_widget.setCurrentWidget(self)  # Главное окно


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Инициализация и запуск приложения
    main_app = MainApp()
    main_app.show()

    sys.exit(app.exec())
