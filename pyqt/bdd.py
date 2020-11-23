import mysql.connector


class Bdd:
	def __init__(self):
		self.bdd = mysql.connector.connect(user ='root', 
            password='root', host='localhost', 
            database='ikeo', port='8081')
		self.curs = self.bdd.cursor()

	def lister_pays(self):
		self.curs.execute("SELECT nom_pays FROM pays")
		lp = []
		for pays in self.curs :
		    lp.append(pays[0])
		return lp

	def lister_references(self):
		self.curs.execute("SELECT id_produit FROM produits")
		lr = []
		for ref in self.curs :
		    lr.append(ref[0])
		return lr	

	def lister_clients(self):#     				afficher tous les sites de productions
		self.curs.execute("SELECT nom_client, adresse_client, ville_client, id_client FROM clients")
		ls =[]
		for client in self.curs :
			client = ", ".join(str(client[i]) for i in range(len(client)))
			ls.append(client)
		return ls

	def lister_produits_sites(self):#    		afficher tous les produits ainsi que leurs sites de production
		self.curs.execute("SELECT nom_produit, nom_site FROM produits JOIN produit_site ON produits.id_produit = produit_site .id_produit JOIN sites ON produit_site.id_site = sites.id_site;")
		result = self.curs.fetchall()
		dps = {}
		for ligne in result :
			dps[ligne[0]] = []
		for prod in dps.keys() :
			for ligne in result :
				if prod in ligne :
					dps[prod].append(ligne[1])
		return dps

	def afficher_facture_date(self, id_client, date):#    afficher la facture d'un client à une date choisie
		val = (id_client, date)
		query = ("SELECT produits.nom_produit, facture_produit.quantite_produit FROM facture_produit \
			JOIN factures ON facture_produit.id_facture = factures.id_facture \
			JOIN clients ON clients.id_client = factures.id_client \
			JOIN produits ON facture_produit.id_produit = produits.id_produit \
			WHERE clients.id_client = %s AND factures.date_facture = %s")
		self.curs.execute(query, val)
		result = self.curs.fetchall()
		return result

	def saisir_facture(self):# 					saisir une facture (et de la mémoriser en base)
		pass

	def saisir_client(self, typecl, nom, rue, ville, pays):#  		saisir un nouveau client
		val = (typecl, nom, rue, ville, pays)
		query = "INSERT INTO clients (id_client, type_client, nom_client, adresse_client, ville_client, pays_client) VALUES (NULL, %s, %s, %s, %s,(SELECT id_pays FROM pays WHERE nom_pays = %s));"
		self.curs.execute(query, val)
		self.bdd.commit()

	def lister_sites(self):#     				afficher tous les sites de productions
		self.curs.execute("SELECT nom_site FROM sites")
		ls =[]
		for site in self.curs :
			ls.append(site[0])
		return ls

	def ajout_produit(self, nompro, refpro, descpro, statpro, nomsite): #    saisir un nouveau produit et de le ratacher à un site de production
		val1 = (refpro, nompro, descpro, statpro)
		query1 = "INSERT INTO produits (id_produit, nom_produit, desc_produit, statut_produit) VALUES (%s, %s, %s, %s);"
		self.curs.execute(query1, val1)
		val2 = (refpro, nomsite)
		query2 = "INSERT INTO produit_site (id_produit, id_site) VALUES (%s, (SELECT id_site FROM sites WHERE nom_site = %s));"
		self.curs.execute(query2, val2)
		self.bdd.commit()
