# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jan  8 17:03:43 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtWebKit, QtGui
from PyQt4.QtGui import *
import sys
import flaker

class EntryWidget(QWidget):
  def __init__(self, entry, parent = None):
    QWidget.__init__(self, parent)

    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.setSizePolicy(sizePolicy)
    self.setObjectName("entryContainer")

    self.entry = QWidget(self)
    self.entry.setObjectName("entry")
    self.avatar = QtWebKit.QWebView(self.entry)
    self.avatar.setGeometry(QtCore.QRect(15, 15, 50, 50))
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.avatar.setSizePolicy(sizePolicy)
    self.avatar.setUrl(QtCore.QUrl(entry["user"]["avatar"]))
    self.avatar.setObjectName("avatar")


    self.verticalLayoutWidget = QWidget(self.entry)
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.verticalLayoutWidget.setSizePolicy(sizePolicy)
    self.verticalLayoutWidget.move(70, 10)
    self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(300, 100))
    self.verticalLayoutWidget.setSizeIncrement(QtCore.QSize(0, 10))
    self.verticalLayoutWidget.setBaseSize(QtCore.QSize(300, 100)) 
    self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

    self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
    self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
    self.verticalLayout.setObjectName("verticalLayout")
    self.verticalLayout.setMargin(0)
    
    self.userName = QLabel(self.verticalLayoutWidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    self.userName.setSizePolicy(sizePolicy)
    self.userName.setFixedWidth(300)
    self.userName.setObjectName("username")
    self.userName.setWordWrap(True)
    self.userName.setText(entry["user"]["login"])
    self.userName.adjustSize()
    self.userName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.verticalLayout.addWidget(self.userName)
    
    
    self.message = QLabel(self.verticalLayoutWidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    self.message.setSizePolicy(sizePolicy)
    self.message.setFixedWidth(300)
    self.message.setObjectName("message")
    self.message.setWordWrap(True)
    self.message.setText(entry["text"])
    self.message.adjustSize()
    self.message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)


    self.verticalLayout.addWidget(self.message)

    self.pushButton = QPushButton(self.verticalLayoutWidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
    self.pushButton.setSizePolicy(sizePolicy)
    self.pushButton.setObjectName("sendButton")
    self.pushButton.setText("Skomentuj")

    self.verticalLayout.addWidget(self.pushButton)

    self.verticalLayoutWidget.adjustSize()
    self.entry.adjustSize()
    self.adjustSize()

    self.setMinimumWidth(self.width())    
    self.setMinimumHeight(self.height())
    
    self.connect(self.pushButton, QtCore.SIGNAL('clicked()'),
        self.button_click)
        
    self.clickStatus = None
    
  def mouseReleaseEvent(self, event):
    if self.clickStatus == "double":
      print "double"
    self.clickStatus = None
  
  def mouseDoubleClickEvent(self, event):
    self.clickStatus = "double"
    
  def button_click(event):
    print "click"

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=0):
        
        QMainWindow.__init__(self, parent)
        # self.setObjectName("MainWindow")
        self.resize(300, 500)
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)
     
        layout = QGridLayout(self.centralWidget)
        
        self.scrollArea = QtGui.QScrollArea()
        layout.addWidget(self.scrollArea)
        layout.setMargin(0)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 300, 500))
        
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.verticalLayoutWidget2 = QWidget()
        self.scrollArea.setWidget(self.verticalLayoutWidget2)
        
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.verticalLayoutWidget2.setSizePolicy(sizePolicy)
        # self.verticalLayoutWidget2.setGeometry(QtCore.QRect(10, 10, 500, 1000))
        self.verticalLayoutWidget2.setSizeIncrement(QtCore.QSize(0, 10))
        self.verticalLayoutWidget2.setBaseSize(QtCore.QSize(300, 100))
        self.verticalLayoutWidget2.setObjectName("container")
        self.verticalLayout2 = QVBoxLayout(self.verticalLayoutWidget2)
        self.verticalLayout2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.verticalLayout2.setMargin(0)
        # self.widget = EntryWidget(self.centralWidget)
        # self.widget.adjustSize()
        # self.widget2 = EntryWidget(self.verticalLayoutWidget2)
        # self.widget3 = EntryWidget(self.verticalLayoutWidget2)
        # self.widget4 = EntryWidget(self.verticalLayoutWidget2)
        # 
        # self.verticalLayout2.addWidget(self.widget)
        # self.verticalLayout2.addWidget(self.widget2)
        # self.verticalLayout2.addWidget(self.widget3)
        # self.verticalLayout2.addWidget(self.widget4)
        # 
        # self.verticalLayoutWidget2.adjustSize()
        # self.scrollArea.setWidget(self.verticalLayoutWidget2)
        # self.setCentralWidget(self.scrollArea)
        self.entrywidgets = []
        
        entries = flaker.getEntries("piotrj")
        for entry in entries["entries"]:
          widget = EntryWidget(entry, self.verticalLayoutWidget2)
          self.entrywidgets.append(widget)
          self.verticalLayout2.addWidget(widget)
          
        
        self.verticalLayoutWidget2.adjustSize()
        self.centralWidget.setFixedWidth(self.centralWidget.sizeHint().width()+15)
        self.centralWidget.setMaximumWidth(self.centralWidget.width())
        
        f = open("entry.css", "r")
        stylesheet = f.read()
        f.close
        self.setStyleSheet(stylesheet)


if __name__ == "__main__": 
  app = QApplication(sys.argv) 
  window = Ui_MainWindow() 
  window.show()
  app.exec_()
