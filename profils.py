#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:11:50 2026

@author: manonbrunet
"""

# profils.py

POINTS_DE_DEPART = {
    "moins_30m2": {1: 5.0,  2: 6.5,  "3-4": 8.0,  "5+": 10.0},
    "30_50m2":    {1: 7.0,  2: 8.5,  "3-4": 10.0, "5+": 12.0},
    "80_120m2":   {1: 10.0, 2: 12.0, "3-4": 15.0, "5+": 18.0},
    "plus_120m2": {1: 14.0, 2: 17.0, "3-4": 21.0, "5+": 25.0},
}

def calculer_seuil(questionnaire):
    
    # Point de départ
    seuil = POINTS_DE_DEPART[questionnaire["surface"]][questionnaire["occupants"]]

    # Équipements
    if questionnaire["chauffage_electrique"]: seuil *= 1.4
    if questionnaire["chauffe_eau"]:          seuil *= 1.2
    if questionnaire["climatisation"]:        seuil *= 1.15
    if questionnaire["seche_linge"]:          seuil *= 1.1

    # Habitudes
    if questionnaire["presence"] == "forte":  seuil *= 1.15
    if questionnaire["presence"] == "faible": seuil *= 0.9

    # Objectif
    if questionnaire["objectif"] == "ecologie":        seuil *= 0.85
    if questionnaire["objectif"] == "reduire_facture": seuil *= 0.90

    return round(seuil, 1) 

