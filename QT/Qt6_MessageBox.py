from PySide6.QtWidgets import QApplication ,QWidget ,QPushButton,QMainWindow,QVBoxLayout,QSlider,QMessageBox
from PySide6.QtCore import Qt
#libarary that process command lines , needed by the Qt library 
import sys


def button1_clicked():
    print("Awwww   !")
    message = QMessageBox()
    message.setMinimumSize(700,200)
    message.setWindowTitle("Warning")
    message.setText("Warningggggg")
    message.setInformativeText("Do you want to kill emara")
    message.setIcon(QMessageBox.Critical)
    message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    message.setDefaultButton(QMessageBox.Ok)
    ret = message.exec()
    if ret == QMessageBox.Ok:
        print("Ok")
    else:
        print("Cancel")
        
        
    
def button2_clicked(data):#data hold whether checked or not
    print("Awwww2   !",data)



#intialize the Qt application
app=QApplication(sys.argv)

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


#create main widget , widget is ملصق which is anything you want to add to your gui ex: button ,slider , label or just empty 
mainWidget=QWidget()
mainWidget.setWindowTitle("Window-1")
#creating a widget layout and adding buttons to it
widget_layout = QVBoxLayout()
widget_layout.addWidget(button_1)
widget_layout.addWidget(button_2)

#assigning the created layout to the main widget we created
mainWidget.setLayout(widget_layout)
mainWidget.show()



#infinite loop
app.exec()
