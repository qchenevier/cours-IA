
### 2018-11-19T14:38:27+01:00


Pedro Munoz
Maria Martinez de la casa
Paul Molitor

Quentin Chenevier
Nancy Varuco
Hadi Mahihenni
Charlotte Pierron-Perles


- starting with PEG
- 13 Agreements signed, 5 flagships
- Not all suppliers: Top 70 %
- 2 teams of Palantir (big delivery)
- start with engine & structure suppliers

- on top of the main Ontology defined by Palantir, what can we do more ?

E.g.: Dashboard Rolls-Royce:
- backed by Hubble.
- focus on data integration ==> not all data in it.
- reporting ==>

Skywise for suppliers:
- API for data ingestion on PC-SPC: has to be integrated into the legal framework of Skywise for suppliers.


POP: forecasting tool
- engine delivery model hosted on iShare (excel)
- integration in Skywise ?
- montecarlo analysis tool to evaluate scenarios

Control towers (several of them):
- in excel

3 phases:
- Reporting
- Analysis
- Forecasting

Related topics:
- PO analytics department, being created soon
- Skywise for procurement = Awareness of Skywise to procurement guys

Product Owner:
- Paul is the focal point but not the product owner
- Sensible

DTO: fund
- Launch something this year
- Not until january
- PO Engines

Other use-case: conformity: coutour report

Next steps:

Complexity:
- Not the volume
- Not the algorithms
- The main challenge is Data Quality & Consistency ==> data is there but it might

UX/UI is important / New ways of working / Operational people under lot of pressure

### 2018-12-19T14:04:45+01:00

Réunion Skywise for suppliers avec Pedro, Maria:

- Mathieu Landman: DTO: Equipments & Systems suppliers:
    - Equipment in Supply Chain
    - in Service issues
- Pedro Munoz
- Maria Martinez De la casa:
    - Propulsion
    - Cabin
- Antoine Morin:
    - System architect: Maintenance operations
    - Talent tool industrialisation
- James Snow
- Antoine Bouillet:
    - Chief Engineering
    - "Automatic fishbone" ==> project of automatic correlations
- Guillaume Bersac: Zero-AOG (former colleague of Quentin)
- Estelle Pimouguet: Head of Health Analytics in Zero AOG: data analytics

- Nancy Varuco
- Quentin Chenevier
- Charlotte Pierron-Perles
- Hadi Mahihenni

Blocking point:
- early adopter agreements
- ...
- work with third parties ==>

Transition phase: scale-up
- platform for problem solving (we are not very good at project mode)

RFP process to engage with Cap ?
- global agreement on ABD contract
- discussion wit Jean-Luc Vincent-Franc on future relationship with next steps
- RFP internal process ==> test the partner at small scale: get to know how it works

Initial areas of activities:

- Production datasets anonymisation:
    - 1 month: target end of january
    - already a model running
    - put in production in Skywise: in data ingestion ?

- Shared area with suppliers: Fault centric approach: build an ecosystem of developers to contribute:
    - Cannot share "attributable" data with suppliers: remove MSN, remove time
    - 4 streams:
        CONF:
        OPERATION:
        LRU: link between TSM
        SENSOR: CCE (Common Conditions Explorer: app from Palantir)
    - Key aspect: architecture, existing tools

- Bricks from Zero-AOG: ???

- Support cabin suppliers:
    - P3: integration of cabin suppliers
    - no use case defined
    - link with PC-SPC way of working
    - light support:
        - no support on data analytics ==> suppliers are good at it. (is this sure ?)
        - support on data engineering

- Operational tool structures (James Snow):
    - working for 1 supplier, next will be "Premium Aerotech"
    - run by palantir (inluding helpdesk)
    - could consider using a 3rd party to help scaling up: on-boarding more suppliers
    - not industrialize

TODO:
- Program a meeting to assess feasability of datasets anonymization ==> Mathieu Landman
- Meet Quentin Amirault ==> anonymisation doit être faite dans COP / Data ingestion ?
- Program an Architecture workshop for 2nd stream: beginning of january.
- Meeting on the contract ==> 8th of january

==> Analyse the need and get back with a set of proposals

### 2019-01-07T10:19:34+01:00

Point Skywise for Suppliers / SkySup:

UC1: anonymisation TLB
- propale à shooter ==> lead Florent
- reboucler avec Christophe REGOUBY ==> lead Benjamin, Valentin

UC2: fault-centric approach
- propale à maturer ==> lead Anouk, support Alexandre, Bruno
- reboucler avec Mathieu LANDMAN: qui est le PO ? ==> lead Hadi

UC3: supplier analytics
- reboucler avec Maria MARTINEZ sur besoin ==> lead Hadi, Alexandre

UC4: reprise outil dispatch de Palantir
- reboucler avec James SNOW sur besoin ==> lead Hadi, Bruno
- demander accès outil pour analyse ==> lead Hadi, Bruno

### 2019-01-08T16:36:41+01:00

Point Skysup avec:
- Guillaume POIRIER
- Benjamin ROUSSEL
- Pascal FOUILLANT
- Mathieu LANDMAN

- Florent MARTY
- Benjamin FARCY
- Valentin VIVANT
- Quentin CHENEVIER

Performance qui étaient mauvaises dès qu'on changeait les sources de NC: 400 sources différentes.

Perfo: 96 % au global (tous champs confondus)

1000 NC

### Wed Feb 13 12:08:30 CET 2019

Réunion avec Pedro sur opportunities for Skywise for suppliers:
- Pedro Munoz:
- Stephane Gucker:
- Mathieu Landmann: sfs, partie équipements & systèmes

- Charlotte
- Hadi
- Quentin

Pedro a vu Philippe DE REBOUL, Bruno DE VILOUTREY.

Vision: ressources, skills, croissance

Mathieu:
- Equipement passeport:
  - bâtir un passeport de l'équipement, depuis chez le fournisseur, jusqu'à sa vie en service
  - travaux avec Palantir sur ce sujet
  - passage à l'échelle sur les différents fournisseurs, handover vers mai
  - trouver un partenaire pour bâtir des features en vertical (Qualité, Supply chain):
    - A/C operability
    - fleet performance
  - travail avec Liebherr pour bâtir cette approche verticale: traçabilité, control tower

- Root cause analysis:
  - étude statistiques pour faire root cause analysis: trouver les drivers.
  - sur périmètre Airbus & aussi fournisseurs
  - volonté de partage des données fournisseurs, si on clair sur le "purpose"
  - Qualité supply chain --> c'est OK
  - Qualité in service --> c'est fermé, ouvrable selon les use-cases, à définir avec la data gouvernance

- Reliability monitoring: 1er service: calcul des taux de fiabilité d'un équipement en service.
  - représente une collecte de données manuelle important pour le fournisseur
  - EYY a déjà commencé à faire des choses

- Problématiques de data engineering:
  - anonymisation des données in-service pour pouvoir les remonter aux fournisseurs
  - gestion des accès aux données (à la colonne)

- Training des populations Airbus qui ne sont pas habituées Skywise: POS, POE, fournisseurs
  - example: PC-SPC
  - example: training des ressources cap Skywise
  - Jamie Snow: a un sujet de training des équipes PO
  - qqn de cap bosse sur POY avec le bundle PO: reboucler avec Claire DUFORT
  - ??? veut créer un département qui fait des analytics pour PO
  - "On a travaillé pendant X mois, sur des use-cases sur Thales, mais personne chez Airbus n'est capable de gérer ces sujets."
  - besoin de training, en commençant par une awareness
  - définir un workpackage de formation
  - notre besoin pour faire une propale:
    - le nombre de personnes à former
    - où elles se trouvent
    - les objectifs de formation: prise en main: Skywise lvl 1/2 (voir les niveaux de training de Palantir)

- REX du use-case avec Thales:
  - faire une RCA sur un problème récurrent sur un équipement
  - fait par Palantir sans upskiller leurs contacts airbus
  - difficulté pour aller plus loin en croisant plus de données
  - approche trop fermée

- Use-case avec Liebherr :
  - qui est le PO ? on a besoin de temps du métier

- In service:
  - sur la partie in service: sur le plateau zero AOG, un airbus
  - l'engineering ont un TTGF de 12 mois: ils n'attendent pas Skywise pour résoudre leurs problèmes
  - quel timeframe ?
    - Palantir a commencé sur la partie data foundation
    - Il faut embrayer avec un dispositif:
      - en 1 mois 1/2 / 2 mois, on peut faire quelque chose pour les 1er use-case.
      - 3/4 sprints de 2 semaines
      - localisation: idéalement Copernic.
      - Greg, Mathieu, Vincent + dispositif
    - NB: le formateur sera volant: Toulouse, Hambourg

Stéphane:
- Product Owner de l'outil Dispatch développé par Palantir, en train de faire une V2 (livrée entre avril et juin)
- la v1 est basée sur le use-case Rolls-Royce
- la v2 devra évoluer, idéalement pour prendre en compte les autres fournisseurs, y compris la cabine.
- produit trop sur mesure pour l'outil
- beaucoup de dette technique: difficile de changer le nom d'une pièce.
- handover: quelle date ?
- objectifs:
  - prendre en main: quels sont les objets clé, quels sont les pipelines
  - faire une critique constructive
  - être capable de faire quelques évolutions mineures
- nécessite une compréhension de la supply chain --> intégrer des consultants fonctionnels
- nouvelle feature à développer: sujet typique: comment réallouer une pièce dans son plan de production (faire un swap), ça fout le bordel dans le suivi de la configuration
  - il y a l'outil CARE chez Airbus pour assurer le suivi (chaque pièce a un CARE), mais pas chez le fournisseur
- court-terme: rentrer dans la v2, pour préparer le handover

Commencer par les besoins de Mathieu, laisser Stéphane pour faire.

Notre contact procurement: Lucie Chambrier.

TODO:
- shooter une propale pour fin de semaine
- analyser l'extrait de RFP envoyé par Mathieu
- shooter qq slides sur le training: les niveaux, le contenu

Point sur les ressources:
- forecast: on peut faire +40 personnes cette année, sur sfs
- on a les ressources indiennes
- croissance des ressources nécessaire pas avant mai-juin --> commencer petit mais avec des gens afutés

- profil:
  - Grégoire Risoti: fort sur le métier --> donc light sur l'aspect fonctionnel
  - scoping

### 2019-02-13T18:20:55+01:00

Point avec Charlotte, Hadi:

Skywise for suppliers - Fault Centric Approach:
- Dispositif:
    - 1 scrum expert qui supervise: Eloi JABET (non facturé)
    - 1 scrum expert: Alexandre TEIXEIRA
    - 1 DS: Valentin VIVANT
    - 1 DE: Hachem AFIFI
    - 0.5 expertise métier: Hadi MAHIHENNI & Quentin CHENEVIER
- Propale:
    - 4 sprints de 2 semaines
    - études statistiques pour faire première root cause analysis
    - mise en place du equipment passport

Skywise for suppliers - Training:
- Dispositif:
    - 0.5 senior DS: Benjamin FARCY
    - 0.5 scrum: Eloi JABET & Quentin CHENEVIER
- Propale:
    - montrer les supports existants

Structure de coût trop chère pour le début: voici c'est un

Reynald --> pas vendu sur PCT, faudrait le vendre.

### 2019-02-15T14:10:39+01:00

Point Sfs avec Alexandre TEIXEIRA et Grégoire RIZZOTTI.

Predictive maintenance:
- hors scope

Equipment passport:
- différence de vision entre fournisseurs et airbus sur la fiabilité intrinsèque.
- Airbus a une vue partielle sur la vie de l'équipement (ex: les résultats de tests qui ont été faits au moment de la dépose de l'équipement).
- Compléter cette vue avec les données in service
- Joindre les forces entre Airbus et les suppliers pour avoir une vue la plus complète possible + éventuellement les MRO

In-service report:
- fait partie de la root cause analysis

Root cause analysis:
- utilisation d'algo
- plusieurs degrés: MISP, RFW, XTRA
- step 1: scoping: scoper le problème: analyse de fréquence (quelle compagnie est la plus touchée, quel équipement, quelle route) --> automatic report
- step 2: fault driver: joindre avec des données vivantes --> deep dive & filter, trouver les patterns récurrents. source: opération, configuration, LRU, sensor.
- step 3a: test condition: écrire les tests requirements nécessaires automatiquement
- step 3b: anonymized time-series: anaonymiser les time-series in-service pour pouvoir les stocker et les exploiter plus tard. Pour pouvoir donner la possibilité à Airbus et Liebherr de travailler ensemble.

Filter: Fault --> Aircraft --> Period --> Part Number --> ...

Other topic:
- Discuter avec les utilisateurs finaux.
- Cas de figure qui dure depuis des années --> arriver à troubleshooter ce problème.

A la grosse, se focaliser sur l'auto report, puis voir la suite.

Compétences nécessaires: Gestion de base de données, connaissance de l'environnement Foundry.

ACMS: Aircraft Condition Management System
EAP: Early Adopter Phase

### 2019-03-04T10:02:21+01:00

Airbus:
- Mathieu LANDMAN (ZO): sponsor du projet
- Grégoire RIZZOTTI (SDG): point focal Liebherr
  - faire attention à ce qu'on échange avec le fournisseur --> on apprend toujours
  - liste de contacts à

Capgemini:
- Alexandre TEIXEIRA (scrum / PPO)
- Eloi JABET ()
- Benjamin FARCY
- Patrick KAMNANG

Convergence sur un outil de root cause analysis --> talon

Consolider use-cases:
Palantir: ontologie - data foundation

Valeur:
- Design Office Airbus: orienter le bureau d'étude pour trouver plus rapidement
- Supplier: aider à faire des tests pertinents, avoir accès aux signaux pour faire RCA
  - TTGF MISP: 12 mois
    - récupérer l'info: 3 mois --> à réduire
    - voir le reste --> à mapper

Process MISP:
- fleet board (SEE) fait une revue d'un évènement pour présenter au program board (SB) qui décide de lancer un MISP --> démarrage du t0 pour le MISP.
- fleet board manque d'analyse / de données, implique peu le fournisseur --> besoin de

Qualification --> Root cause analysis --> Développement d'une solution --> Développement d'un kit de retrofit

2 types de responsabilité pour un fournisseur:
- fournisseur d'un équipement: spec équipement
- fournisseur d'un macro-équipement (plus sur A350): spec d'intégration, le fournisseur fait une pré-intégration de plusieurs équipements. Le fournisseur a besoin d'avoir des données sur un spectre plus large pour pouvoir faire soi-même l'analyse. En
↗ besoin data pour un RSP

déploiement solutions:
- direct fit
- retro fit: déploiement avec un Service Bulletin --> cloture du MISP

Focus sur le rapport automatisé (en 2 mois): sous la forme de widgets (modules):
--> à base de Foundry Contour Report avec filtres sur le côté
- Features:
  - (level 0) Tronc commun de chaque rapport: stat de flotte, ...
  - (level 1) Widgets prédéfinis ajoutés manuellement
  - (level 2) Widgets préféfinis suggérés parce qu'on a trouvé des corrélations
- End users:
  - SEE
  - Fournisseur

Données:
- ISAIM: outil Airbus des Airlines des données de dépose, mais tout ne passe pas par Airbus !
- Données fournisseurs (sources identifiées)

⚠️ obstacle data management: donnée attribuable à une A/L --> pas partageable avec le fournisseur --> anonymisation. Règles établies avec la data gouv: checklist en cours d'anonymisation.

Story line:
- scoping (filtrage des évènements pertinents et des sensors):
  - faults pertinentes
  - A/C program
  - A/C configuration (P/N, supplier, ...)
  - operations (age, ...)
  - time period
- clustering des routes / évènements --> la manière de faire les clusters est super structurante

Ex: peinture qui a des bulles d'air près de la connectique, bulles qui gonflent en altitude

Stakeholders / Product Owners:
- EY: Denis BELMONTE
- Benjamin VINCENT

Enjeu: harmoniser les applis:
- Talon (Estelle Pimouguet / Guillaume Bersac)
- Common cause analysis (projet Grégoire RIZZOTTI)
- RCA (projet Qualité)

TODO:
- workshops avec appli Talon, MISP investigator.
- partager la liste des ATA
- meeting SRS pour connaitre le contenu de leurs données

Glossaire:
- NFF: No Fault Found
- MISP: Major In Service Problem
- RFW: Request For Work (rebaptisé CISP)

### 2019-03-07T09:48:50+01:00

DSM Skywise for suppliers:
- faire le point avec Benjamin et Patrick sur contenu fonctionnel des données
- faire la demande d'accès au données pour moi
- revoir la présentation

### 2019-03-12T08:56:26+01:00

Skywise for suppliers:
- m'impliquer sur le BCase de Skywise for supplierss
- choisir avec Ben et Patrick ce qu'on over-deliver en data science

### 2019-03-12T17:00:00+01:00

Quels datasets:
- Données publiques
  - METAR
  - Flight: basée sur FR24: analyse de Mehdi:
      - missing data --> quelles colonnes
      - incoherent data --> retard sur la mise à jour des données --> Quel retard ?
- AC Flight hours Flight cycles:
  - missing data: seulement 200 avions
- Event All Status / Validated: OI - Operational Interruption
  - All Status: en attente de traitement
  - Validated: table filtrée
  - Point de contact: Louis MELLIORAT sur DME
- CMS reports / faults / etc:
  - Point de contact: Quentin CHENEVIER
- Removals:
  - data from airlines: qualité hétérogène à évaluer
  - a comparer / jointer aux events

TODO: initier le rapport contour
