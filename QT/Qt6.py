from PySide6.QtWidgets import QApplication ,QWidget ,QPushButton,QMainWindow,QSlider
from PySide6.QtCore import Qt
#libarary that process command lines , needed by the Qt library 
import sys


def button1_clicked():
    print("Awwww   !")

def button2_clicked(data):
    print("Awwww   !",data)

def Slider_Function(data):
    print(data)
    

#intialize the Qt application
app=QApplication(sys.argv)

#create main window
window=QMainWindow()

#creating a normal pushbutton
button_1 = QPushButton()
button_1.setText("Press Me!")
button_1.clicked.connect(button1_clicked)  #connect the button press to the function we created button1_clicked

#creating a checklist pushbutton , either checked or unchecked
button_2 = QPushButton()
button_2.setText("Press Me!")
button_2.setCheckable(True)
button_2.clicked.connect(button2_clicked)  #connect the button press to the function we created button1_clicked

#creating a slider
slider=QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.valueChanged.connect(Slider_Function)

window.setCentralWidget(button_2)
#show the main window we created
window.show()


#infinite loop
app.exec()
