from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from ui import Ui_MainWindow
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
import os
from PyQt5.QtGui import QPixmap

workdir = ''




class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showfiles)
        self.ui.listWidget.currentRowChanged.connect(self.showchosenfiles)
        self.image = None


    def chooseworkdir(self):
        global workdir
        workdir = QFileDialog.getExistingDirectory()

    


    def showfiles(self):
        extentions = ['.png','.jpg','.jpeg','.gif', 'svg','.bmp']
        self.ui.listWidget.clear()
        self.chooseworkdir()
        filenames = os.listdir(workdir)
        for file in filenames:
            for ext in extentions:   
                if file.endswith(ext):
                    self.ui.listWidget.addItem(file)

    def showimage(self, path):
        self.ui.label.hide()
        pix = QPixmap(path)
        pix = pix.scaled(self.ui.label.size(), aspectRatioMode=Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pix)
        self.ui.label.show()

    def saveimage(self):
        self.ui.pushButton_9.clicked.connect(self.saveimage)
        if self.image:
            try:
                save_path, _ = QFileDialog.getSaveFileName(self, "Зберегти зображення", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
                if save_path:
                    self.image.save(save_path)
                    print("Зображення збережено!")
            except (IOError, OSError):
                print("Помилка: Неможливо зберегти зображення!")


    
    def showchosenfiles(self):
        self.ui.pushButton_2.clicked.connect(self.saveimage)
        if self.ui.listWidget.currentRow() >= 0:
            file = self.ui.listWidget.currentItem().text()
            print(file)
            image_path = os.path.join(workdir, file)
            self.image = Image.open(image_path)
            self.showimage(image_path)

        
    def blackwhite(self):
        self.ui.pushButton_3.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')
                self.image = self.image.convert("L")
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати чорно-біле перетворення!")

    def sharpen(self):
        self.ui.pushButton_4.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.filter(ImageFilter.SHARPEN)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати різкість!")

    def flip(self):
        self.ui.pushButton_5.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати відзеркалення!")

    def left(self):
        self.ui.pushButton_6.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.transpose(Image.ROTATE_270)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати поворот!")

    def right(self):
        self.ui.pushButton_7.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.transpose(Image.ROTATE_90)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати поворот!")

    def blur(self):
        self.ui.pushButton_8.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.filter(ImageFilter.BLUR)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати розмиття!")

    def ehnance(self):
        self.ui.pushButton.clicked.connect(self.saveimage)
        if self.image:
            try:
                self.image = self.image.convert('RGB')  
                self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
                image_path = os.path.join(workdir, "temp.jpg")
                self.image.save(image_path)
                self.showimage(image_path)
            except (AttributeError, IOError, OSError):
                print("Помилка: Неможливо виконати контур!")
    
    
    



app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
