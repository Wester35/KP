import os
from PIL import Image
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog
from libs.database import SessionLocal
from models.User import User
from ui.ui_main import Ui_MainWindow as UI_Main


class MainApp(QWidget):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_Main()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.ui.frame.setVisible(False)
        self.ui.pushButton.clicked.connect(self.upload_image)
        self.ui.profileButton.clicked.connect(self.open_frame)
        self.ui.closeButton.clicked.connect(self.close_frame)


    def open_frame(self):
        self.ui.frame.setVisible(True)

    def close_frame(self):
        self.ui.frame.setVisible(False)

    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self,
                                                   "Выберите фото", "", "Images (*.png *.jpg *.jpeg)")
        if not file_path:
            return


        save_dir = "libs/user_images"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        save_path = os.path.join(save_dir, f"{self.user_id}.jpg")

        try:
            img = Image.open(file_path)
            img = img.convert("RGB")
            img.thumbnail((300, 300))
            img.save(save_path, "JPEG", quality=85)

            self.save_image_path_to_db(save_path)

            QMessageBox.information(self, "Успешно", "Фото загружено!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось загрузить фото: {str(e)}")

    def save_image_path_to_db(self, image_path):
        db = SessionLocal()
        user = db.query(User).filter(User.id == self.user_id).first()
        if user:
            user.photo = image_path
            db.commit()
        db.close()