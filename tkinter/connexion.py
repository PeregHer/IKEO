import mysql.connector as mysql
from datetime import datetime


class Connexion:

    @classmethod
    def ouvrir_connexion(cls):
        cls.link = mysql.connect(
            user='root', password='root', host='localhost', port="8081", database='ikeo')
        cls.cursor = cls.link.cursor()

    @classmethod
    def fermer_connexion(cls):
        cls.cursor.close()
        cls.link.close()

    @classmethod
    def get_produits(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute(
            "SELECT nom_produit, nom_site FROM produits JOIN produit_site ON produits.id_produit = produit_site .id_produit JOIN sites ON produit_site.id_site = sites.id_site")
        result = cls.cursor.fetchall()
        cls.fermer_connexion()
        produits_site = {}
        for i in result:
            produits_site[i[0]] = []
        for i in produits_site.keys():
            for y in result:
                if i in y:
                    produits_site[i].append(y[1])
        return produits_site

    @classmethod
    def get_facture(cls, client, date):
        client = client.split(', ')
        cls.ouvrir_connexion()
        cls.cursor.execute(
            f"SELECT produits.nom_produit, facture_produit.quantite_produit FROM facture_produit JOIN factures ON facture_produit.id_facture = factures.id_facture JOIN clients ON clients.id_client = factures.id_client JOIN produits ON facture_produit.id_produit = produits.id_produit WHERE clients.nom_client = '{client[0]}' AND clients.ville_client = '{client[1]}' AND factures.date_facture = '{date}'")
        result = cls.cursor.fetchall()
        cls.fermer_connexion()
        return result

    @classmethod
    def get_clients(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute(
            "SELECT nom_client, ville_client from clients ORDER BY nom_client")
        clients = cls.cursor.fetchall()
        cls.fermer_connexion()
        clients = (', '.join(i) for i in clients)
        return clients

    @classmethod
    def get_date_factures(cls, client):
        client = client.split(', ')
        cls.ouvrir_connexion()
        cls.cursor.execute(
            f"SELECT date_facture from factures JOIN clients ON clients.id_client = factures.id_client WHERE nom_client = '{client[0]}' AND ville_client = '{client[1]}'")
        dates = cls.cursor.fetchall()
        cls.fermer_connexion()
        for i, date in enumerate(dates):
            dates[i] = date[0].strftime("%Y-%m-%d")
        return dates

    @classmethod
    def get_pays(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("SELECT nom_pays from pays")
        pays = cls.cursor.fetchall()
        cls.fermer_connexion()
        return pays

    @classmethod
    def get_types(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("SELECT type_client from clients")
        types = set([item[0] for item in cls.cursor.fetchall()])
        cls.fermer_connexion()
        return types

    @classmethod
    def get_sites(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("SELECT nom_site from sites")
        sites = [item[0] for item in cls.cursor.fetchall()]
        cls.fermer_connexion()
        return sites

    @classmethod
    def inserer_clients(cls, *values):
        SQL = f"""INSERT INTO clients (id_client, type_client, nom_client, adresse_client, ville_client, pays_client)  VALUES (NULL, "{values[0]}", "{values[1]}", "{values[2]}", "{values[3]}", (SELECT id_pays from pays WHERE nom_pays = "{values[4]}"))"""
        cls.ouvrir_connexion()
        cls.cursor.execute(SQL)
        cls.link.commit()
        cls.fermer_connexion()

    # saisir factures
    @classmethod
    def lister_factures(cls):
        cls.ouvrir_connexion()
        cls.cursor.execute("Select id_facture from factures ORDER BY id_facture")
        factures = cls.cursor.fetchall()
        cls.fermer_connexion()
        return factures

    @classmethod
    def saisie_facture(cls, date, client, facture, produit, quantite):
        client = client.split(', ')
        cls.ouvrir_connexion()
        cls.cursor.execute(f"INSERT INTO factures VALUES ('{facture}', '{date}', (SELECT id_client from clients WHERE nom_client = '{client[0]}' AND ville_client = '{client[1]}'))")
        cls.cursor.execute(f"INSERT INTO facture_produit VALUES ('{facture}', (SELECT id_produit from produits WHERE nom_produit = '{produit}'), {quantite})")
        cls.link.commit()
        cls.fermer_connexion()