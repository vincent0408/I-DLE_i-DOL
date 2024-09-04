import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QRadioButton, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        self.move(300, 300)        
        self.ui()
    
    def event_radio_checked(self):
        if(self.radio1.isChecked()):
            return "a8249618-00a1c"
        elif(self.radio2.isChecked()):
            return "a8249618-01afw"
        elif(self.radio3.isChecked()):
            return "a8249618-02bew"

    def ui(self):
        self.setWindowTitle("Simple PyQt6 Program")
        upperleft = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop

        input_box = QLineEdit()
        # input_box.setMinimumWidth(200)

        kktix_button = QPushButton("Go to KKtix")
        kktix_button.setFont(QFont("Times New Roman", 18))
        kktix_button.clicked.connect(lambda: go_to_kktix(self.event_radio_checked()))
        
        self.radio1 = QRadioButton("10/4")
        self.radio2 = QRadioButton("10/5")
        self.radio3 = QRadioButton("10/6")
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.event_radio_checked)
        self.radio2.clicked.connect(self.event_radio_checked)
        self.radio3.clicked.connect(self.event_radio_checked)

        # Create a horizontal layout for the radio buttons
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.radio1)
        h_layout.addWidget(self.radio2)
        h_layout.addWidget(self.radio3)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(kktix_button) 
        self.setLayout(layout)

def go_to_kktix(event_id):
    url = f'https://kktix.com/events/{event_id}/registrations/new'
    options = uc.ChromeOptions()
    # options.add_argument(f"--load-extension={pathlib.Path().absolute()}/CapSolver/")
    driver = uc.Chrome(options=options)
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    driver.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return driver
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())