import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()        
        
    def initUI(self):        
        grid = QGridLayout()
        self.setLayout(grid)
        button1 = QPushButton("Top")
        grid.addWidget(button1, 100, 100)
        button2 = QPushButton("Bottom")
        grid.addWidget(button2, 100, 200)

            
        self.move(300, 150)
        self.setWindowTitle('RB')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
