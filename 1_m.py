from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import os

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
       
        self.label_login = QLabel("Login:", self)
        self.label_login.move(20, 20)
        self.line_edit_login = QLineEdit(self)
        self.line_edit_login.move(80, 20)
        
        self.label_password = QLabel("Password:", self)
        self.label_password.move(20, 60)
        self.line_edit_password = QLineEdit(self)
        self.line_edit_password.move(80, 60)
        self.line_edit_password.setEchoMode(QLineEdit.Password)  

       
        self.button_signin = QPushButton("SignIn", self)
        self.button_signin.move(20, 100)
        self.button_signin.clicked.connect(self.sign_in)

        self.button_signup = QPushButton("SignUp", self)
        self.button_signup.move(100, 100)
        self.button_signup.clicked.connect(self.sign_up)

        # Faylga yo'lni belgilash
        self.file_path = "users.txt"
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Login System")
        self.show()

    def sign_in(self):
        login = self.line_edit_login.text()
        password = self.line_edit_password.text()

        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                users = [line.strip().split(":") for line in file]
                for user_login, user_password in users:
                    if user_login == login and user_password == password:
                        QMessageBox.information(self, "Success", "Siz tizimga kirdingiz")
                        return
                QMessageBox.warning(self, "Error", "Login yoki parol noto'g'ri")
        else:
            QMessageBox.warning(self, "Error", "Foydalanuvchi ma'lumotlari fayli topilmadi")

    def sign_up(self):
        login = self.line_edit_login.text()
        password = self.line_edit_password.text()

        if not login or not password:
            QMessageBox.warning(self, "Error", "Login va parolni kiriting")
            return

        users = []
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                users = [line.strip().split(":") for line in file]
        
        if len(users) >= 10:
            for user_login, _ in users:
                if user_login == login:
                    QMessageBox.warning(self, "Error", "Bu login allaqachon mavjud")
                    return
            with open(self.file_path, "a") as file:
                file.write(f"{login}:{password}\n")
            QMessageBox.information(self, "Success", "Foydalanuvchi qo'shildi")
        else:
            QMessageBox.warning(self, "Error", "Kamida 10 foydalanuvchi mavjud emas")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = LoginApp()
    sys.exit(app.exec_())
