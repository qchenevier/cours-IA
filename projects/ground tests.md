
### 2019-03-05T11:11:00+01:00

Présents:
- Eugénie MACABOUT (Ai): stream leader du Dynamic Check & Tests (se structure)
- Anouk ANTIBI: QBGGS puis BSE Datalab.
- Quentin CHENEVIER
- Pascal GALIBERT:
  - QBG, qualité cross-programme ground-tests.
  - Responsable du process FUIN-0305, amélioration du processus, fournir méthodes et outils, moyens d'essais.
  - Amélioration majeure du processus: dynamic ground test plan (passer du statique au dynamique pour faire des tests plus fiables et le plus tôt possible).
  - Test très influencés par ce que prescrit le bureau d'étude mais assez peu par ce que voit le client final: pas de customer feedback loop (mis à part rebouclage client par le client).
- Emmanuel ARVEUX (Accenture): projet dynamic ground test plan.
  - Besoin analytics:
    - Jointure NC SAP / Tests ESAO pour identifier les RTI.
    - Construire une data factory cross FAL pour créer un dataset de tests qui créent plein de retests, pour réduire les NC.
    - Réduire aussi les tests inutiles (trouver les retests).

D'ici 2 mois, avoir le dataset qui permet d'objectiver.

Chez QBG:
- Olivier ZENARI: expert ESAO
- Jérôme CANDAT: expert

- Analyse de free text: synergie, se coordonner avec Benjamin ROUSSEL.

- Octobre 2017: hackathon
- Janvier 2018 - Juin 2018: analyse croisée NC et RTI. --> analyse faite par DTO. NC-RTI plus facile à faire que NC-GTI.

Approche transnationale pour le process:
- harmonisation par le .

Sprint 0:

Propale QBG:
-  blue plan SA

Décision:
- Décision: Faire un sprint 0 + sprint 1/2
- PO: QBG (Pascal GALIBERT)
- Dans le stream d'Eugénie sur le control plan.

Key success factors:
- Approche transationale
- Rencontrer les collègues allemands: au moins 2-3 jours à Hambourg (intégrer les éléments de déplacement)

Propale ce soir.

11 mars: sprint 0: 3 semaines: fin 1er avril. 2 sprints: 4 semaines.

Camp de base: ML1.

Budget owner: Bernard MARQUEZ.

Sprint 1 - 2: Avril / Mai.

### 2019-03-07T17:19:19+01:00

Prénom : Réda
Nom : DIHI
Naissance : 24/11/1992
Nationalité : Marocain

### 2019-03-11T10:18:43+01:00

Premier point QBG:

5-10 % des NCs qui ne sont pas liées à des GTI

Dataset allemand: Pas de lien avec les GTI dans la base des NC, obligé de traiter le champ free text de la base de NC pour pouvoir faire le lien.

Parler à Hadi du déplacement à Hambourg qu'on avait pas prévu.

DU: Demande Utilisateur:
GTD/GTP: Ground Test Designer/Performer

Vision: RTI KPI cockpit (sur les différentes stations)
- Utilisateurs: réunion le mercredi matin
  - Qualiticiens: QSL

### 2019-03-19T10:58:04+01:00

weekly au ML1
revue sprint demo #1
revue sprint demo #2

weekly meeting:
- meeting avec O.Zenari (14h-16h) : data exploration

Bien matérialiser la todo list.

- Beaucoup d'attentes sur le digital... reporting au petits oignons à faire.

### 2019-04-09T10:28:36+02:00

Ticket:
- Entre novembre et février

Point avec Reda / messages clés:
- On a bien analysé le besoin: backlog rempli et validé par le client
- On a identifié les données requises et les points durs qui restent à travailler
- A la fin des 2 mois, on aura les fondations de l'applicaton, le dashboard GTI et le dashboard RTI (avec quelques features manquantes)
- Il reste un reliquat du backlog dont la décision de le réaliser ou non est à évaluer en fonction du business case (exercice en cours)

### 2019-04-10T14:42:59+02:00

Sprint 0 review - Ground Tests:
- RTI --> is the priority
- Recurrence & Reason WHY --> P1 at G5, before the fifth of june.
  --> webex from 9 to 10
  -->


Exemple:
- GTI FUEL: 8 26 0165
- magie des jointures ...
- NC: 9052026 --> lien fait par data engineering (70% des données / 30% des données non liables)
- NC Raison: [free text] 24QA en défaut / Ne transmet pas l'information de pression - Fault présent sur P/B LH 1 PUMP / Refus de la 24 QA
- Raison: Pompe Carburant HS --> labellisé à la main par Karim
- Récurrence Raison "Pompe Carburant HS": 2

--> avoir une liste de pain points (Raisons récurrentes de NC sur des RTI) pour pouvoir


### 2019-04-11T09:24:07+02:00

NC related to RTI
NC non-related to RTI --> ?

Reason --> shall give a hint of the root cause -->

GTI dashboard

Implication:
- Patrick

### 2019-04-12T10:14:27+02:00

Sprint 1: semaine 16-17-18-19-20: livraisons weekly le vendredi:
  - 19 avril
  - 26 avril
  - 3 mai
  - 10 mai
  - 17 mai
Sprint 2: semaine 21-22-23-24: fin le 14 juin: livraisons weekly le vendredi:
  - 24 mai
  - 31 mai
  - 7 juin
  - 14 juin

### 2019-04-24T15:18:12+02:00

Newcomer:
- Adeline BORT (BSLOT):
  - End-user Contour

New US:
- Pouvoir filtrer les NC par date de FOT (jointure avec prod à faire)
- BSLAT (--> + TJN + MOB)
- Normaliser les RTI par nombre d'avions
- Séparer les stats Green (structurel - plus stable dans le temps, activité prévisible) vs Cabin (habillage - customization, activité plus imprévisible): investiguer comment rajouter information Green vs Cabin (from ESAO table). **-->** Quelle colonne prendre dans quelle table d'ESAO (Emmanuel prend l'action).


A rajouter dans next steps:
- éléments du backlog:
  - step 0: jointure avec données ESAO / NC
  - ...
- backlog analysis:
  - NLP blah blah


Exemple analyse NC:
- number: 9144485
- defect group: "DAMAGE" --> type d'action générique --> le QUOI haut niveau
- imput def: USSM-25CAB --> poste responsable --> le QUI doit faire pour résoudre quelque chose
- major component description: Cabin -->

Information Zoning

due to --> colonne "liability"
born by --> colonne "station"

### 2019-06-12T10:35:30+02:00

Meeting Ground tests:
- Deliverable 2: NCs covered by GTI: some are covered by RTI, check mail from Patrick.
- Topics:
  - Specific coaching: How to refresh the data --> 1h
    - People: Patrick, Emmanuel, Olivier
  - Sanity check: Workload time
- TODO: Add column of GTI (starting NC ref)
- Deliveries:
  - Closure meeting 10 to 11 AM Monday

Eval MArie:

Delivery --> axe majeur
Behavior --> axe majeur
Consulting skills -->
Content & Innovation
People

### 2019-06-24T16:01:32+02:00

1. RTI:
- Study the cost of adding additional columns from the xls files (est-ce que le code est évolutif de ce point de vue là ?)
- Station (D1ANNC) Poste GTI TLS est un must have selon Karim ==> must have ==> à voir

2. GTI
- GTI OK/NOK: number of overestimation to be analyzed with Patrick ==> must have
- Station (D1ANNC) Poste GTI TLS est un must have selon Karim ==> must have ==> à voir
- Station (D1ANNC) Poste GTI HBG est un must have selon Patrick ==> must have ==> à voir

4. other KPIs
- GTI ref is missing: voir avec Patrick, impact ? ==> must have, mais ça a l'air d'être marginal

5. data refresh: formalized tutorial ==> one shot faisable pour quelqu'un de formé sur la plateforme

TODO:
- évaluer/chiffrer en interne le restant dans la grosseur du trait (tutorial, rajouter les colonnes Station) et donner une date de livraison.
- un point avec Patrick pour évaluer l'ampleur des dégâts sur le KPI GTI OK/NOK.
