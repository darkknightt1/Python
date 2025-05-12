from PySide6.QtWidgets import QApplication ,QWidget ,QPushButton,QMainWindow,QHBoxLayout,QVBoxLayout,QSlider
from PySide6.QtCore import Qt
#libarary that process command lines , needed by the Qt library 
import sys


def button1_clicked():
    print("Awwww   !")
    
def button2_clicked(data):#data hold whether checked or not
    print("Awwww   !",data)

def Slider_Function(data):
    print(data)

#intialize the Qt application
app = QApplication(sys.argv)

#creating a normal pushbutton
button_1 = QPushButton()
button_1.setText("Press Me!")
button_1.clicked.connect(button1_clicked)  #connect the button press to the function we created button1_clicked

#creating a checklist pushbutton , either checked or unchecked
button_2 = QPushButton()
button_2.setText("Press Me!")
button_2.setCheckable(True)
button_2.clicked.connect(button2_clicked)  #connect the button press to the function we created button1_clicked
#-----------------------------------------------------------------------------------------
#creating a slider
slider=QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.valueChanged.connect(Slider_Function)

#create main widget , widget is ملصق which is anything you want to add to your gui ex: button ,slider , label or just empty 
mainWidget=QWidget()
mainWidget.setWindowTitle("Window-1")
#creating a widget layout and adding buttons to it
widget_layout = QHBoxLayout()#QVBoxLayout()
widget_layout.addWidget(button_1)
widget_layout.addWidget(button_2)
widget_layout.addWidget(slider)

#assigning the created layout to the main widget we created
mainWidget.setLayout(widget_layout)
mainWidget.show()
#window.setCentralWidget(button_2)



#infinite loop
app.exec()
