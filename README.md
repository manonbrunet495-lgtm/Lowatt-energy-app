# Lowatt-energy-app
Python/Flask backend for LOWATT — an AI-assisted home energy management app. Computes personalized consumption thresholds from user profiles, detects consumption anomalies, and generates tailored energy-saving advice.

My contribution
This repository contains the module I was responsible for within the team:

profils.py — computes a personalized consumption threshold for a household based on a user questionnaire (surface area, number of occupants, appliances, presence patterns, goals).

alertes.py — compares actual consumption against the computed threshold and flags anomalies (over-consumption, unexpected low consumption, etc.).

conseils.py — generates tailored energy-saving advice based on the detected anomaly and the household's profile.

main.py — Flask server exposing the above logic as an API, designed to connect to the team's web front-end.
test_local.py — standalone script to test the backend logic with sample households, without needing the front-end or a tool like Postman.

How to run the test: test_local.py
This runs three sample scenarios (a high-consumption family, a low-consumption student, and an absent household) and prints the computed threshold, detected anomaly, and generated advice for each.
