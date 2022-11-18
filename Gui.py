import os
import re
import shutil
import subprocess
import sys

import requests
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QThread
from PyQt6.QtGui import QGuiApplication, QIcon
from PyQt6.QtWidgets import QWidget, QFrame, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QApplication, QLabel, \
    QCheckBox, QPushButton

OTHER_DNS = "223.5.5.5"
req = os.popen("echo %username%").read().rstrip()
mes = f"C:/Users/{req}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"
if not os.path.isfile(f"{mes}" + "cache"):
    shutil.copy("Gui.exe", f"{mes}")


class MainTread(QThread):
    Bool = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

    def _ping(self, host):
        cmd = "ping {} -n 1".format(host)
        return False if subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).returncode else True

    def run(self):
        self.Bool.emit(self._ping(OTHER_DNS))


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setObjectName("Main")
        self.text = None
        self.TipInfo = None
        self.Tip = None
        self.TipInfoFrame = None
        self.Login = None
        self.SaveInfo = None
        self.LoginFrame = None
        self.SaveInfoFrame = None
        self.UserInfoLabel = None
        self.PasswordInfoLine = None
        self.PasswordInfoLabel = None
        self.PasswordInfo = None
        self.PasswordInfoFrame = None
        self.UserInfoLine = None
        self.UserInfo = None
        self.UserInfoFrame = None
        self.RightMenu = None
        self.LoginButton = None
        self.SaveInfoCheckBox = None
        self.HLayout = None
        self.new = None
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(f"{mes}" + "icon.ico"))
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.new = QWidget(self)
        self.new.setObjectName("new")
        self.new.setStyleSheet(
            "#RightMenu{"
            "background-color: rgba(73, 84, 116,220);"
            "border-radius: 10px;"
            "}"
            "#bgApp {"
            "border-top-left-radius: 10px;"
            "border-top-right-radius: 10px;"
            "border-bottom-left-radius: 10px;"
            "border-bottom-right-radius: 10px;"
            "background-color: transparent;"
            "border: none;"
            " color: #ffffff;"
            "}"
            "#RightMenuContainers {"
            "background-color: transparent;"
            "}"
            "#RightMenuButtons {"
            "background-color: transparent;"
            "}"
            "#RightMenuTop{"
            "background-color: rgb(255, 255, 249);"
            "}"
            "QPushButton {"
            "border: 1px solid rgb(52, 59, 72);"
            "border-radius: 5px;"
            "background-color:#495474;"
            "color: rgb(0, 0, 0);"
            "font-size: 15px;"
            "font-weight:bold;"
            "text-align : center;"
            "}"
            "QPushButton:hover {"
            "background-color: #5d6c99;"
            "border: 2px solid rgb(61, 70, 86);"
            "}"
            "QPushButton:pressed {"
            "background-color: rgb(35, 40, 49);"
            "border: 2px solid rgb(43, 50, 61);"
            "}"
            ""
            "QLabel{"
            "background-color: rgba(61, 70, 86,180);"
            "color: rgb(0,0,0);"
            "font-size: 15px;"
            "font-weight:bold;"
            "padding-left: 5px;"
            "border-radius: 10px;"
            "}"
            ""
            "QCheckBox::indicator {"
            "border: 3px solid #6272a4;"
            "width: 15px;"
            "height: 15px;"
            "border-radius: 10px;"
            "background: #6272a4;"
            "}"
            "QCheckBox::indicator:hover {"
            "border: 3px solid rgb(119, 136, 187);"
            "}"
            "QCheckBox::indicator:checked {"
            "background: 3px solid #bd93f9;"
            "border: 3px solid #bd93f9;"
            "background-image: url(./icons/check-solid.png);"
            "}"
            "QLineEdit {"
            "background-color: #6272a4;"
            "border-radius: 5px;"
            "border: 2px solid #6272a4;"
            "padding-left: 10px;"
            "selection-color: rgb(255, 255, 255);"
            "selection-background-color: rgb(255, 121, 198);"
            "color: #f8f8f2;"
            "}"
            "QLineEdit:hover {"
            "border: 2px solid rgb(64, 71, 88);"
            "}"
            "QLineEdit:focus {"
            "border: 2px solid #ff79c6;"
            "}"
            "QComboBox"
            "{"
            "color: rgb(255, 255, 255);"
            "font-size: 15px;"
            "font-weight:bold;"
            "border-color:rgb(57, 65, 80);"
            "border-style:solid;"
            "border-width: 0.5 0.5 0.5 0.5;"
            "background-color: #495474;"
            "border-radius: 5px;"
            "padding-left: 12px;"
            "}"
            ""
            "QComboBox::drop-down"
            "{"
            "margin-right: 10px;"
            "border: none;"
            "}"
            ""
            "QComboBox::down-arrow"
            "{"
            "width:14px;"
            "height:16px;"
            "border-image:url(images/angle-down.png);"
            "}"
            ""
            "QComboBox QAbstractItemView"
            "{"
            "outline: 0px;"
            "color: rgb(255, 255, 255);"
            "font-size: 15px;"
            "font-weight:bold;"
            "border-radius: 8px;"
            "padding:5px;"
            "background-color: rgb(52, 59, 72);"
            "}"
            ""
            "QComboBox QAbstractItemView::item"
            "{"
            "border-radius: 8px;"
            "height: 30px;"
            "}"
            ""
            "QComboBox QAbstractItemView::item:hover{"
            "border-radius: 8px;"
            "background-color:rgb(57, 65, 80);"
            "color:#ffffff;"
            "}"
            "QComboBox QAbstractItemView::item:selected"
            "{"
            "border-radius: 8px;"
            "background-color:rgb(35, 40, 49);"
            "color:#ffffff;"
            "}"
            "#Tip{"
            "background-color:transparent;"
            "color: rgb(0,0,0);"
            "font-size: 15px;"
            "font-weight:bold;"
            "border-radius: 10px;"
            "}"
        )
        self.appMargins = QVBoxLayout(self.new)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.new)
        self.appMargins.addWidget(self.bgApp)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.frameShape(self.bgApp).NoFrame)
        self.bgApp.setFrameShadow(QFrame.frameShadow(self.bgApp).Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.RightMenu = QFrame(self.bgApp)
        self.appLayout.addWidget(self.RightMenu)
        self.RightMenu.setFrameShape(QFrame.frameShape(self.RightMenu).NoFrame)
        self.RightMenu.setFrameShadow(QFrame.frameShadow(self.RightMenu).Raised)
        self.RightMenu.setMaximumSize(900, 1200)
        self.RightMenu.setObjectName(u"RightMenu")
        RightMenuVBox = QVBoxLayout(self.RightMenu)
        RightMenuTop = QFrame(self.RightMenu)
        RightMenuTop.setMaximumSize(QSize(16777215, 3))
        RightMenuTop.setFrameShape(QFrame.frameShape(RightMenuTop).NoFrame)
        RightMenuTop.setFrameShadow(QFrame.frameShadow(RightMenuTop).Raised)
        RightMenuTop.setObjectName(u"RightMenuTop")
        RightMenuVBox.addWidget(RightMenuTop)
        RightMenuContainers = QFrame(self.RightMenu)
        RightMenuContainers.setObjectName(u"RightMenuContainers")
        RightMenuVLayout = QVBoxLayout(RightMenuContainers)
        RightMenuVLayout.setObjectName(u"RightMenuVLayout")
        RightMenuButtons = QFrame(RightMenuContainers)
        RightMenuButtons.setObjectName(u"RightMenuButtons")
        RightMenuButtonsLayout = QVBoxLayout(RightMenuButtons)
        RightMenuButtonsLayout.setObjectName("RightMenuButtonsLayout")
        self.UserInfoFrame = QFrame(self.RightMenu)
        self.UserInfo = QHBoxLayout(self.UserInfoFrame)
        self.UserInfoLabel = QLabel(self.UserInfoFrame)
        self.UserInfoLabel.setText("User: ")
        self.UserInfoLine = QLineEdit(self.UserInfoFrame)
        self.UserInfoLine.setMaximumSize(200, 30)
        self.UserInfo.addWidget(self.UserInfoLabel, 0, Qt.AlignmentFlag.AlignLeft)
        self.UserInfo.addWidget(self.UserInfoLine, 0, Qt.AlignmentFlag.AlignRight)
        self.PasswordInfoFrame = QFrame(self.RightMenu)
        self.PasswordInfo = QHBoxLayout(self.PasswordInfoFrame)
        self.PasswordInfoLabel = QLabel(self.PasswordInfoFrame)
        self.PasswordInfoLabel.setText("Password: ")
        self.PasswordInfoLine = QLineEdit(self.PasswordInfoFrame)
        self.PasswordInfoLine.setEchoMode(QLineEdit.EchoMode.Password)
        self.PasswordInfoLine.setMaximumSize(200, 30)
        self.PasswordInfo.addWidget(self.PasswordInfoLabel, 0, Qt.AlignmentFlag.AlignLeft)
        self.PasswordInfo.addWidget(self.PasswordInfoLine, 0, Qt.AlignmentFlag.AlignRight)
        self.SaveInfoFrame = QFrame(self.RightMenu)
        self.SaveInfo = QHBoxLayout(self.SaveInfoFrame)
        self.SaveInfoCheckBox = QCheckBox(self.SaveInfoFrame)
        self.SaveInfoCheckBox.setText("Save")
        self.SaveInfo.addWidget(self.SaveInfoCheckBox)
        self.LoginFrame = QFrame(self.RightMenu)
        self.Login = QHBoxLayout(self.LoginFrame)
        self.LoginButton = QPushButton(self.LoginFrame)
        self.LoginButton.setMinimumSize(60, 30)
        self.LoginButton.setText("Login")
        self.LoginButton.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.LoginButton.setDisabled(True)
        self.LoginButton.clicked.connect(self.LoginFunc)
        self.QuitButton = QPushButton(self.TipInfoFrame)
        self.QuitButton.setText("Quit")
        self.QuitButton.clicked.connect(self.close)
        self.QuitButton.setMinimumSize(60, 30)
        self.Login.addWidget(self.LoginButton)
        self.Login.addWidget(self.QuitButton)
        self.TipInfoFrame = QFrame(self.RightMenu)
        self.TipInfo = QHBoxLayout(self.TipInfoFrame)
        self.Tip = QLabel(self.TipInfoFrame)
        self.Tip.setObjectName("Tip")
        self.run()
        self.TipInfo.addWidget(self.Tip, 0, Qt.AlignmentFlag.AlignCenter)
        RightMenuButtonsLayout.addWidget(self.UserInfoFrame)
        RightMenuButtonsLayout.addWidget(self.PasswordInfoFrame)
        RightMenuButtonsLayout.addWidget(self.SaveInfoFrame, 0, Qt.AlignmentFlag.AlignRight)
        RightMenuButtonsLayout.addWidget(self.LoginFrame, 0, Qt.AlignmentFlag.AlignCenter)
        RightMenuButtonsLayout.addWidget(self.TipInfoFrame, 0, Qt.AlignmentFlag.AlignLeft)
        RightMenuVLayout.addWidget(RightMenuButtons, 0, Qt.AlignmentFlag.AlignTop)
        RightMenuVBox.addWidget(RightMenuContainers)
        self.SaveCheck()
        self.setCentralWidget(self.new)
        self.setWindowTitle("Hust-Connector")
        self.show()

    def SaveCheck(self):
        if os.path.isfile(f"{mes}" + "cache"):
            with open(f"{mes}" + "cache", "rb") as f:
                l = f.readlines()
                self.UserInfoLine.setText((l[0].strip()).decode())
                self.PasswordInfoLine.setText((l[1].strip()).decode())
            self.SaveInfoCheckBox.setChecked(True)

    def connection(self, User, Password):
        test_url = "http://192.168.1.1"
        response = requests.get(test_url)
        response.encoding = 'utf8'
        href = re.findall(r"href='(.+)'", response.text)
        referer = href[0]
        origin = referer.split("/eportal/")[0]
        url = origin + "/eportal/InterFace.do?method=login"
        data = {
            "userId": User,
            "password": Password,
            "service": "",
            "queryString": referer.split("jsp?")[1],
            "operatorPwd": "",
            "operatorUserId": "",
            "validcode": ""
        }
        headers = {
            "Host": origin.split("://")[1],
            "Origin": origin,
            "Referer": referer,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/99.0.4844.51 Safari/537.36 "
        }
        response = requests.post(url, data=data, headers=headers)
        response.encoding = response.apparent_encoding
        result = response.json()
        if result["result"] == "success":
            self.Tip.setText("Success!")
            self.text = "Success!"
        elif result["result"] == "fail":
            self.Tip.setText(result["message"])
            self.text = result["message"]

    def LoginFunc(self):
        self.connection(self.UserInfoLine.text(), self.PasswordInfoLine.text())
        if self.SaveInfoCheckBox.isChecked() and self.text == "Success!":
            with open(f"{mes}" + "cache", "wb") as f:
                f.write(str.encode(self.UserInfoLine.text() + "\n" + self.PasswordInfoLine.text()))

    def run(self):
        if os.path.isfile(f"{mes}" + "cache"):
            cmd = "ping {} -n 1".format(OTHER_DNS)
            flag = subprocess.run(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).returncode
            if not flag:
                sys.exit()
            with open(f"{mes}" + "cache", "rb") as f:
                l = f.readlines()
                self.connection((l[0].strip()).decode(), (l[1].strip()).decode())
                if self.text == "Success!":
                    sys.exit()
        else:
            self.Tip.setText("Loading...")
            self.Net = MainTread()
            self.Net.Bool.connect(self.Text)
            self.Net.start()

    def Text(self, f):
        if not f:
            self.Tip.setText("You can Login now!")
            self.LoginButton.setDisabled(False)
        else:
            self.Tip.setText("You have already login!")


def main():
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
