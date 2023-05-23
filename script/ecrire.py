#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                               Here git the code of a simple
                
#                            notepad, not specially useful but at least simplier                      |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                  to modify or customize rathen than the one natively present on windows os               |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                   |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#            You normally should be able to open any file texts by drag'n' drop in a tab or not
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
                
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
      

import sys, fitz, os,json, csv,markdown,yaml

from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

from PyQt5 import QtGui
from PyQt5.QtCore import  Qt, QTextStream, QFile, QIODevice
from PyQt5.QtGui import  QKeySequence, QIcon
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QMessageBox, QTextEdit,QShortcut , QTabWidget, QMenu, QFileDialog, QAction, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDialog, QColorDialog



#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


#Here we set the config.ini, initialy it was ".theme_color_ecrire.ini"
#But I had some issues with to write in a hidden file so I left it for now
THEME_FILE_NAME = "theme_color_ecrire.ini"


#function to make an exe file with py to exe
def ressource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path ,relative_path)
#to make it works, you have to rename all your path with ressource_path (/path/) WHEN YOU WILL TURN THE SCRIPT TO EXE
#Example : /icon/lol.png  BECOME  ressource_path(/icon/lol.png)





#The main class for the notepad
class ecriture(QMainWindow):
    def __init__(self):
        super().__init__()

        self.GUI()




#____ ___  ____ _  _    ____ _ _    ____ ____ 
#|  | |__] |___ |\ |    |___ | |    |___ [__  
#|__| |    |___ | \|    |    | |___ |___ ___] 
                                             


#Function to listen drag files events
    def dragEnterEvent(self, event):

        #Check if the drag event contains URLs
        if event.mimeData().hasUrls():

            #Accept the proposed action
            event.acceptProposedAction()



#Function to drop files in the app
    def dropEvent(self, event):
        #Get the list of URLs from the drag event
        urls = event.mimeData().urls()

        #Loop through each URL and open the associated file
        for url in urls:
            file_path = url.toLocalFile()

            if file_path:
                self.open_file(file_path)



#Function to open all kinds of files using different libraries relative to extensions files
    def open_file(self, file_name):

        file_ext = file_name.split('.')[-1].lower()
        content = ""    

        with open(file_name, 'r', encoding='utf-8') as file:
            if file_ext in ['txt', 'md']:
                content = file.read()

                if file_ext == 'md':
                    content = markdown.markdown(content)

            elif file_ext == 'html':
                soup = BeautifulSoup(file, 'html.parser')
                content = soup.prettify()

            elif file_ext == 'xml':
                tree = ET.parse(file)
                content = ET.tostring(tree.getroot(), encoding='unicode')

            elif file_ext == 'csv':
                reader = csv.reader(file)
                content = "\n".join([", ".join(row) for row in reader])

            elif file_ext == 'tsv':
                reader = csv.reader(file, delimiter='\t')
                content = "\n".join(["\t".join(row) for row in reader])

            elif file_ext == 'json':
                data = json.load(file)
                content = json.dumps(data, indent=4)

            elif file_ext == 'yaml':
                data = yaml.safe_load(file)
                content = yaml.dump(data, default_flow_style=False) 

            elif file_ext == 'pdf':
                data = fitz.open(file_name)
                #We read all pages for pdf files to get text
                for page in data:
                    content += page.get_text()
                data.close()

        #Create a new ta widget with the PDF content and file path attributes
        if content:
            text_edit = QTextEdit()
            text_edit.setPlainText(content)
            text_edit.file_path = file_name

            self.tabs.addTab(text_edit, file_name.split("/")[-1]) #Add the new tab

        else:
            QMessageBox.warning(self, "Error", "Unsupported file format.")  






#___ ____ ___  ____ 
# |  |__| |__] [__  
# |  |  | |__] ___] 
                   


#Function to create a new tab with a QTextEdit widget
    def new_tab(self):
        text_edit = QTextEdit()
        self.apply_theme_colors(text_edit)       #Apply the current theme colors to the QTextEdit widget
        self.tabs.addTab(text_edit, "Untitled")  #Add the new tab to the tab widget with the default name "Untitled"
    


#Function to close tab
    def close_tab(self, index):

        #Get the tab widget at the given index
        tab = self.tabs.widget(index)
        #Check if the user wants to save any unsaved changes before closing the tab
        
        if self.maybe_save(tab):
            self.tabs.removeTab(index)

        else:
            return




#Function to close only the current tab
    def close_current_tab(self):

        #Check if there are any tabs open
        if self.tabs.count() > 0:

            #Get the index of the currently active tab
            current_index = self.tabs.currentIndex()

            #Call the close_tab function with the current index
            self.close_tab(current_index)





#____ ____ _  _ ____    ____ ___  ___ _ ____ _  _ ____ 
#[__  |__| |  | |___    |  | |__]  |  | |  | |\ | [__  
#___] |  |  \/  |___    |__| |     |  | |__| | \| ___] 


#Save function
    def save(self):

        #Get the current tab widget
        current_tab = self.tabs.currentWidget()

        #If the current tab widget has a file path attribute and it is not empty, save to that file
        if hasattr(current_tab, "file_path") and current_tab.file_path:
            self.save_to_file(current_tab.file_path)

        #Otherwise, prompt the user to choose a file name and save to that file
        else:
            self.save_as()




#Save as
    def save_as(self):

        options = QFileDialog.Options()

        #Prompt the user to choose a file name and location to save the file
        file_name, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Text Files (*.txt);;All Files (*)", options=options)

        #If a file name was chosen, save to that file
        if file_name:
            self.save_to_file(file_name)





#Save in an opened file
    def save_to_file(self, file_name):

        current_tab = self.tabs.currentWidget()

        file = QFile(file_name)
        if file.open(QIODevice.WriteOnly | QIODevice.Text):

            #Write the text content of the current tab widget to the file
            text_stream = QTextStream(file)
            text_stream << current_tab.toPlainText()
            file.close()

            #Set the file path attribute of the current tab widget to the saved file path
            current_tab.file_path = file_name

            #Update the tab text to display the file name
            self.tabs.setTabText(self.tabs.currentIndex(), file_name.split("/")[-1])

    





#___  ____ ____ _  _ 
#  /  |  | |  | |\/| 
# /__ |__| |__| |  | 
                    



#Function to scale the fonts of a given widget and its children by a given scale factor
    def scale_fonts(self, widget, scale_factor):

        #Loop through all children of the given widget
        for child in widget.children():
            #Check if the child is a widget

            if isinstance(child, QWidget):

                #Scale the child's font size by the given scale factor
                font = child.font()
                font.setPointSizeF(font.pointSizeF() * scale_factor)
                child.setFont(font) 

                #Recursively apply the scale factor to all children of the child widget
                self.scale_fonts(child, scale_factor)




#Function to zoom in/out when the user scrolls with the mouse
    def wheelEvent(self, event):

        #Check if the user is holding down the Ctrl key

        if QApplication.keyboardModifiers() == Qt.ControlModifier:

            #Get the amount scrolled by the user
            delta = event.angleDelta().y()

            #Determine if the mouse is over a QTextEdit widget
            widget_under_cursor = self.childAt(event.pos())
            is_over_text_edit = isinstance(widget_under_cursor, QTextEdit) or (widget_under_cursor is not None and isinstance(widget_under_cursor.parentWidget(), QTextEdit))

            #Zoom in/out based on the scroll direction and whether the mouse is over a QTextEdit widget
            if delta > 0:
                if is_over_text_edit:
                    self.zoom_text(1.1)
                else:
                    self.zoom(1.1)
            elif delta < 0:
                if is_over_text_edit:
                    self.zoom_text(1 / 1.1)
                else:
                    self.zoom(1 / 1.1)




#Function to zoom in/out when the user presses the "+" or "-" keys
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Plus:
            self.zoom(1.1)

        elif event.key() == Qt.Key_Minus:
            self.zoom(1 / 1.1)

        else:
            super().keyPressEvent(event)





#Function to apply the zoom factor to the application
    def zoom(self, scale_factor):

        #Exclude QTextEdit widgets from being scaled
        if not isinstance(self.focusWidget(), QTextEdit):

            #Scale the fonts of the application and its children by the given scale factor
            self.scale_fonts(self, scale_factor)




#Function to zoom the text of the current tab by a given scale factor
    def zoom_text(self, scale_factor):
        current_tab = self.tabs.currentWidget()

        if current_tab:
            font = current_tab.font()
            font.setPointSizeF(font.pointSizeF() * scale_factor)
            current_tab.setFont(font)








#____ ____ _    ____ ____ ____ 
#|    |  | |    |  | |__/ [__  
#|___ |__| |___ |__| |  \ ___] 
#                              


#Here we define the theme of the application 

#Function to save the current theme colors to a file
    def save_theme_colors(self):

        #Create a file path for the theme colors file
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), THEME_FILE_NAME)

        try:

            #Open to rewrite
            with open(file_path, "w") as theme_file:

                #Write the current text and background colors to the file
                theme_file.write(f"{self.color_text}\n{self.color_background}")


        except PermissionError:
            #Warning if the user 's not permited to save the theme colors file (useful for hidden config.ini)
            QMessageBox.warning(self, "Permission Error", "Unable to save theme colors. Please check file permissions and try again.")
    
    
#Function to load the theme colors from a file
    def load_theme_colors(self):

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), THEME_FILE_NAME)

        try:
            #Read only
            with open(file_path, "r") as theme_file:

                #Read the text and background colors from the file
                self.color_text = theme_file.readline().strip()
                self.color_background = theme_file.readline().strip()
                #print(f"COuleurs chargées:Text-{self.color_text}, Background - {self.color_background}")  # to debug
    
                #Apply the theme colors to existing tabs
                for index in range(self.tabs.count()):
                    tab = self.tabs.widget(index)
                    self.apply_theme_colors_to_app()

        #If the theme colors file does not exist, use default colors    
        except FileNotFoundError:


            self.color_text = "black"
            self.color_background = "white"

            self.apply_theme_colors_to_app()
    


    
#Function to apply the current theme colors to a tab
    def apply_theme_colors(self, text_edit):
        text_edit.setStyleSheet(f"background-color: {self.color_background}; color: {self.color_text};")
        self.setStyleSheet(f"QMainWindow {{background-color: {self.color_background}; color: {self.color_text};}}")
    
    


#Function to apply the current theme colors to whole app
    def apply_theme_colors_to_app(self):
        #Create a new palette for the application and set the colors
        palette = self.palette()

        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(self.color_background))
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(self.color_text))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(self.color_background))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(self.color_text))

        self.tabs.setPalette(palette)
    
    



#Function to apply theme colors to a QTextEdit widget
    def apply_theme_colors(self, text_edit):
        text_edit.setStyleSheet(f"background-color: {self.color_background}; color: {self.color_text};")




#Function to ask if want to change colors (need some rework)
    def maybe_save(self, tab):

        #Display a message box asking the user if they want to save their changes
        reply = QMessageBox.question(self, 'Save changes ?',
                                     "Would you like to save changes ?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        #If the user wants to save, set the current tab to the one being closed and call the save_as function
        if reply == QMessageBox.Yes:
            self.tabs.setCurrentWidget(tab)
            self.save_as()
            return True
        
        elif reply == QMessageBox.No:
            return True
        
        else:
            return False



#Function to update all tabs color
    def update_tab_colors(self, color_text=None, color_background=None):
        #If there is no text color use the default color
        if color_text is None:
            color_text = self.color_text

        #Same for the background tabs
        if color_background is None:
            color_background = self.color_background

        #Loop through all tabs and set their stylesheets to use the updated colors
        for index in range(self.tabs.count()):
            tab = self.tabs.widget(index)
            tab.setStyleSheet(f"background-color: {color_background}; color: {color_text};")





#Let user to pick the color to apply for the tabs texts
    def change_color_text(self):

        #Choose the color with
        color = QColorDialog.getColor()

        #Avoid errors by checking if the color exists
        if color.isValid():

            #Updates the current text color
            self.color_text = color.name()

            #Updates the color of the btn_color_txt (the colored square but rectangle ) with the selected color
            self.btn_color_txt.setStyleSheet(f"background-color: {self.color_text};")

            #Updates the color of all open tabs with the selected color
            self.update_tab_colors(color_text=self.color_text)

            #Saves the new theme colors to the settings file
            self.save_theme_colors()

            #Applies the new theme colors to the entire application
            self.apply_theme_colors_to_app()    




#Let user to pick the color to apply for the tabs background
    def change_color_background(self):

        color = QColorDialog.getColor()

        if color.isValid():
            self.color_background = color.name()
            self.btn_color_background.setStyleSheet(f"background-color: {self.color_background};")

            self.update_tab_colors(color_background=self.color_background)
            self.save_theme_colors()
            self.apply_theme_colors_to_app()    






#____ ____ ____ ___  _  _ _ ____ ____ _       _  _ ____ ____ ____    _ _  _ ___ ____ ____ ____ ____ ____ ____ 
#| __ |__/ |__| |__] |__| | |    |__| |       |  | [__  |___ |__/    | |\ |  |  |___ |__/ |___ |__| |    |___ 
#|__] |  \ |  | |    |  | | |___ |  | |___    |__| ___] |___ |  \    | | \|  |  |___ |  \ |    |  | |___ |___ 
#                                                                                                            


#GUI to change colors of the application
    def theme_changer_GUI(self):

        #Dialog window for the theme
        dial_theme = QDialog(self)
        dial_theme.setWindowTitle("Color mode")
        dial_theme.setFixedSize(200, 100)


        #Labels to notify what is what
        lab_color_change = QLabel("Change tabs colors :")
        lab_color_txt = QLabel("Text :")
        lab_color_background = QLabel("Background :")

        #Button to change text tabs color 
        self.btn_color_txt = QPushButton()
        self.btn_color_txt.setStyleSheet(f"background-color: {self.color_text};")
        self.btn_color_txt.clicked.connect(self.change_color_text)


        #Button to change background tabs color 
        self.btn_color_background = QPushButton()
        self.btn_color_background.setStyleSheet(f"background-color: {self.color_background};")
        self.btn_color_background.clicked.connect(self.change_color_background)


        #Horizontal layout for the text color in tabs
        H_lay_color_text = QHBoxLayout()
        H_lay_color_text.addWidget(lab_color_txt)
        H_lay_color_text.addWidget(self.btn_color_txt)


        #Horizontal layout for the background color in tabs
        H_lay_color_background = QHBoxLayout()
        H_lay_color_background.addWidget(lab_color_background)
        H_lay_color_background.addWidget(self.btn_color_background)


        #Vertical layout for theme page
        V_lay_theme = QVBoxLayout()
        V_lay_theme.addWidget(lab_color_change)
        V_lay_theme.addLayout(H_lay_color_text)
        V_lay_theme.addLayout(H_lay_color_background)

        #Set the layout of the dialog window and show it
        dial_theme.setLayout(V_lay_theme)

        dial_theme.exec_()






#Function to create main menus and their actions
    def main_menus(self):

        #Get menu bar
        menu_bar = self.menuBar()

    #Function to create new file + shortcut
        action_new_file = QAction("New", self)
        action_new_file.setShortcut(QKeySequence.New)
        action_new_file.triggered.connect(self.new_tab)


    #Function to save current tab + shortcut
        action_save = QAction("Save", self)
        action_save.setShortcut(QKeySequence.Save)
        action_save.triggered.connect(self.save)


    #Function to "save as" current tab + shortcut
        action_save_as = QAction("Save as +", self)
        action_save_as.setShortcut(QKeySequence("Ctrl+Shift+S"))
        action_save_as.triggered.connect(self.save_as)


    #Function to open in a tab
        action_open = QAction("Open", self)
        action_open.setShortcut(QKeySequence.Open)
        action_open.triggered.connect(self.open_file)



        #Add a "Theme" action to the "Display" menu
        action_theme = QAction("Mode", self)
        action_theme.triggered.connect(self.theme_changer_GUI)



        #Add actions to the "file" menu
        file_menu = QMenu("Files", self)

        file_menu.addAction(action_new_file)
        file_menu.addAction(action_save)
        file_menu.addAction(action_save_as)
        file_menu.addAction(action_open)


        #Add actions to the "display" menu
        menu_view = QMenu("Display", self)

        menu_view.addAction(action_theme)


        #Show the menus
        menu_bar.addMenu(file_menu)
        menu_bar.addMenu(menu_view)







#The main graphical user interface (GUI)
    def GUI(self):

        self.setWindowTitle('Ecrire')
        self.setWindowIcon(QIcon(ressource_path(r"ico\ecrire.png")))

        #Style of the whole application (css)
        self.setStyleSheet("""
            QMessageBox {
                background-color: darkgray;
                color: white;
            }       

            QMenuBar {
                background-color: darkgray;
                color: white;
            }

            QMenuBar::item:selected {
                background-color: gray;
            }

            QMenu {
                background-color: darkgray;
                color: white;
            }

            QMenu::item:selected {
                background-color: gray;
            }

        """)        


        #Create a tab widget to hold multiple open files
        self.tabs = QTabWidget()


        #Enable the closing tabs requests
        self.tabs.setTabsClosable(True)

        #Connect the tabCloseRequested signal to close tabs
        self.tabs.tabCloseRequested.connect(self.close_tab)


        #Enable the application to accept drops from other applications
        self.setAcceptDrops(True)

        #Close tabs with ctrl w
        X_tabs = QShortcut(QKeySequence("Ctrl+W"), self)
        X_tabs.activated.connect(self.close_current_tab)


        #Load theme colors from a configuration file
        self.load_theme_colors()


        #Set the central widget as tabs
        self.setCentralWidget(self.tabs)



        #Create the menus
        self.main_menus()







#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3
         

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    herodote = ecriture()
    herodote.show()
    
    sys.exit(app.exec_())
