import json
from datetime import date

depenses = []
choix = ""
def sauvegarder_depenses():
    with open("depenses.json", "w") as fichier:
        json.dump(depenses, fichier, indent=4)
def charger_depenses():
    global depenses

    with open("depenses.json", "r") as fichier:
        depenses = json.load(fichier)
def ajouter_depense():
    description = input("Description de la dépense: ").strip()

    while description == "":
        print("Description invalide !")
        description = input("Description de la dépense: ").strip()

    categorie = input("Categorie de la dépense: ").strip()
    while categorie == "":
        print("Categorie invalide !")
        categorie = input("Categorie : ").strip()

    while True:
        try :
            montant = int(input("Montant: "))
            if montant <= 0:
                print("Montant invalide !")
            else:
                break
        except ValueError:
            print("Montant invalide !")


    depense ={
      "description": description,
      "montant": montant,
      "categorie": categorie,
      "date": str(date.today())
    }
    depenses.append(depense)
    sauvegarder_depenses()
    print("Dépense ajoutée !")

def afficher_depense():
    print("\nListe des depenses :")
    if not depenses:
        print("Aucune dépense enrégistrée.")
        return
    print(f"{'N°':<4}{'Description':<15}{'Catégorie':<12}{'Date' :<12}{'Montant':>8}")
    print("-" * 51)
    for i, depense in enumerate(depenses, start=1):
        date_depense = depense.get("date", "-")
        print(f"{i:<4}{depense['description']:<15}{depense['categorie']:<12}{date_depense:<12}{depense['montant']:>8}")


def total_depenses():

    if not depenses:
      print("Aucune depenses enregistrée !")
      return
    total = 0
    for depense in depenses:
      total += depense['montant']

    print(f"\nTotal des depenses : {total}")

def rechercher_depense():
     rechercher = input("Quel dépense veux-tu rechercher ? ")
     trouve = False

     for depense in depenses:
         if rechercher.lower() in depense["description"].lower():
             print("Dépense trouvé !")
             print("description :", depense["description"])
             print("montant :", depense["montant"])
             print("categorie:", depense["categorie"])
             trouve = True
     if trouve == False:
         print("Dépense introuvable !")

def supprimer_depense():
    nom_depense = input("Quel dépenses veux-tu supprimer ? ")
    trouve = False

    for depense in depenses:
     if depense["description"] == nom_depense:
        depenses.remove(depense)
        sauvegarder_depenses()
        print("Depense supprimé !")
        trouve = True
        break
    if trouve == False:
      print("Dépense introuvable !")

def total_par_categorie():
    if not depenses:
        print("Aucune dépense enrégistrée !")
        return
    totaux = {}
    for depense in depenses:
        categorie = depense["categorie"].lower()
        totaux[categorie] = totaux.get(categorie, 0) + depense["montant"]
    print("\nTotal par categories :")
    for categorie, total in totaux.items():
        print(f"{categorie:<12} {total:>8}")

def total_du_mois():
    mois_actuel = str(date.today())[:7]
    total = 0
    for depense in depenses:
        date_depense = depense.get("date", "")
        if date_depense[:7] == mois_actuel:
            total += depense["montant"]
    print(f"\nTotal du mois ({mois_actuel}) : {total}")

def modifier_depense():
    depense_modification = input("Quel dépenses veux-tu modifier ? ")

    for depense in depenses:
        if depense["description"] == depense_modification :
            choix = input("Que veux-tu modiier ? (description/montant/categorie) :")
            if choix == "description":

                nouvelle_description = input("Nouvelle_description :").strip()
                while nouvelle_description == "":
                    print("Nouvelle description invalide !")
                    nouvelle_description = input("Nouvelle description :").strip()
                depense["description"] = nouvelle_description
                print("Description modifiée avec succès !")
                sauvegarder_depenses()


            elif choix == "montant":
                while True:
                    try:
                        nouveau_montant = int(input("Nouveau montant :"))
                        while nouveau_montant == "":
                            print("Nouveau montant invalide !")
                            nouveau_montant = input("Nouveau_montant :").strip()
                        depense["montant"] = nouveau_montant
                        print("nouveau montant modifié avec succès !")
                        sauvegarder_depenses()

                        if nouveau_montant <= 0:
                            print("montant invalide ! ")
                        else:
                            depense["montant"] = nouveau_montant
                            print("Montant modifier avec succès !")
                            break
                    except ValueError:
                        print("Tu dois entrer un montant valide !")

            elif choix == "categorie":
                nouvel_categorie = input("Nouvel-categorie:").strip()
                while nouvel_categorie == "":
                    print("Nouvelle categories invalide !")
                    nouvel_categorie = input("Nouvelle categorie:").strip()
                depense["categorie"] = nouvel_categorie
                print("nouvelle catégorie modifiée avec succès !")
                sauvegarder_depenses()

try:
    charger_depenses()
except FileNotFoundError:
    depenses = []
while choix != "9":
    print("\n---MENU---")
    print("1. Ajouter depense")
    print("2. Afficher depense")
    print("3. Total depense")
    print("4. Rechercher depense")
    print("5. Modifier depense")
    print("6. Supprimer depense")
    print("7. Total par categories")
    print("8. total du mois")
    print("9. Quitter ")

    choix = input("choisis une option: ")
    if choix == "1":
        ajouter_depense()

    elif choix == "2":
           afficher_depense()

    elif choix == "3":
           total_depenses()

    elif choix == "4":
        rechercher_depense()

    elif choix == "5":
        modifier_depense()

    elif choix == "6":
        supprimer_depense()

    elif choix == "7":
        total_par_categorie()

    elif choix == "8":
        total_du_mois()

    elif choix == "9":
            print("Au revoir !")

    else:
            print("choix invalide !")
