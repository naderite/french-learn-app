# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grammaire_levelPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(654, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.512, y1:0, x2:0.512, y2:1, stop:0 rgba(252, 216, 70, 255), stop:1 rgba(254, 249, 108, 255));")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"background-color: rgb(a255, 255, 255,0);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.content_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(70)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setContentsMargins(9, 21, 9, 20)
        self.btn_word10 = QPushButton(self.content_frame)
        self.btn_word10.setObjectName(u"btn_word10")
        self.btn_word10.setMinimumSize(QSize(0, 50))
        self.btn_word10.setMaximumSize(QSize(260, 16777215))
        self.btn_word10.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word10, 4, 2, 1, 1)

        self.word2_guess = QLineEdit(self.content_frame)
        self.word2_guess.setObjectName(u"word2_guess")
        self.word2_guess.setMaximumSize(QSize(260, 16777215))
        self.word2_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word2_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word2_guess, 1, 1, 1, 1)

        self.btn_word4 = QPushButton(self.content_frame)
        self.btn_word4.setObjectName(u"btn_word4")
        self.btn_word4.setMinimumSize(QSize(0, 50))
        self.btn_word4.setMaximumSize(QSize(260, 16777215))
        self.btn_word4.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word4, 2, 0, 1, 1)

        self.btn_word2 = QPushButton(self.content_frame)
        self.btn_word2.setObjectName(u"btn_word2")
        self.btn_word2.setMinimumSize(QSize(0, 50))
        self.btn_word2.setMaximumSize(QSize(260, 16777215))
        self.btn_word2.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word2, 0, 2, 1, 1)

        self.word4_guess = QLineEdit(self.content_frame)
        self.word4_guess.setObjectName(u"word4_guess")
        self.word4_guess.setMaximumSize(QSize(260, 16777215))
        self.word4_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word4_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word4_guess, 1, 3, 1, 1)

        self.word7_guess = QLineEdit(self.content_frame)
        self.word7_guess.setObjectName(u"word7_guess")
        self.word7_guess.setMaximumSize(QSize(260, 16777215))
        self.word7_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word7_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word7_guess, 3, 2, 1, 1)

        self.word9_guess = QLineEdit(self.content_frame)
        self.word9_guess.setObjectName(u"word9_guess")
        self.word9_guess.setMaximumSize(QSize(260, 16777215))
        self.word9_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word9_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word9_guess, 5, 0, 1, 1)

        self.word12_guess = QLineEdit(self.content_frame)
        self.word12_guess.setObjectName(u"word12_guess")
        self.word12_guess.setMaximumSize(QSize(260, 16777215))
        self.word12_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word12_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word12_guess, 5, 3, 1, 1)

        self.btn_word8 = QPushButton(self.content_frame)
        self.btn_word8.setObjectName(u"btn_word8")
        self.btn_word8.setMinimumSize(QSize(0, 50))
        self.btn_word8.setMaximumSize(QSize(260, 16777215))
        self.btn_word8.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word8, 4, 0, 1, 1)

        self.word8_guess = QLineEdit(self.content_frame)
        self.word8_guess.setObjectName(u"word8_guess")
        self.word8_guess.setMaximumSize(QSize(260, 16777215))
        self.word8_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word8_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word8_guess, 3, 3, 1, 1)

        self.btn_word0 = QPushButton(self.content_frame)
        self.btn_word0.setObjectName(u"btn_word0")
        self.btn_word0.setMinimumSize(QSize(0, 50))
        self.btn_word0.setMaximumSize(QSize(260, 16777215))
        font = QFont()
        font.setFamilies([u"Book Antiqua"])
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.btn_word0.setFont(font)
        self.btn_word0.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word0, 0, 0, 1, 1)

        self.word10_guess = QLineEdit(self.content_frame)
        self.word10_guess.setObjectName(u"word10_guess")
        self.word10_guess.setMaximumSize(QSize(260, 16777215))
        self.word10_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word10_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word10_guess, 5, 1, 1, 1)

        self.word6_guess = QLineEdit(self.content_frame)
        self.word6_guess.setObjectName(u"word6_guess")
        self.word6_guess.setMaximumSize(QSize(260, 16777215))
        self.word6_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word6_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word6_guess, 3, 1, 1, 1)

        self.word5_guess = QLineEdit(self.content_frame)
        self.word5_guess.setObjectName(u"word5_guess")
        self.word5_guess.setMaximumSize(QSize(260, 16777215))
        self.word5_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word5_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word5_guess, 3, 0, 1, 1)

        self.btn_word3 = QPushButton(self.content_frame)
        self.btn_word3.setObjectName(u"btn_word3")
        self.btn_word3.setMinimumSize(QSize(0, 50))
        self.btn_word3.setMaximumSize(QSize(260, 16777215))
        self.btn_word3.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word3, 0, 3, 1, 1)

        self.btn_word7 = QPushButton(self.content_frame)
        self.btn_word7.setObjectName(u"btn_word7")
        self.btn_word7.setMinimumSize(QSize(0, 50))
        self.btn_word7.setMaximumSize(QSize(260, 16777215))
        self.btn_word7.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word7, 2, 3, 1, 1)

        self.word3_guess = QLineEdit(self.content_frame)
        self.word3_guess.setObjectName(u"word3_guess")
        self.word3_guess.setMaximumSize(QSize(260, 16777215))
        self.word3_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word3_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word3_guess, 1, 2, 1, 1)

        self.word11_guess = QLineEdit(self.content_frame)
        self.word11_guess.setObjectName(u"word11_guess")
        self.word11_guess.setMaximumSize(QSize(260, 16777215))
        self.word11_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word11_guess.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.word11_guess, 5, 2, 1, 1)

        self.btn_word1 = QPushButton(self.content_frame)
        self.btn_word1.setObjectName(u"btn_word1")
        self.btn_word1.setMinimumSize(QSize(0, 50))
        self.btn_word1.setMaximumSize(QSize(260, 16777215))
        self.btn_word1.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word1, 0, 1, 1, 1)

        self.btn_word9 = QPushButton(self.content_frame)
        self.btn_word9.setObjectName(u"btn_word9")
        self.btn_word9.setMinimumSize(QSize(0, 50))
        self.btn_word9.setMaximumSize(QSize(260, 16777215))
        self.btn_word9.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word9, 4, 1, 1, 1)

        self.btn_word6 = QPushButton(self.content_frame)
        self.btn_word6.setObjectName(u"btn_word6")
        self.btn_word6.setMinimumSize(QSize(0, 50))
        self.btn_word6.setMaximumSize(QSize(290, 16777215))
        self.btn_word6.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word6, 2, 2, 1, 1)

        self.btn_word11 = QPushButton(self.content_frame)
        self.btn_word11.setObjectName(u"btn_word11")
        self.btn_word11.setMinimumSize(QSize(0, 50))
        self.btn_word11.setMaximumSize(QSize(260, 16777215))
        self.btn_word11.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word11, 4, 3, 1, 1)

        self.btn_word5 = QPushButton(self.content_frame)
        self.btn_word5.setObjectName(u"btn_word5")
        self.btn_word5.setMinimumSize(QSize(0, 50))
        self.btn_word5.setMaximumSize(QSize(260, 16777215))
        self.btn_word5.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(23, 182, 214);\n"
"border-color: rgb(108, 108, 108);\n"
"font: 700 24pt \"Book Antiqua\";\n"
"color:rgb(225, 255, 255);")

        self.gridLayout_2.addWidget(self.btn_word5, 2, 1, 1, 1)

        self.word1_guess = QLineEdit(self.content_frame)
        self.word1_guess.setObjectName(u"word1_guess")
        self.word1_guess.setMaximumSize(QSize(260, 16777215))
        self.word1_guess.setLayoutDirection(Qt.LeftToRight)
        self.word1_guess.setAutoFillBackground(False)
        self.word1_guess.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgba(255, 239, 233, 250);\n"
"font: 20pt \"Calisto MT\";\n"
"color: rgb(43, 43, 43);")
        self.word1_guess.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.word1_guess, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.content_frame, 1, 0, 1, 1)

        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setMaximumSize(QSize(16777215, 200))
        self.title_frame.setStyleSheet(u"background-color: rgb(a255, 255, 255,0);")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.title_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(9, 0, 9, 8)
        self.lvl_title = QLabel(self.title_frame)
        self.lvl_title.setObjectName(u"lvl_title")
        self.lvl_title.setMinimumSize(QSize(100, 0))
        self.lvl_title.setMaximumSize(QSize(16777215, 120))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(64)
        font1.setBold(True)
        font1.setItalic(False)
        self.lvl_title.setFont(font1)
        self.lvl_title.setStyleSheet(u"color:rgb(214, 2, 48);\n"
"font: 700 64pt \"Tw Cen MT\";")
        self.lvl_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.lvl_title, 0, 2, 1, 1)

        self.btn_goto_menu = QPushButton(self.title_frame)
        self.btn_goto_menu.setObjectName(u"btn_goto_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_goto_menu.sizePolicy().hasHeightForWidth())
        self.btn_goto_menu.setSizePolicy(sizePolicy1)
        self.btn_goto_menu.setMinimumSize(QSize(140, 50))
        self.btn_goto_menu.setMaximumSize(QSize(140, 50))
        self.btn_goto_menu.setStyleSheet(u"background-color:rgb(229, 36, 39);\n"
"color: white;\n"
"font: 600 16pt \"Segoe UI Semibold\";\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.btn_goto_menu, 0, 3, 1, 1)

        self.btn_correct = QPushButton(self.title_frame)
        self.btn_correct.setObjectName(u"btn_correct")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_correct.sizePolicy().hasHeightForWidth())
        self.btn_correct.setSizePolicy(sizePolicy2)
        self.btn_correct.setMinimumSize(QSize(180, 60))
        self.btn_correct.setMaximumSize(QSize(140, 50))
        self.btn_correct.setStyleSheet(u"background-color: rgb(0, 212, 0);\n"
"border-radius: 10px;\n"
"color: rgb(252, 255, 234);\n"
"font: 700 18pt \"Segoe UI Variable Text\";")

        self.gridLayout.addWidget(self.btn_correct, 0, 1, 1, 1)

        self.lvl_question = QLabel(self.title_frame)
        self.lvl_question.setObjectName(u"lvl_question")
        sizePolicy1.setHeightForWidth(self.lvl_question.sizePolicy().hasHeightForWidth())
        self.lvl_question.setSizePolicy(sizePolicy1)
        self.lvl_question.setMinimumSize(QSize(16, 30))
        self.lvl_question.setMaximumSize(QSize(1270, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(20)
        self.lvl_question.setFont(font2)
        self.lvl_question.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.lvl_question.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lvl_question, 3, 2, 1, 1)


        self.gridLayout_3.addWidget(self.title_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_word10.setText(QCoreApplication.translate("MainWindow", u"mot11", None))
        self.btn_word4.setText(QCoreApplication.translate("MainWindow", u"mot5", None))
        self.btn_word2.setText(QCoreApplication.translate("MainWindow", u"mot3", None))
        self.btn_word8.setText(QCoreApplication.translate("MainWindow", u"mot9", None))
        self.btn_word0.setText(QCoreApplication.translate("MainWindow", u"mot1", None))
        self.btn_word3.setText(QCoreApplication.translate("MainWindow", u"mot4", None))
        self.btn_word7.setText(QCoreApplication.translate("MainWindow", u"mot8", None))
        self.btn_word1.setText(QCoreApplication.translate("MainWindow", u"mot2", None))
        self.btn_word9.setText(QCoreApplication.translate("MainWindow", u"mot10", None))
        self.btn_word6.setText(QCoreApplication.translate("MainWindow", u"mot7", None))
        self.btn_word11.setText(QCoreApplication.translate("MainWindow", u"mot12", None))
        self.btn_word5.setText(QCoreApplication.translate("MainWindow", u"mot6", None))
        self.word1_guess.setText("")
        self.lvl_title.setText(QCoreApplication.translate("MainWindow", u"Titre ", None))
        self.btn_goto_menu.setText(QCoreApplication.translate("MainWindow", u"Au menu", None))
        self.btn_correct.setText(QCoreApplication.translate("MainWindow", u"Corriger", None))
        self.lvl_question.setText(QCoreApplication.translate("MainWindow", u"consigne", None))
    # retranslateUi

