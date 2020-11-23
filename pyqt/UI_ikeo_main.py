import sys
from fenetres import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QStyleFactory

def main():
	app = QApplication.instance() 
	if not app:
		app = QApplication(sys.argv)
	app.setStyle(QStyleFactory.create("Fusion"))

	fen = Fenetre()
	fen.show()

	app.exec_()

main()