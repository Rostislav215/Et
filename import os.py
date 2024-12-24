import os 
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageFilter


from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtMultimediaWidgets import QVideoWidget

workdir = ""
class ImageEditor:
    def __init__(self):
        self.image = None
        self.folder = "modifyed"
        self.filemane = None
    def  load_image(self):
        path = os.path.join(workdir, self.filemane)
        self.image = Image.open(path)
        
    def showImage(self,path):
        ui.piccher.hide()
        pixmap  = QtGui.QPixmap(path)
        w, h = ui.piccher.width(), ui.piccher.height()
        pixmap = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        ui.piccher.setPixmap(pixmap)
        ui.piccher.show()
    def seve_imag(self,name):
        path = os.path.join(workdir,self.folder,name + self.filemane)
        if not os.path.isdir(os.path.join(workdir,self.folder)):
            os.makedirs(os.path.join(workdir,self.folder))
        self.image.save(path)
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.seve_imag("left")
        path = os.path.join(workdir,self.folder,"left" + self.filemane)
        self.showImage(path)
    def black(self):
        self.image = self.image.convert('L')
        self.seve_imag("black")
        path = os.path.join(workdir,self.folder,"black" + self.filemane)
        self.showImage(path)
    def blurred(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.seve_imag("blurred")
        path = os.path.join(workdir,self.folder,"blurred" + self.filemane)
        self.showImage(path)
        
imag = ImageEditor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1206, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.folder = QtWidgets.QPushButton(self.centralwidget)
        self.folder.setGeometry(QtCore.QRect(60, 40, 93, 28))
        self.folder.setObjectName("folder")
        self.W_B_btn = QtWidgets.QPushButton(self.centralwidget)
        self.W_B_btn.setGeometry(QtCore.QRect(910, 560, 93, 28))
        self.W_B_btn.setObjectName("W_B_btn")
        self.mirror = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.left_btn.setGeometry(QtCore.QRect(260, 560, 93, 28))
        self.left_btn.setObjectName("left_btn")
        self.right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.right_btn.setGeometry(QtCore.QRect(410, 560, 93, 28))
        self.right_btn.setObjectName("right_btn")
        self.shatpeness = QtWidgets.QPushButton(self.centralwidget)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 221, 551))
        self.listWidget.setObjectName("listWidget")
        self.piccher = QtWidgets.QLabel(self.centralwidget)
        self.piccher.setGeometry(QtCore.QRect(254, 90, 921, 421))
        self.piccher.setText("")
        self.piccher.setObjectName("piccher")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.folder.clicked.connect(self.open_folder)
        self.left_btn.clicked.connect(imag.left)
        self.W_B_btn.clicked.connect(imag.black)
        self.right_btn.clicked.connect(imag.blurred)
        self.listWidget.clicked.connect(self.choseImage)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.folder.setText(_translate("MainWindow", "Папки"))
        self.W_B_btn.setText(_translate("MainWindow", "Ч/Б"))
        self.left_btn.setText(_translate("MainWindow", "Переміщяти"))
        self.right_btn.setText(_translate("MainWindow", "Розмито"))
    def open_folder(self):
        global workdir
        self.listWidget.clear()
        workdir = QtWidgets.QFileDialog.getExistingDirectory()
        
        print(workdir)
        
        filenames = os.listdir(workdir)
        
        
        self.listWidget.addItems(filenames)
    def choseImage(self):
        filemane = self.listWidget.currentItem().text()
        imag.filemane = filemane
        imag.load_image()
        path = os.path.join(workdir,filemane)
        imag.showImage(path)
    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



