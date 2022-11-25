# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grammaire_menuPage.ui'
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
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1295, 510)
        MainWindow.setStyleSheet(u"border-radius: 1px")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.21, x2:1, y2:1, stop:0 rgba(199, 103, 107, 255), stop:1 rgba(248, 161, 121, 255));")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.centralwidget)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(0, 0))
        self.side_menu.setMaximumSize(QSize(300, 16777215))
        self.side_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_menu.setStyleSheet(u"background-color: rgb(157, 81, 88);")
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.side_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_to_eval = QToolButton(self.side_menu)
        self.btn_to_eval.setObjectName(u"btn_to_eval")
        self.btn_to_eval.setMaximumSize(QSize(500, 70))
        self.btn_to_eval.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_to_eval.setStyleSheet(u"background-color: rgb(255, 202, 71);\n"
"border-radius: 20px;\n"
"color: white;\n"
"font: 700 22pt \"Segoe UI Variable Display\";")

        self.gridLayout.addWidget(self.btn_to_eval, 6, 0, 1, 1)

        self.btn_to_vocab = QToolButton(self.side_menu)
        self.btn_to_vocab.setObjectName(u"btn_to_vocab")
        self.btn_to_vocab.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_to_vocab.sizePolicy().hasHeightForWidth())
        self.btn_to_vocab.setSizePolicy(sizePolicy)
        self.btn_to_vocab.setMaximumSize(QSize(500, 70))
        self.btn_to_vocab.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_to_vocab.setLayoutDirection(Qt.LeftToRight)
        self.btn_to_vocab.setStyleSheet(u"background-color: rgb(255, 202, 71);\n"
"border-radius: 20px;\n"
"color: white;\n"
"font: 700 22pt \"Segoe UI Variable Display\";")

        self.gridLayout.addWidget(self.btn_to_vocab, 2, 0, 1, 1)

        self.btn_to_conj = QToolButton(self.side_menu)
        self.btn_to_conj.setObjectName(u"btn_to_conj")
        self.btn_to_conj.setMaximumSize(QSize(500, 70))
        self.btn_to_conj.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_to_conj.setStyleSheet(u"background-color: rgb(255, 202, 71);\n"
"border-radius: 20px;\n"
"color: white;\n"
"font: 700 22pt \"Segoe UI Variable Display\";")

        self.gridLayout.addWidget(self.btn_to_conj, 5, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.side_menu)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setEnabled(False)
        self.toolButton_2.setMaximumSize(QSize(500, 70))
        self.toolButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet(u"background-color: rgba(255, 202, 71,70);\n"
"border-radius: 20px;\n"
"color: rgba(255,255,255,200);\n"
"font: 700 22pt \"Segoe UI Variable Display\";")

        self.gridLayout.addWidget(self.toolButton_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(41, 56, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.side_menu, 0, 0, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.gridLayout_5 = QGridLayout(self.main_menu)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 26, -1, -1)
        self.title_frame = QFrame(self.main_menu)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 200))
        self.title_frame.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.title_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Sitka Heading Semibold"])
        font.setPointSize(61)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(255, 202, 71);\n"
"background-color: rgba(255, 255, 255,0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.title_frame, 0, 0, 1, 1)

        self.content_frame = QFrame(self.main_menu)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.content_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setContentsMargins(50, 40, 23, 0)
        self.btn_acc_lvl0 = QPushButton(self.content_frame)
        self.btn_acc_lvl0.setObjectName(u"btn_acc_lvl0")
        self.btn_acc_lvl0.setMinimumSize(QSize(0, 70))
        self.btn_acc_lvl0.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_acc_lvl0.setFont(font1)
        self.btn_acc_lvl0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acc_lvl0.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.btn_acc_lvl0, 3, 0, 1, 1)

        self.btn_acc_lvl1 = QPushButton(self.content_frame)
        self.btn_acc_lvl1.setObjectName(u"btn_acc_lvl1")
        self.btn_acc_lvl1.setMinimumSize(QSize(0, 70))
        self.btn_acc_lvl1.setMaximumSize(QSize(16777215, 16777215))
        self.btn_acc_lvl1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acc_lvl1.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_acc_lvl1, 3, 1, 1, 1)

        self.label_2 = QLabel(self.content_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(30)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgb(255, 202, 71);\n"
"\n"
"background-color: rgba(255, 255, 255,0);\n"
"font: 700 30pt \"Verdana\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Ignored, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 2, 1, 1)

        self.btn_acc_lvl3 = QPushButton(self.content_frame)
        self.btn_acc_lvl3.setObjectName(u"btn_acc_lvl3")
        self.btn_acc_lvl3.setMinimumSize(QSize(0, 70))
        self.btn_acc_lvl3.setMaximumSize(QSize(16777215, 16777215))
        self.btn_acc_lvl3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acc_lvl3.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_acc_lvl3, 4, 1, 1, 1)

        self.btn_nom_lvl1 = QPushButton(self.content_frame)
        self.btn_nom_lvl1.setObjectName(u"btn_nom_lvl1")
        self.btn_nom_lvl1.setMinimumSize(QSize(0, 70))
        self.btn_nom_lvl1.setMaximumSize(QSize(16777215, 16777215))
        self.btn_nom_lvl1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nom_lvl1.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_nom_lvl1, 3, 4, 1, 1)

        self.btn_nom_lvl3 = QPushButton(self.content_frame)
        self.btn_nom_lvl3.setObjectName(u"btn_nom_lvl3")
        self.btn_nom_lvl3.setMinimumSize(QSize(0, 70))
        self.btn_nom_lvl3.setMaximumSize(QSize(16777215, 16777215))
        self.btn_nom_lvl3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nom_lvl3.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_nom_lvl3, 4, 4, 1, 1)

        self.btn_nom_lvl2 = QPushButton(self.content_frame)
        self.btn_nom_lvl2.setObjectName(u"btn_nom_lvl2")
        self.btn_nom_lvl2.setMinimumSize(QSize(0, 70))
        self.btn_nom_lvl2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_nom_lvl2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nom_lvl2.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_nom_lvl2, 4, 3, 1, 1)

        self.btn_nom_lvl0 = QPushButton(self.content_frame)
        self.btn_nom_lvl0.setObjectName(u"btn_nom_lvl0")
        self.btn_nom_lvl0.setMinimumSize(QSize(0, 70))
        self.btn_nom_lvl0.setMaximumSize(QSize(16777215, 16777215))
        self.btn_nom_lvl0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_nom_lvl0.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_nom_lvl0, 3, 3, 1, 1)

        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 60))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:rgb(255, 202, 71);\n"
"background-color: rgba(255, 255, 255,0);\n"
"font: 700 30pt \"Verdana\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_3, 1, 3, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.label_4 = QLabel(self.content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 60))
        self.label_4.setStyleSheet(u"color:rgb(255, 202, 71);\n"
"\n"
"background-color: rgba(255, 255, 255,0);\n"
"font: 700 30pt \"Verdana\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 2)

        self.btn_acc_lvl2 = QPushButton(self.content_frame)
        self.btn_acc_lvl2.setObjectName(u"btn_acc_lvl2")
        self.btn_acc_lvl2.setMinimumSize(QSize(0, 70))
        self.btn_acc_lvl2.setMaximumSize(QSize(16777215, 16777215))
        self.btn_acc_lvl2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_acc_lvl2.setStyleSheet(u"border-radius:20px;\n"
"background-color:rgb(102, 109, 198); \n"
"font: 700 20pt \"Tahoma\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.gridLayout_3.addWidget(self.btn_acc_lvl2, 4, 0, 1, 1)


        self.gridLayout_5.addWidget(self.content_frame, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.main_menu, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_to_eval.setText(QCoreApplication.translate("MainWindow", u"Evaluation", None))
        self.btn_to_vocab.setText(QCoreApplication.translate("MainWindow", u"Vocabulaire", None))
        self.btn_to_conj.setText(QCoreApplication.translate("MainWindow", u"Conjugaison", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"Grammaire", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"R\u00e9vision de grammaire", None))
        self.btn_acc_lvl0.setText(QCoreApplication.translate("MainWindow", u"Niveau 0", None))
        self.btn_acc_lvl1.setText(QCoreApplication.translate("MainWindow", u"Niveau 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Accord", None))
        self.btn_acc_lvl3.setText(QCoreApplication.translate("MainWindow", u"Niveau 3", None))
        self.btn_nom_lvl1.setText(QCoreApplication.translate("MainWindow", u"Niveau 1", None))
        self.btn_nom_lvl3.setText(QCoreApplication.translate("MainWindow", u"Niveau 3", None))
        self.btn_nom_lvl2.setText(QCoreApplication.translate("MainWindow", u"Niveau 2", None))
        self.btn_nom_lvl0.setText(QCoreApplication.translate("MainWindow", u"Niveau 0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nominalisation", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" des adjectives", None))
        self.btn_acc_lvl2.setText(QCoreApplication.translate("MainWindow", u"Niveau 2", None))
    # retranslateUi

