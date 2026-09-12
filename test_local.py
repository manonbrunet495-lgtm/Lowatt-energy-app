"""
test_local.py — Pour tester le backend sans frontend ni Postman.
Lance simplement : python test_local.py
"""

from profils import calculer_seuil
from alertes import detecter_anomalie
from conseils import donner_conseil

# --- Jeux de test ---
cas_de_test = [
    {
        "label": "Famille en surconsommation (chauffage électrique)",
        "questionnaire": {
            "surface": "80_120m2",
            "occupants": "3-4",
            "chauffage_electrique": True,
            "chauffe_eau": True,
            "climatisation": False,
            "seche_linge": True,
            "presence": "forte",
            "objectif": "reduire_facture",
        },
        "conso_reelle": 35.0,
    },
    {
        "label": "Étudiant seul, petit appart, tout va bien",
        "questionnaire": {
            "surface": "moins_30m2",
            "occupants": 1,
            "chauffage_electrique": False,
            "chauffe_eau": False,
            "climatisation": False,
            "seche_linge": False,
            "presence": "faible",
            "objectif": "ecologie",
        },
        "conso_reelle": 4.2,
    },
    {
        "label": "Couple absent (vacances ?)",
        "questionnaire": {
            "surface": "30_50m2",
            "occupants": 2,
            "chauffage_electrique": True,
            "chauffe_eau": False,
            "climatisation": False,
            "seche_linge": False,
            "presence": "faible",
            "objectif": "simple_suivi",
        },
        "conso_reelle": 1.5,
    },
]

# --- Lancement des tests ---
print("=" * 55)
for cas in cas_de_test:
    q = cas["questionnaire"]
    conso = cas["conso_reelle"]

    seuil    = calculer_seuil(q)
    anomalie = detecter_anomalie(conso, seuil)
    conseil  = donner_conseil(anomalie, q)
    score    = round(conso / seuil, 2)

    print(f"\n🧪 {cas['label']}")
    print(f"   Seuil calculé   : {seuil} kWh")
    print(f"   Conso réelle    : {conso} kWh")
    print(f"   Score           : {score}  ({'🔴' if score > 1.1 else '🟢'})")
    print(f"   Anomalie        : {anomalie}")
    print(f"   Conseil         : {conseil}")
    print("-" * 55)
