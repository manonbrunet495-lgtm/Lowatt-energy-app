#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:15:49 2026

@author: manonbrunet
"""

# conseils.py

def donner_conseil(anomalie, questionnaire):

    # Tout va bien
    if anomalie == "NORMAL":
        return "✅ Votre consommation est normale. Continuez comme ça !"

    # Il est probablement en vacances
    if anomalie == "CONSO_ANORMALEMENT_BASSE":
        return "🏖️ Vous consommez très peu. Êtes-vous absent ?"

    # Alerte légère
    if anomalie == "ALERTE_LEGERE":
        return "📊 Consommation un peu au dessus de la normale. Gardez un œil dessus."

    # Alerte forte → là on personnalise selon son profil
    if anomalie == "ALERTE_FORTE":

        if questionnaire["chauffage_electrique"]:
            return "🔥 Votre chauffage électrique consomme beaucoup. Essayez de baisser le thermostat d'1 ou 2 degrés."

        if questionnaire["chauffe_eau"]:
            return "💧 Programmez votre chauffe-eau la nuit, pendant les heures creuses."

        if questionnaire["seche_linge"]:
            return "👕 Utilisez votre sèche-linge la nuit, c'est moins cher et plus écolo."

        if questionnaire["presence"] == "forte":
            return "🏠 Vous êtes beaucoup à la maison. Pensez à éteindre les appareils en veille."

        # Si aucun équipement particulier → conseil générique
        return "⚠️ Votre consommation est anormalement élevée. Vérifiez vos appareils."