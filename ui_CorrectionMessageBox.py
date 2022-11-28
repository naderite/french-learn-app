# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CorrectionMessageBox.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        Dialog.setStyleSheet(u"background-color: rgb(1, 93, 191);\n"
"border-radius: 20px;")
        self.btn_tryagain = QPushButton(Dialog)
        self.btn_tryagain.setObjectName(u"btn_tryagain")
        self.btn_tryagain.setGeometry(QRect(270, 410, 131, 41))
        self.btn_tryagain.setStyleSheet(u"border-radius: 8px;\n"
"background-color: rgb(29, 235, 64);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 14pt \"Segoe UI\";")
        self.btn_goto_menu = QPushButton(Dialog)
        self.btn_goto_menu.setObjectName(u"btn_goto_menu")
        self.btn_goto_menu.setGeometry(QRect(530, 410, 101, 41))
        self.btn_goto_menu.setStyleSheet(u"border-radius: 8px;\n"
"background-color: rgb(238, 31, 31);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Tw Cen MT\";")
        self.msg_txt = QLabel(Dialog)
        self.msg_txt.setObjectName(u"msg_txt")
        self.msg_txt.setGeometry(QRect(30, 20, 581, 361))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.msg_txt.setFont(font)
        self.msg_txt.setLayoutDirection(Qt.LeftToRight)
        self.msg_txt.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.msg_txt.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_tryagain.setText(QCoreApplication.translate("Dialog", u"Ressayer", None))
        self.btn_goto_menu.setText(QCoreApplication.translate("Dialog", u"Menu", None))
        self.msg_txt.setText(QCoreApplication.translate("Dialog", u"mot 1 = syn 1", None))
    # retranslateUi

