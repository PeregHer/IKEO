
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Popup(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("IkeoOoooooo")
        self.msg.setStyleSheet("color: #003399; background-color: #FFCC00")

    def champ_vide_err(self, champs):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Les champs {champs} doivent être renseignés")
    	x = self.msg.exec_()

    def ref_exist_err(self):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Cette référence existe déjà dans la base !")
    	x = self.msg.exec_()    	

    def connex_err(self):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Une erreur est survenue. Vérifiez votre connexion avec le serveur.")
    	x = self.msg.exec_()   