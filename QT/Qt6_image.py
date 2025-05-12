from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget , QLabel , QHBoxLayout , QVBoxLayout , QPushButton , QMainWindow , QSlider , QApplication
from PySide6.QtCore import Qt
import sys

def button1_clicked():
    print("Awwww   !")




#intialize the Qt application
app    = QApplication(sys.argv)
window = QMainWindow()



mainWidget = QWidget()
mainWidget.setWindowTitle("Tutobot")

#creating a normal pushbutton
button_1 = QPushButton()
button_1.setText("Press Me!")
button_1.clicked.connect(button1_clicked)  #connect the button press to the function we created button1_clicked



image_label = QLabel()
image_label.setPixmap(QPixmap("images.png"))



layout = QVBoxLayout()
layout.addWidget(image_label)
layout.addWidget(button_1)
mainWidget.setLayout(layout)



mainWidget.show()



app.exec()


