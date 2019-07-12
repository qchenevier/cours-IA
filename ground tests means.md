
### 2018-10-16T17:45:45+02:00

Point avec QSW:

Au service de:
- éxecuteurs d'essai en concevant / produisant des moyens de tests soft / hard
- maintenance des moyens de tests

Wiring Test Data Analysis:
- Logs texte au format propriétaire qui ont été analysés et
- Client: Maintenance de l'outillage. Clustering des tests similaires / Anticipation des tests KO (soit classif soit clustering)

GTI (Ground Test Instruction) defects:
- un peu similaire

Data extract analysis:
- quels sont les pages / données qui sont le plus utilisées sur le portail data extract

C/B usage:
- voir quels sont les CBS (C/B simulator) les plus utilisés à travers les logs.
- équipement CBS coûteux, donc objectif d'anticiper tâche de maintenance / identifier les CBS qui ne sont plus utilisés

Prédiction de la prochaine panne d'outillage:
- avis de panness d'outillage tracés sous SAP PGI
- maintenance prédictive des outillages, mieux anticiper le parc outillage (les spares) pour la montée en cadence

Tools vs Aircraft vs GTI:
- troubleshooting

### 2018-11-27T16:52:09+01:00

Point avec QBGGS:

Utilisateurs:
- Mainteneurs des moyens d'essais
- Utilisateurs des moyens d'essais

GTI: Ground Test Instruction
- Entre 300 et 600 GTI par avion
- 2 jours de tests par avion
- si panne d'quipement de test ==> retard

RTI: Repeat Test Instruction
- Test supplémentaires, dûes au manip' avion

ESAO: Essais au Sol Assistés au Sol
A/C: aircraft
WO: Work Order
PN: Part Number (l'identification d'un type d'équipement)
SN: Serial Number (l'identification d'un équipement particulier: il y a plusieurs SN pour un PN)
CBS: Circuit Breaker Simulator (pas nécessaire sur A320)

Evènements funestes qu'on peut éviter:
- GTI ralenti par un TroubleShooting
- RTI suite à GTI interrompu parce que test KO

En théorie, un test GTI devrait passer nominalement, mais les tests lèvent des NCs qui n'ont pas été vues avant. Un but intéressant est de pouvoir compter les defects qui sont "levés" au moment des tests.

Tests: 2 grandes phases:
- Cablage puis Power-ON
- Systèmes (au fur et à mesure)

Utilisation de l'analytics:
- Optimisation du parc outillage (doit-on dupliquer un outil pour supporter le ramp-up ?)
- Compréhension d'un panne d'un outillage et faire une corrélation avec éventuellement un contexte

Beaucoup d'interactions à prévoir avec QBGGM (Maintenance essais au Sol)

QBGGS: ESAO Software
QBGGW: Ground Test Tools
QBGGM: Maintenance
QBGGXX: 2 autres équipes

Sur toulouse:
- 100-130 M€ d'équipements de tests
- 7 à 10 % de frais de maintenance (Idéalement, en vrai c'est beaucoup moins)

### 2018-12-03T11:10:33+01:00

Nouvelle personne:

Olivier BOIZEAU:
- augmentation des
- digitalisation ==> blockchain

US1:
- transactions SAP
- beaucoup de champs free text: besoin de faire du text mining
- relié au cas US4

US2: visualisation exploration

US3:

US4: machine learning: classifier en trois domaines (ou alors prendre le problème dans l'autre sens (features importances analysis))

U5 records: données de maintenance

Problématique: on est souvent mis en défaut : "c'est votre outil". Besoin de trouver la root cause.
Capitaliser pour redistribuer du savoir

Extractions de données:
- ME ticket ==> extraction de données

Projet d'optimisation de l'ingestion ==> en contact.

début week 3 - 13/12: feedback (interne) vers autres chefs d'équipe pour définr orientation et choix des use-cases pour 2019

Présentation :
- envoyer les templates de livrables pour pouvoir se projeter.
- donner les logins à Olivier pour partage des données.

### 2018-12-18T10:10:09+01:00

Point avec Olivier:
- investigation quel maintenance préventive est réellement:

50 GTD (3 x 15 pour les 3 FALs + 5 pour la FAL A380)
500 GTP

waste ==> only A320 ==> avoir A350

UC1:
- croiser les NCs / defects avec le nombre d'interruptions pour savoir si les interruptions sont dûs à l'avion ou au GTI: (utiliser la référence de l'outillage, la date, le poste)
- rajouter le temps moyen d'interruption (qu'on a calculé)
- besoin de mettre en place un suivi de l'impact des corrections des GTI

UC2:
- faire apparaître quel est la quantité du parc
- enveloppe maintenance: 2.5 M€ au global ==> 10 % au global
    - 60 % corrective / 40 % préventive
- taux horaire ==> 60 €/h
- code CSEM: retour magasin pour panne

UC4:
- reboucler avec utilisateurs finaux: MAP A320 / Control Plan.

UC5:
- valeur du parc: 150 M€ trop élevé ==> 100 M€

UC6:
- poste technique: 3ME ronde

- à partir de 2018: plus de description, uniquement un code.

Prévoir session feedback au début

TODO:
- UC1: refaire l'analyse pour l'A350 (voir l'A330 ?)
- dire aux garçons que s'ils viennent, ils doivent prendre des notes.
- faire des plots pour montrer les volumes: maintenance préventive, maintenanve corrective (dûe à préventive ou en opération)
- Chaque use-case: Faire apparaître coût de l'effort (enveloppe pour chaque use-case)
-

### 2018-12-19T15:25:55+01:00

Tests means exploitation:
- AVL, AVL2
- ARP
- ERP

    Faire le point avec le manuf, AET, process optimizer
    Plutôt géré par le manuf:

Natco coordination:
- Moins de traçabilité autre part qu'en France

Measurement drifts:

Next step:
- pas trop GTP
- GTI
- MSN ==> NC

==> use-case: quand il y a un incident, à qui on l'attribue ?

- 400 avions / an

Les 3 streams de valeurs:
- data additionnelle

- troubleshooting des erreurs

- optimisation parc outillage en prenant en compte le planning avion:
    - ...
    - voir performance des outils d'essai

==> suite

Olivier:
- continuer: data cleaning, exploration & engineering, en local
- focus sur la maintenance
- construire la vision à plus long-terme avec QBG (Anne)

Stéphane:
- continuer à extraire: beaucoup données métier dans SAP PGI, mais pas dans leur outil ESAO:
    - data owner: SAP Qualité: Guillaume POIRIER pour les données qualités
    - data owner: Jig & tools: Manuf: Contact ?

TODO:
- regarder données AVL dans skywise
- reboucler avec Quentin Amirault pour connaître les données ingérées dans Skywise, éventuellement les noms es data officers
