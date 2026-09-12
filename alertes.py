#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:15:31 2026

@author: manonbrunet
"""

# alertes.py

def detecter_anomalie(conso_reelle, seuil):

    if conso_reelle > seuil * 1.3:    # dépasse le seuil de plus de 30%
        return "ALERTE_FORTE"

    elif conso_reelle > seuil * 1.1:  # dépasse le seuil de 10 à 30%
        return "ALERTE_LEGERE"

    elif conso_reelle < seuil * 0.5:  # consomme deux fois moins que d'habitude
        return "CONSO_ANORMALEMENT_BASSE"  # peut-être qu'il est en vacances ?

    else:
        return "NORMAL"