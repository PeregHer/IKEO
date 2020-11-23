import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStyleFactory, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox, QMessageBox
from bdd import Bdd
from popup import Popup

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(400,50,300,450)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        self.initUI()
        self.initCmd()

    def initUI(self):
        self.logo = QLabel()
        self.logo.setGeometry(0,0,300,107)
        self.logo.setText("")
        self.logo.setPixmap(QPixmap("ikeo.png"))
        self.logo.setScaledContents(True)
        self.texte_invit = QLabel("HCenter", self )
        self.texte_invit.setText("Bienvenue ! Que souhaitez-vous faire ?")
        self.texte_invit.setAlignment(Qt.AlignCenter)
        self.bprodsite = QPushButton("Afficher les produits et leurs sites de production") 
        self.bfacdate = QPushButton("Afficher les factures par date")
        self.bsaisfac = QPushButton("Saisir une facture")        
        self.bsaisclient = QPushButton("Entrer un nouveau client en base")
        self.bsite = QPushButton("Afficher les informations des sites de production")
        self.bsaisprod = QPushButton("Saisir un nouveau produit")

        layout = QVBoxLayout()
        layout.addWidget(self.logo)   
        layout.addWidget(self.texte_invit)
        layout.addWidget(self.bprodsite)
        layout.addWidget(self.bfacdate)
        layout.addWidget(self.bsaisfac)
        layout.addWidget(self.bsaisclient)
        layout.addWidget(self.bsite)
        layout.addWidget(self.bsaisprod)
        self.setLayout(layout)

    def initCmd(self):
        self.bprodsite.clicked.connect(self.appui_bprodsite)
        self.bfacdate.clicked.connect(self.appui_bfacdate)        
        self.bsaisfac.clicked.connect(self.appui_bsaisfac)
        self.bsaisclient.clicked.connect(self.appui_bsaisclient)
        self.bsite.clicked.connect(self.appui_bsite)
        self.bsaisprod.clicked.connect(self.appui_bsaisprod)                

    def appui_bprodsite(self):#    	afficher tous les produits ainsi que leurs sites de production
    	self.fen1 = Fen1()
    	self.fen1.show()
    def appui_bfacdate(self):#     	afficher la facture d'un client à une date choisie
    	self.fen2 = Fen2()
    	self.fen2.show()
    def appui_bsaisfac(self):#     	saisir une facture (et de la mémoriser en base)
    	self.fen3 = Fen3()
    	self.fen3.show()
    def appui_bsaisclient(self):#  	saisir un nouveau client
    	self.fen4 = Fen4() 
    	self.fen4.show()
    def appui_bsite(self):#     	afficher tous les sites de productions
    	self.fen5 = Fen5()
    	self.fen5.show()
    def appui_bsaisprod(self):#     saisir un nouveau produit et de le ratacher à un site de production
    	self.fen6 = Fen6()
    	self.fen6.show()


class Fen1(QDialog):# afficher tous les produits ainsi que leurs sites de production
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,140,400,270)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

        self.label = QLabel()
        self.label.setText("Voici la liste des produits ainsi que leurs sites de production :")
        self.label.setAlignment(Qt.AlignCenter)
        self.table = QLabel()
        self.table.setStyleSheet("border: 1px solid #FFCC00; font: 10pt Tahoma; color: #FFCC00")
        self.table.setText(self.affichage1())
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def affichage1(self):
    	dps = self.data.lister_produits_sites()
    	aff1 = "\n"
    	for key, values in dps.items():           
    		aff2 = "\t".join(values)
    		aff1 += " {:<23}\t>:\t{:<25} \n".format(key, aff2)
    	return aff1


class Fen2(QDialog):#     	afficher la facture d'un client à une date choisie
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,50,400,450)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

        self.vide = QLabel()
        self.texte_invit = QLabel()
        self.texte_invit.setText("Choisir un client :")     
        self.texte_invit2 = QLabel()
        self.texte_invit2.setText("Date de facturation (AAAA-MM-JJ) :")
        self.listeclients = QComboBox()
        self.listeclients.addItems(self.data.lister_clients()) 
        self.champ = QLineEdit()
        self.btok = QPushButton("Rechercher")
        self.btok.clicked.connect(self.appui_ok2)
        self.label = QLabel()
        self.label.setStyleSheet("font: 10pt Tahoma; color: #FFCC00")
        
        layout = QVBoxLayout()
        layout.addWidget(self.vide)
        layout.addWidget(self.texte_invit)
        layout.addWidget(self.listeclients)
        layout.addWidget(self.texte_invit2)
        layout.addWidget(self.champ)
        layout.addWidget(self.vide)
        layout.addWidget(self.btok)
        layout.addWidget(self.vide)
        layout.addWidget(self.label)
        layout.addWidget(self.vide)
        self.setLayout(layout)

    def appui_ok2(self):
        date = self.champ.text() 
        client = self.listeclients.currentText()
        client = client.split(", ")
        idclient = client[-1]
        if date :
        	try:
        		achats = self.data.afficher_facture_date(idclient, date)
        		aff1 = " \t{:<23}\t>:\t{:<25} \n".format("Article", "Quantité")
        		for i in achats:
        			aff1 += " \t{:<23}\t>:\t{:<25} \n".format(i[0], i[1])
        		self.label.setText(aff1)
        	except:
        		self.label.setText("Une erreur est survenue. Veuillez vérifier votre connexion au serveur et réessayer.")

class Fen3(QDialog):#     	saisir une facture (et de la mémoriser en base) A TERMINER
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,50,500,450)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

class Fen4(QDialog):#  	saisir un nouveau client
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,50,500,450)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

        self.vide = QLabel()
        self.invit1 = QLabel()
        self.invit1.setText("Choisir le type de client :")        
        self.invit2 = QLabel()
        self.invit2.setText("Nom du client :")
        self.invit3 = QLabel()
        self.invit3.setText("Adresse :")
        self.invit4 = QLabel()
        self.invit4.setText("Ville :")
        self.invit5 = QLabel()
        self.invit5.setText("Pays :")
        self.affect_typecl = QComboBox(self)
        self.affect_typecl.addItems(['Magasin', 'Central d\'achat'])
        self.affect_pays = QComboBox(self)
        self.affect_pays.addItems(self.data.lister_pays())
        self.champ2 = QLineEdit()
        self.champ3 = QLineEdit()
        self.champ4 = QLineEdit()
        self.btok = QPushButton("Entrer dans la base")
        self.btok.resize(100, 30)
        self.btok.clicked.connect(self.appui_ok4)
        self.label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.invit1)
        layout.addWidget(self.affect_typecl)
        layout.addWidget(self.invit2)
        layout.addWidget(self.champ2)
        layout.addWidget(self.invit3)
        layout.addWidget(self.champ3)
        layout.addWidget(self.invit4)
        layout.addWidget(self.champ4)
        layout.addWidget(self.invit5)
        layout.addWidget(self.affect_pays)
        layout.addWidget(self.vide)
        layout.addWidget(self.btok)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def appui_ok4(self):
        typecl = self.affect_typecl.currentText()
        nom = self.champ2.text() 
        rue = self.champ3.text()
        ville = self.champ4.text()
        pays = self.affect_pays.currentText()
        if (bool(nom) & bool(ville)) :
        	try :	
        		self.data.saisir_client(typecl, nom, rue, ville, pays)
        		self.champ2.setText("")
        		self.champ3.setText("")
        		self.champ4.setText("") 
        		self.label.setText("Nouveau client entré en base.")
        	except : 
        		self.label.setText("Une erreur est survenue. Veuillez vérifier votre connexion au serveur et réessayer.")
        else :
        	self.pop = Popup()
        	self.pop.champ_vide_err("'Nom' et 'Ville'")

class Fen5(QDialog):#     	afficher tous les sites de productions
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,150,300,250)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()
        self.label.setText("Voici la liste de nos sites de production :")
        self.label2.setText(self.affichage5())
        self.label.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("border: 4px solid #FFCC00; font: 10pt Tahoma; color: #FFCC00")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        self.setLayout(layout)

    def affichage5(self):
    	ls = self.data.lister_sites()
    	ss = "\n".join(ls)
    	return ss

class Fen6(QDialog):#     saisir un nouveau produit et de le ratacher à un site de production
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("IkeoOoooooo")
        self.setGeometry(500,50,500,450)
        self.setStyleSheet("background-color: #003399; color: #FFFFFF")
        try:
        	self.data = Bdd()
        except mysql.connector.errors.InterfaceError :
        	self.pop = Popup()
        	self.pop.connex_err()

        self.vide = QLabel()
        self.invit0 = QLabel()
        self.invit0.setText("Nom du produit :")        
        self.invit1 = QLabel()
        self.invit1.setText("Référence :") 
        self.invit2 = QLabel()
        self.invit2.setText("Description :")
        self.invit3 = QLabel()
        self.invit3.setText("Statut du produit :")
        self.invit4 = QLabel()
        self.invit4.setText("Site de production :")
        self.affect_statut = QComboBox(self)
        self.affect_statut.addItems(['Commercialisation abandonnée', 'Commercialisé'])
        self.affect_site = QComboBox(self)
        self.affect_site.addItems(self.data.lister_sites())
        self.champ0 = QLineEdit()
        self.champ1 = QLineEdit()
        self.champ2 = QLineEdit()
        self.btok = QPushButton("Entrer dans la base")
        self.btok.resize(100, 30)
        self.btok.clicked.connect(self.appui_ok6)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.invit0)
        layout.addWidget(self.champ0)
        layout.addWidget(self.invit1)
        layout.addWidget(self.champ1)
        layout.addWidget(self.invit2)
        layout.addWidget(self.champ2)
        layout.addWidget(self.invit3)
        layout.addWidget(self.affect_statut)
        layout.addWidget(self.invit4)
        layout.addWidget(self.affect_site)## ajouter possibilité d'affecter plusieurs sites
        layout.addWidget(self.vide)
        layout.addWidget(self.btok)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def appui_ok6(self):
        nompro = self.champ0.text()
        refpro = self.champ1.text()
        descpro = self.champ2.text() 
        if self.affect_statut.currentText() == 'Commercialisé':
        	statpro = 0
        else :
        	statpro = 1
        site1 = self.affect_site.currentText()
        refs_existantes = self.data.lister_references()
        if refpro in refs_existantes :
        	self.pop1 = Popup()
        	self.pop1.ref_exist_err()
        else :
        	if (bool(nompro) & bool(refpro)) : ## faire un if imbriqué pour ref existe déjà ou pas
        		try:
        			self.data.ajout_produit(nompro, refpro, descpro, statpro, site1)
        			self.champ0.setText("")
        			self.champ1.setText("")
        			self.champ2.setText("") 
        			self.label.setText("Nouveau produit entré en base.")
        		except OperationalError : 	
        			self.label.setText("Une erreur est survenue. Vérifiez votre connexion avec le serveur de données.")
        	else :
        		self.pop = Popup()
        		self.pop.champ_vide_err("'Nom' et 'Référence'")


# def main():
# 	app = QApplication.instance() 
# 	if not app:
# 		app = QApplication(sys.argv)
# 	app.setStyle(QStyleFactory.create("Fusion"))

# 	fen = Fenetre()
# 	fen.show()

# 	app.exec_()

# main()

