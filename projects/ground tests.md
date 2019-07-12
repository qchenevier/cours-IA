
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
