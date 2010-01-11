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
# import flaker
from flaker import Flaker, Flak, FlakUser
class EntryWidget(QWidget):
  def __init__(self, entry, parent = None):
    QWidget.__init__(self, parent)

    self.entry = entry
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.setSizePolicy(sizePolicy)
    self.setObjectName("entryContainer")

    self.entryWidget = QWidget(self)
    self.entryWidget.setObjectName("entry")
    self.avatar = QtWebKit.QWebView(self.entryWidget)
    self.avatar.setGeometry(QtCore.QRect(15, 15, 50, 50))
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.avatar.setSizePolicy(sizePolicy)
    self.avatar.setUrl(QtCore.QUrl(entry.user.avatar))
    self.avatar.setObjectName("avatar")


    self.verticalLayoutWidget = QWidget(self.entryWidget)
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    self.verticalLayoutWidget.setSizePolicy(sizePolicy)
    self.verticalLayoutWidget.move(70, 10)
    self.verticalLayoutWidget.setMinimumSize(QtCore.QSize(400, 100))
    # self.verticalLayoutWidget.setSizeIncrement(QtCore.QSize(0, 10))
    self.verticalLayoutWidget.setBaseSize(QtCore.QSize(400, 100)) 
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
    self.userName.setText(entry.user.login)
    self.userName.adjustSize()
    self.userName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    self.verticalLayout.addWidget(self.userName)
    
    
    self.message = QLabel(self.verticalLayoutWidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    self.message.setSizePolicy(sizePolicy)
    self.message.setFixedWidth(300)
    self.message.setObjectName("message")
    self.message.setWordWrap(True)
    self.message.setText(entry.text)
    self.message.adjustSize()
    self.message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    # self.message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
    


    self.verticalLayout.addWidget(self.message)

    self.pushButton = QPushButton(self.verticalLayoutWidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
    self.pushButton.setSizePolicy(sizePolicy)
    self.pushButton.setObjectName("sendButton")
    self.pushButton.setText("Skomentuj")

    self.verticalLayout.addWidget(self.pushButton)

    self.verticalLayoutWidget.adjustSize()
    self.entryWidget.adjustSize()
    self.adjustSize()

    self.setMinimumWidth(self.width())    
    self.setMinimumHeight(self.height())
    
    self.connect(self.pushButton, QtCore.SIGNAL('clicked()'),
        self.button_click)
        
    self.clickStatus = None
        
    
  def mouseReleaseEvent(self, event):
    if self.clickStatus == "double":
      self.emit(QtCore.SIGNAL("doubleClick(str)"), self.entry.id)

  
  def mouseDoubleClickEvent(self, event):
    self.clickStatus = "double"
    
  def button_click(event):
    # del self.avatar
    print "click"
  
class LoginWidget(QWidget):
  def __init__(self, flakerService, parent = None):
    QWidget.__init__(self, parent)
    
    self.flakerService = flakerService
    self.formLayoutWidget = QtGui.QWidget(self)
    self.formLayoutWidget.setGeometry(QtCore.QRect(0, 20, 400, 200))
    self.formLayoutWidget.setObjectName("loginWidget")
    self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
    self.formLayout.setObjectName("formLayout")
    self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
    self.usernameLabel = QtGui.QLabel(self.formLayoutWidget)
    self.usernameLabel.setObjectName("usernameLabel")
    self.usernameLabel.setText(u"Login")
    self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.usernameLabel)
    self.usernameField = QtGui.QLineEdit(self.formLayoutWidget)
    self.usernameField.setObjectName("usernameField")
    self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.usernameField)
    self.passwordLabel = QtGui.QLabel(self.formLayoutWidget)
    self.passwordLabel.setObjectName("passwordLabel")
    self.passwordLabel.setText(u"Hasło")
    self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.passwordLabel)
    self.passwordField = QtGui.QLineEdit(self.formLayoutWidget)
    self.passwordField.setEchoMode(QtGui.QLineEdit.Password)
    self.passwordField.setObjectName("passwordField")
    self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.passwordField)
    self.loginButton = QtGui.QPushButton(self.formLayoutWidget)
    self.loginButton.setObjectName("loginButton")
    self.loginButton.setText("Zaloguj")
    self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.loginButton)
    self.wrongCredentials = QtGui.QLabel(self.formLayoutWidget)
    self.wrongCredentials.setObjectName("label")
    self.wrongCredentials.setText(u"Złe dane")
    self.wrongCredentials.hide()
    self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.wrongCredentials)
    
    self.connect(self.loginButton, QtCore.SIGNAL('clicked()'), self.login)
    self.adjustSize()
    
    
  def login(self):
    self.flakerService.authorize(login=self.usernameField.text(), password=self.passwordField.text())
    authorized = False
    try:
      authorized = self.flakerService.auth()
    except:
      authorized = False
    
    if authorized:
      self.emit(QtCore.SIGNAL("loggedon"))
    else: 
      self.wrongCredentials.show()
        
class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=0):
        
        QMainWindow.__init__(self, parent)
        self.flakerService = Flaker()
        
        self.resize(400, 500)
        self.centralWidget = QWidget(self)
        self.centralWidget.setObjectName("centralWidget")
        self.setCentralWidget(self.centralWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
     
        layout = QGridLayout(self.centralWidget)
        layout.setMargin(0)
        
        
        self.title = QLabel()
        self.title.setMinimumWidth(400)
        self.title.setText("FlaPy")
        self.title.setObjectName("title")
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
        layout.addWidget(self.title)
        
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 400, 500))
        layout.addWidget(self.scrollArea)
        
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.createEntryListWidget()
        self.loginWidget = LoginWidget(self.flakerService)
        self.connect(self.loginWidget, QtCore.SIGNAL("loggedon"), self.login)
        self.scrollArea.setWidget(self.loginWidget)
        

        
        f = open("entry.css", "r")
        stylesheet = f.read()
        f.close
        self.setStyleSheet(stylesheet)
        

    def createEntryListWidget(self):
      self.entryListContainer = QWidget()
      sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
      self.entryListContainer.setSizePolicy(sizePolicy)
      self.entryListContainer.setSizeIncrement(QtCore.QSize(0, 10))
      self.entryListContainer.setBaseSize(QtCore.QSize(300, 100))
      self.entryListContainer.setObjectName("container")
      self.entryListLayout = QVBoxLayout(self.entryListContainer)
      self.entryListLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
      self.entryListLayout.setObjectName("entryListLayout")
      self.entryListLayout.setMargin(0)

      self.entrywidgets = []

      # entries = flakerService.getNewEntries("piotrj")
      entries = self.flakerService.friends("piotrj", 1)
      
      for entry in entries:
        widget = EntryWidget(entry, self.entryListContainer)
        self.entrywidgets.append(widget)
        self.entryListLayout.addWidget(widget)
        self.connect(widget, QtCore.SIGNAL("doubleClick(str)"), self.doubleClick)
        
      self.entryListContainer.adjustSize()

  
    def createEntryDetailWidget(self, id):
      self.detailContainer = QWidget()
      sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
      self.detailContainer.setSizePolicy(sizePolicy)
      self.detailContainer.setSizeIncrement(QtCore.QSize(0, 10))
      self.detailContainer.setBaseSize(QtCore.QSize(400, 100))
      self.detailContainer.setObjectName("container")   
      self.detailLayout = QVBoxLayout(self.detailContainer)
      self.detailLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
      self.detailLayout.setObjectName("detailLayout")
      self.detailLayout.setMargin(0)

      entry = self.flakerService.show(id)

      self.detailwidgets = []
      widget = EntryWidget(entry, self.detailContainer)
      self.detailwidgets.append(widget)
      self.detailLayout.addWidget(widget)

      for comment in entry.comments:
        widget = EntryWidget(comment, self.detailContainer)
        self.detailwidgets.append(widget)
        self.detailLayout.addWidget(widget)   
        
    def doubleClick(self, id):
      self.createEntryDetailWidget(id)
      self.entryListContainer.hide()
      self.scrollArea.setWidget(self.detailContainer)
    
    def login(self):
      self.createEntryListWidget()
      self.scrollArea.setWidget(self.entryListContainer)
      self.entryListContainer.adjustSize()
      del self.loginWidget
      
      self.centralWidget.adjustSize()
      self.centralWidget.setFixedWidth(self.centralWidget.sizeHint().width()+15)
      self.centralWidget.setMaximumWidth(self.centralWidget.width())
        
if __name__ == "__main__": 
  app = QApplication(sys.argv) 
  window = Ui_MainWindow() 
  window.show()
  app.exec_()
