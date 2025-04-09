import sys
from PySide6.QtWidgets import QApplication
from controllers.crud import load_user_session, check_if_logged_in
from views.auth_window import Auth
from views.main_window import MainApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    session_data = load_user_session()
    if session_data and session_data.get("user_id"):
        user_id, is_teacher, is_admin = check_if_logged_in()
        main_app = MainApp(user_id, is_teacher, is_admin)
        main_app.show()
    else:
        main_app = Auth()
        main_app.show()

    sys.exit(app.exec())
