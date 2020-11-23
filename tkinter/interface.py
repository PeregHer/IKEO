import tkinter as tk
from tkinter import ttk
from connexion import Connexion
from functools import partial
import datetime

color_ids = {'Bleu': '#0051BA', 'Jaune': '#FFDA1A'}


class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("IKEO")
        self.master.geometry('1200x600')
        self.master.minsize(900, 600)
        self.master.configure(bg=color_ids['Bleu'])

        label = tk.Label(self.master, font=('Helvetica', '50'),
                         fg=color_ids['Bleu'], bg=color_ids['Jaune'], text="IKEO")
        label.pack(fill='x', side='top')

        self.bottom_frame = tk.Frame(self.master, bg=color_ids['Bleu'])
        self.bottom_frame.pack(side='bottom')

        nom_auteur = tk.Label(self.bottom_frame, font=(
            'Helvetica', '12'), fg=color_ids['Jaune'], bg=color_ids['Bleu'], text="Aude, Jamal, Ludivine, Pereg")
        nom_auteur.pack(side='bottom', ipady=10)

        self.frame_boutons = tk.Frame(self.master, bg=color_ids['Bleu'])
        self.frame_boutons.pack(pady=25)

        self.frame_menu = tk.Frame(self.master, bg=color_ids['Bleu'])
        self.frame_menu.pack()

        fonctions = {'Afficher produits': self.afficher_produits, 'Afficher facture': self.afficher_facture,
                     'Saisir client': self.saisir_client,  'Afficher sites': self.afficher_sites, 'Saisir facture': self.saisir_facture}
        for i, (key, value) in enumerate(fonctions.items()):
            ligne = tk.Button(self.frame_boutons, height=2, width=12, bg=color_ids['Jaune'], bd=0, font=(
                'Helvetica', '12'), text=key, command=value)
            ligne.grid(row=0, column=i, padx=5, ipadx=12)

    def afficher_produits(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        produits_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
        produits_frame.pack()

        produits_site = Connexion.get_produits()

        produit_label = tk.Label(produits_frame, text="Produits", bg=color_ids['Bleu'], font=(
            'Helvetica', '20', 'underline'))
        sites_label = tk.Label(produits_frame, text="Sites", bg=color_ids['Bleu'], font=(
            'Helvetica', '20', 'underline'))

        produit_label.grid(row=0, column=0, padx=50)
        sites_label.grid(row=0, column=1, padx=50)

        for i, (key, value) in enumerate(produits_site.items(), 1):
            produit = tk.Label(produits_frame, text=key,
                               bg=color_ids['Bleu'], font=('Helvetica', '12'))
            produit.grid(row=i, column=0)

            sites = tk.Label(produits_frame, text=value,
                             bg=color_ids['Bleu'], font=('Helvetica', '12'))
            sites.grid(row=i, column=1)

    def afficher_facture(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        def remplir_entree_date(self):
            dates = Connexion.get_date_factures(entree_client.get())
            if len(dates) > 0:
                entree_date.set('Choisir une date')
            else:
                entree_date.set('Aucune factures')
            entree_date.configure(values=dates)

        def afficher():
            for widget in facture_frame.winfo_children():
                widget.grid_forget()

            result = Connexion.get_facture(
                entree_client.get(), entree_date.get())

            produit_label = tk.Label(facture_frame, text="Produits", bg=color_ids['Bleu'], font=(
                'Helvetica', '20', 'underline'))
            sites_label = tk.Label(facture_frame, text="Quantités", bg=color_ids['Bleu'], font=(
                'Helvetica', '20', 'underline'))
            produit_label.grid(row=0, column=0, padx=50)
            sites_label.grid(row=0, column=1, padx=50)

            for i, values in enumerate(result, 1):
                produit_label = tk.Label(facture_frame, font=(
                    'Helvetica', '13'), bg=color_ids['Bleu'], text=values[0])
                produit_label.grid(row=i, column=0)

                quantite_label = tk.Label(facture_frame, font=(
                    'Helvetica', '13'), bg=color_ids['Bleu'], text=values[1])
                quantite_label.grid(row=i, column=1)

        entrees_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
        entrees_frame.pack()

        facture_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
        facture_frame.pack()

        entree_client = ttk.Combobox(entrees_frame, width=50, values=list(
            Connexion.get_clients()), state="readonly")
        entree_client.set('Chosir un client')
        entree_client.bind('<<ComboboxSelected>>', remplir_entree_date)
        entree_client.grid(row=0, column=0, padx=20, pady=30)

        entree_date = ttk.Combobox(entrees_frame, state="readonly")
        entree_date.grid(row=0, column=1, padx=20, pady=30)

        boutton_factures = tk.Button(entrees_frame, height=2, width=13, bg=color_ids['Jaune'], bd=0, font=(
            'Helvetica', '11'), text="Afficher", command=afficher)
        boutton_factures.grid(row=0, column=2, padx=20, pady=30)

    def saisir_client(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        display_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
        display_frame.pack()

        def inserer():
            Connexion.inserer_clients(type_liste.get(), entree_nom.get(
            ), entree_adresse.get(), entree_ville.get(), pays_liste.get())
            self.saisir_client()

        for i, text in enumerate(['Nom', 'Type', 'Adresse', 'Ville', 'Pays']):
            label = tk.Label(display_frame, text=text, bg=color_ids['Bleu'], font=(
                'Helvetica', '12', 'underline'))
            label.grid(row=0, column=i)

        entree_nom = tk.Entry(display_frame, bg='white',
                              width=20, justify='center', font=('', '9'))
        entree_nom.grid(row=1, column=0, padx=10, pady=15)

        type_liste = ttk.Combobox(display_frame, width=20, values=list(
            Connexion.get_types()), state="readonly")
        type_liste.set('Chosir un type')
        type_liste.grid(row=1, column=1, padx=10, pady=15)

        entree_adresse = tk.Entry(
            display_frame, bg='white', width=20, justify='center', font=('', '9'))
        entree_adresse.grid(row=1, column=2, padx=10, pady=15)

        entree_ville = tk.Entry(display_frame, bg='white',
                                width=20, justify='center', font=('', '9'))
        entree_ville.grid(row=1, column=3, padx=10, pady=15)

        pays_liste = ttk.Combobox(display_frame, width=20, values=list(
            Connexion.get_pays()), state="readonly")
        pays_liste.set('Chosir un pays')
        pays_liste.grid(row=1, column=4, padx=10, pady=15)

        but_saisir_client = tk.Button(display_frame, height=2, width=13, bg=color_ids['Jaune'], bd=0, font=(
            'Helvetica', '11'), text="Saisir", command=inserer)
        but_saisir_client.grid(row=2, columnspan=5, padx=20, pady=10)

    def afficher_sites(self):
        for widget in self.frame_menu.winfo_children():
            widget.pack_forget()

        sites_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
        sites_frame.pack()

        sites = Connexion.get_sites()

        sites_label = tk.Label(sites_frame, text="Sites", bg=color_ids['Bleu'], font=(
            'Helvetica', '20', 'underline'))
        sites_label.grid(row=0, column=1, padx=50)

        for i, value in enumerate(sites, 1):
            label = tk.Label(sites_frame, text=value,
                             bg=color_ids['Bleu'], font=('Helvetica', '12'))
            label.grid(row=i, column=1)

    def saisir_facture(self):
            for widget in self.frame_menu.winfo_children():
                widget.pack_forget()        
            
            def valider():
                #date du jour                
                Connexion.saisie_facture(self.entree_date.get(), self.entree_client.get(), self.entree_facture.get(), self.entree_produit.get(), self.entree_quantite.get())
                        
            self.entrees_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
            self.entrees_frame.pack()

            self.facture_frame = tk.Frame(self.frame_menu, bg=color_ids['Bleu'])
            self.facture_frame.pack()

            self.entree_facture = ttk.Combobox(self.entrees_frame, values=list(Connexion.lister_factures()), state="normal")
            self.entree_facture.grid(row = 0 , column = 0, padx=20, pady=30)

            self.entree_client = ttk.Combobox(self.entrees_frame, values=list(Connexion.get_clients()), state="readonly")
            self.entree_client.grid(row = 0 , column = 1, padx=20, pady=30)

            self.entree_produit = ttk.Combobox(self.entrees_frame, values=list(Connexion.get_produits()), state="readonly")
            self.entree_produit.grid(row = 0 , column = 2, padx=20, pady=30)

            self.entree_quantite = tk.Entry(self.entrees_frame, bg='white', width=20, justify='center', font=('Helvetica', '10'))
            self.entree_quantite.grid(row = 0 , column = 3, padx=20, pady=30)
            
            self.entree_date = tk.Entry(self.entrees_frame, bg='white', width=20, justify='center', font=('Helvetica', '10'))
            self.entree_date.grid(row = 0 , column = 4, padx=20, pady=30)
            self.now = datetime.date.today() 
            self.date_facture = self.now.strftime("%Y-%m-%d")
            self.entree_date.insert(0, self.date_facture)

            self.boutton_factures = tk.Button(self.entrees_frame, height=2, width=13, bg=color_ids['Jaune'], bd=0, font=('Helvetica', '11'), text="Valider", command=valider)
            self.boutton_factures.grid(row = 0 , column = 5, padx=20, pady=30)