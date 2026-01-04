from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from random import choice

import sys

answers = ["It is certain",
         "It is decidedly so",
         "Without a doubt", 
         "Yes - definitely", 
         "You may rely on it", 
         "As I see it, yes", 
         "Most likely", 
         "Outlook good", 
         "Yes", 
         "Signs point to yes", 
         "Don't count on it", 
         "My reply is no", 
         "My sources say no", 
         "Outlook no so good", 
         "Very doubtful", 
         "Ask again later", 
         "Reply hazy, try again", 
         "Better not tell you now", 
         "Cannot Predict now", 
         "Concentrate and ask again"
        ]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("magic 8 Ball")

        self.answer = QLabel("Please enter a question in the text box below.")

        self.input = QLineEdit()

        self.yes = QPushButton("Ask the question!")
        self.yes.clicked.connect(self.yes_clicked)
        self.no = QPushButton("Exit")
        self.no.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.answer)
        layout.addWidget(self.input)
        layout.addWidget(self.yes)
        layout.addWidget(self.no)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def yes_clicked(self):
        new_label = choice(answers)
        self.input.setText("")
        self.answer.setText(new_label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()