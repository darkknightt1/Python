from PySide6.QtWidgets import QApplication ,QWidget ,QPushButton,QMainWindow,QHBoxLayout,QVBoxLayout ,QStatusBar
from PySide6.QtCore import Qt ,QSize
#libarary that process command lines , needed by the Qt library 
import sys



def Quit_Fuction():
    global app
    app.quit()
    
def Message_Fuction():
    global window
    window.statusBar().showMessage("Hello guys____!",3000) #show this message to the statusbar of the window mainwindow 
    
    


#intialize the Qt application
app=QApplication(sys.argv)

#create main window , window is more gneral than widget ,they can include ,taskbar ,menubar ,...
window=QMainWindow()
window.setWindowTitle("My application")

#menubar and menus and actions 
#menubar is a bar intop that contain anything we want in the window
menu_bar = window.menuBar()
file_menu = menu_bar.addMenu("File")
edit_menu = menu_bar.addMenu("Edit")
setting_menu = menu_bar.addMenu("Settings")
#menubar actions
#action is the set of actions that can actually be done inside each item in the menu Ex: save ,save as ,Quit actions inside "File"
Quit_action = file_menu.addAction("Quit")
Quit_action.triggered.connect(Quit_Fuction)
Message_action = file_menu.addAction("Message")
Message_action.triggered.connect(Message_Fuction)

#Status bar, shown at the bottom to show messages for example
window.setStatusBar(QStatusBar()) #u can add the message u want when a certain action is done


window.show()

#infinite loop
app.exec()
