
### 2018-06-07T09:56:21+02:00

Réunion avec Katherine Ribere:

Pour les utilisateurs:
- Pb: TechRequest donne pas les bonnes infos

Rencontrer Vincent Cherière & Eloi Chabaut

Match: codage des QLB
Aller voir match.

RCA.

Conditions:
- Capacité à développer avec Maxence
- Roadmap sur les focus et la variation de la composition de l'équipe.

### 2018-06-11T09:14:18+02:00

Scope A330/A380 ==> à commonaliser avec le scope A350 RCA.

Jérémy Brousseau: problem solving. RCA modules programmatiques ==> il doit partir en mode produit.

Plateau dédié qualité.

Scoping:
- QSR: Pas la priorité
- Concessions: Oui ==> contenu connu sous SAP


Yann Foster (Airbus)

### 2018-07-03T15:01:09+02:00

Phone call avec Benjamin Roussel:
- je te remercie de nous faire confiance
- je ne sais pas encore si c'est possible d'avoir des ressources pour ce workshop: de quel type ?
- quelle rôle vois-tu pour nous lors de ce workshop ?
- comment pouvons-nous contractualiser ? eric ne veut pas qu'on travaille plus que quelques heures gratuitemnt ?
- si contractualisation, quels types de livrables ? instruction des sujets ?

(Phone call pas fait)

### 2018-07-04T11:09:59+02:00

Propales

DART:
Sprint 0:
- de base, marge à 62 %: 36405€
- option Proxy PO (1 senior consultant - Amira): 48531€ (+12106€)
- option UX designer (0.5 backelite + 1 app level B - 321): 62506€ (+13975€)

4 sprints delivery:
- de base, marge à 62 %: 206601€
- option Proxy PO (1 senior consultant - Amira): 279576€ (+72975€)
- option UI developper (1.5 app level B - 321): 333722€ (+54146€)

Qcentral:
Work unit: 2 jours * 2 consultants (Quentin & Benjamin)
- 11221€

### 2018-10-09T16:34:35+02:00

Point avec Hadi: priorisation des leads

- DART sprint 1 ... N (Qualité): sprint 0 fait / on hold because archi
    - pas de data science
    - intéressant mais difficile parce qu'on doit hybrider avec SAP

- FAL Warning Extended (Qualité): lead avec apps / préliminaire
    - monitoring des échanges de données entre les différents systèmes du manuf pour éviter des pb de désynchro
    - utiliser Skywise pour faire du "contrôle qualité" de ces échanges.

- PCSPC Broughton: propale shootée (500k€)
    - 2 use-cases avec l'équipe Quantum locale: preventive maintenance sur le tooling et la HSDM (High Speed Drilling Machine)
    - propale shootée cet été mais pas de réponse depuis
- PCSPC Hamburg: lead
    - idée sur la 4ème ligne A320: aller identifier des use-cases sur le drilling avec CI Germany
    - Dans PC-SPC ou en-dehors
- PCSPC Saint-Eloi: suite d'une presta déjà effectuée
    - predictive maintenance sur outils coupants

- XBOM DDMS: propale shootée (option à 70k€)
    - utiliser les BOMs pour standardiser les product lines.

- ??? QK Qualité programme: rencontre avec QK
    - pitcher PCSPC et la data science pour la qualité

- Toulouse-Metropole VILAGIL: lead
    - plateforme mobility as a service

- Reflights: lead
    - sujets proposé sur PCT: data science pour prévenir les reflights (gros BCase)

- Audit automation: lead
    - voir mail d'Eric

### 2018-10-30T15:48:41+01:00

PC-SPC: call avec Hadi et Ali: Propales

Quality Control Tower:
- PO: Bnejamin Roussel
- Besoin: sprint 0

Tindoor:
- Besoin: coordination / assistance technique avec les fournisseurs

Ground test means:
- Besoin: sprint 0 + PoC

### 2018-10-31T15:58:08+01:00

Point avec Hadi. Qui appeler pour staffer ?

Ressources managers:
- Sogeti Hight Tech: Khaoutar Krichen (Maman de Marwan)
- Capgemini Apps: Charlotte Labeuse
- Staffeuse Skywise: Nathalie Vinas

### 2018-11-12T14:16:12+01:00

PC-SPC: team retrospective #1

Orlando:
- 2 points weekly par plant
- échos des plants:
    - Stade ça se passe pas bien: Point dur entre connectivité ZILO ... data ingestion. Problème d'un investissement du PO pour faire avancer les sujets.
    - Nouvelle architecture pour l'ingestion de data machine ==> COP écrit directement des fichiers parquet au bon format dans S3 (au lieu d'utiliser Magritte).
    - Orlando tient plutôt le Rôle de Thierry Semelle sur cette boîte au lettre vers la data ingestion ?
- API supplier:
    - en cours: faire un kit d'accès en python pour pouvoir faire la requête POST avec les bons certificats.
- SMS / mail alerting:
    - Outil en dehors de la Foundry qui se branche sur les datasets Foundry, qui permait de faire une alerte mail ou SMS
    - 1er use-case
- Run mode:
    - 3 briques à mettre en place: machine jusqu'à ingestion, backend foundry, frontend foundry
    - activer le run mode pour les 3 briques: "oui le run mode existe bien mais nous n'avons pas encore d'application en run"
    - nécessité d'avoir une application performante, mature, auditée avec un KT
    - KT: spec, best practices, documentation...

Cedric:
- Onboardé le 24 octobre, puis formé sur Mulesoft (pour API supplier et SMS Alerting)
- Mismatch entre la version de Mulesoft et la version implémentée ==> aller près de l'API squad ?
- Se former à Foundry pour préparer le support

Marie:
- Déploiement la toolbox pour la Pre-FAL Hambourg pour l'A350. Pas possible pour le Single Aisle (en pre-FAL H245), parce que pas de données.
- Bug fixing ==> en cours
- Semaine Pro: Déployer la toolbox à SNZ pour le SA et l'A350 (SPC Vision et MAA).

Marwan:
- Broughton: bug fixing, nouveau format des datasets après correction avec la data ingestion (timestamp qui sont convertis en string...)
- Toujours des bugs qui subsistent: dûs à la data ingestion ==> pas traité avant 3 semaines.
- Single Aisle en déploiement, mais un bug sur les données ==> Russ se préoccupe davantage de l'A350, donc ça va, mais il faut quand même s'en préoccuper.
- Mise en place d'un dashboard qui permet de visualiser tout le workflow. Besoin spécifique qu'on a choisi d'implémenter à part de la toolbox.
- Accompagnement d'une ressource locale ==> good ! Mais il bosse pour l'équipe Quantum. Philippe doit avoir son mot à dire, vu qu'on forme un gars mais pas pour PC-SPC.

Imane:
- Lancer les ingestions de données pour la FAL Hambourg.
- Pour la pre-FAL, il y a quelques données dans SPC vision. Beaucoup d'échanges de mails, mais pas de réponses.
- Station 40/41:
-

Hadi:
- ramp-up: enjeu stratégique pour la boîte, mais en fait on n'a plus bossé sur l'A350.
- Use-cases ramp-up:
    - door rigging
    - H245
    - station 40-41
- Remarque Orlando: "single-aisle ramp-up" est un token d'invincibilité pour pouvoir faire passer sa demande d'ingestion en premier. Il faut trouver la team qui "certifie" les use-cases ramp-up.
- Comment pousser du conseil pour mieux aborder les use-cases ?
- Propales en cours:
    - Audit
    - Support
    - Door rigging

Ali:
- Hambourg: bien partager l'info avec Imane
- SNZ: avec l'équipe centrale, déployer la toolbox
- Getafe: en framing, mais ils ont pas de budget...
- Puerto Real: en framing
- Scrum of Scrum:
    - Tous les sujets en cours / besoins sont renseignés dans un fichier
    - Toutes les 2 semaines
- Capability Library:
    - Vision de quand elle sera déployée. A construire dans la roadmap de sprints.

Quentin:
- Audit:
    - enjeu pour le plateau et pour Cap
    - Philippe veut un audit plutôt vertical
- Propales: staffing à trouver
- QBGGS
- Communication à propos des requêtes

Actions:
- Imane partager l'info sur les données Hambourg avec Ali
- Hadi faire meeting Station 40 next wave
- Ali retravailler la roadmap de sprints pour rajouter la ligne "PC-SPC central"
- Quentin faire meeting pour s'assurer de la cohérence des implémentations des pipelines d'intégration
- Quentin faire passer les bonnes pratiques
- Quentin met en place une mailing-list
- Hadi / Ali de décider quel est le Knowledge repository et quel est la date pour faire un repas d'équipe

Semaine prochaine:
- MC: Marie
- Prez:
    - Imane: Corrélations Station 40
    - Marwan: sur le sujet Orbital measures

### 2018-10-31T15:58:08+01:00

Point avec Hadi. Qui appeler pour staffer ?

Besoins staffing:
- Quality Control Tower: début 26 novembre ==> sur à 90 %
    - 1 consultant fonctionnel (Scrum Master / Proxy-PO)
    - 1 tech lead (ou dev expérimenté)

- QBGGS: début décembre ==> sur à 50 %
    - 1 consultant fonctionnel (Scrum Master / Proxy-PO)
    - 1 data scientist

- DME:
    - 1 data scientist (DME ==> OK)

Ressources managers:
- Staffeuse Skywise: Nathalie Vinas
- Capgemini Apps: Charlotte Labeuse
- Sogeti High Tech: Khaoutar Krichen (Maman de Marwan)
- Staffeuse OT ==> ?

### 2018-12-10T14:10:42+01:00

- Finir l'industrialisation de la toolbox
- Mieux détecter de nouveaux use-case de data science
- Agilité: optimisation de la formation

Cette semaine pour Hadi:
- Quality Control Tower
- Propale Q1
- Structuration support

- Faire un feedback à Orlando sur les audits.

- Demander à Marwan quel nouveau cas de test il met en place pour résoudre le bug

### 2019-01-07T14:14:47+01:00

PC-SPC:

Hadi:
- mettre Bernard RIBERE dans la boucle à partir de maintenant:
    - Profil moins digital que Philippe mais beaucoup d'expérience Manufacturing.
    - Un peu old school: beaucoup de pédagogie, mais un grand savoir fonctionnel.
    - A travaillé sur le projet "NC in Takt"
- Cedric quitte le projet, Mathieu reprend ses activités: support technique & architecture.
- PC-SPC Toolbox ==> shifter vers un "run mode" ==> on-boarder Mathieu.
- Marwan va quitter le dispositif: travail de capitalisation & transmission.

Orlando:
- Point avec Bernard RIBERE et Philippe MIRALLES
- Défi: Mise en place du run:
    - supporter l'existant
    - soulager l'équipe centrale
- Supplier API qui commence à être déployée avec les cas pilotes.
    - pousser les brique technique au prochain PI planning (3ème semaine de janvier)
- Skywise Academy (par Annabelle Gérard): Certification payante.

Imane: Station 40
- Nouveau dashboard pour voir les mesures orbitales et les rails pour que Saint-Nazaire et Nantes puissent voir les mesures avant la FAL.
- Propale BSE (Single-Aisle Chief Engineering): besoin de data science / dashboarding
    - équipe à staffer: 3 personnes (1 Consultant / 1 DS / 1 DE)
    - garder une seule équipe: soudée avec le reste de PC-SPC.
- Déplacement à Hambourg

Marie:
- Déploiement Capability Library: analyse du bug: impact & root cause ==> avant de déployer.
- Test sur Getafe: OK
- Guide utilisateur à créer avec Ali.
- Sprint à venir: Getafe & Puerto Real.

Ali:
- Capacity library: sprint industrialisation prévu.
- Backlog à revoir.
- Assessment en cours: réunion mardi.

Marwan:
- "J'ai été au brésil et j'ai kiffé"
- Déploiement de la toolbox avec Saint-Nazaire
    - Tous les programmes déployés
    - Réticence du Single-Aisle (difficile à on-boarder)
- Plan de travail à définir:
    - Capability Library

Quentin:
-

TODO:
- déménagement à organiser pour PC-SPC
- on-boarder Mathieu sur Foundry
- on-boarder Mathieu sur la toolbox
- analyser support Skywise Academy d'Annabelle Gerard
- réunion: besoin fiabilité & industrialisation algorithme Capability Library. Lister tâches.

### 2019-01-07T17:04:42+01:00

Point avec Imane - Station 40:

Trouver des tronçons similaires entre SNZ / HAM et au cours du temps:
- K-nearest neighbors avec distance L1 et distance L2. Si besoin customizer la distance.
- PCA pour trouver les patterns de déformation fréquents (voir la distribution des valeurs propres): 1 PCA sur SNZ, 1 PCA sur HAM, 1 PCA sur la diff.
- A voir mais plus tard: anomaly detection

### 2019-01-18T14:45:56+01:00

réunions:
- mardi / mercredi matin: station 40
- mercredi après-midi / jeudi: station 41

1 fois par mois à Hambourg

objectif du projet:
- réduire l'extra lead time sur les FAL HAM et TLS pour le programme SA

- revoir le tolerancement sur les 2 stations 40/41
- liste de pain points à corriger

station 40: jonction center wing box - ailes
station 41: jonction fuselages

livrables génériques:
- data engineering pour la capability:
    - génération des datasets avec les capabilités calculées
    - dashboard pour visualiser (dashboard spécifique).
- root causes analysis pour les pain points
    - exploratory data analysis
    - début de modélisation

virtual assembly software

use-case modélisation: réunion à prévoir

livrables engagés pour la semaine prochaine:
- réunion mardi sur un problème constaté côté Nantes
- nouveau dashboard côté volume
- modèle prédictif: orbital measurement / rails

méthode de travail:
- weekly 30 minutes: revue de l'avancement du backlog
- si contenu: réunion fixée dans agenda commun pour revue résultats (1 heure)
- point fixés au fil de l'eau, mais pas de sprints (pas de sanctuarisation d'un backlog).

- 2 nouveaux membre à 50 %: data scientist Airbus, qui va travailler sur le workpackage "data analytics" leadé par Imane: besoin de l'alimenter.

Chaimaa - Station 17 BSE:

Phase sprint 0:
- data collection
- définition des user stories (sur les NC dans les nacelles)
- backlog priorisé, pas très clarifié, pas prêt techniquement

next step:
- lundi matin: précision du backlog: estimation workload / capacité.
- key success factors: avoir les bons filtres ==> chaimaa

### 2019-01-21T14:11:26+01:00

Point PC-SPC retrospective:

Quentin: poser des points pour le suivi des activités
- Imane: feedback vers Bernard + contact Caroline CHABRE - 30 min
- Marie: knowledge transfer + feedback vers Bernard - 1 h
- Chaimaa: début activités - 1h

Marie:
- sprint puerto real: capacity library + déployer dashboard Semaphore
- avec Ali - suivi des plants pour le déploiement:
    - 2 sites problématiques: FAL TLS et EYY ==> pas de réponse

Imane: station 40/41
- Steering vendredi dernier
- Démo de l'outil des mesures orbitales ==> suite au problème d'assemblage de certains avions ==> capitalisation à faire. ==> à capitaliser ?
- A Hambourg pour la semaine d'après.
- Se maille avec Chaimaa pour lui donner du support

Ali:
- sur tout 2019: faire attention aux impacts migration excel ==> google suite
- capability library: fiabilité qui peut être améliorée. impact à évaluer la semaine prochaine
- présentation jeudi à Bernard.
- définir roadmap future pour
    - mise à niveau qualité code
    - run mode
    ==> intégrer absolument Orlando pour ce point: roadmap
- use-case machine learning: Hambourg

Chaimaa / Anouk: station 17
- dataset pas propre (colonnes mal remplies)
- aucune user story lancée pour l'instant parce que pas accès aux données
- dataset "NC_SA_QMP" global des NC (3 millions de lignes) ==> filtrer sur l component "nacelle".

TODO Quentin:
- mettre la main sur Hadi pour alignement avec Ali mardi matin
- poser points à Imane / Chaimaa / Marie

### 2019-01-22T09:13:05+01:00

3 axes:
- IOT / real time
- Single Aisle ramp up
- Toolbox Run mode

Toolbox run mode:
- continuer scrum of scrum pour garder communication inter-sites / bonne pratiques
- ...

SA ramp-up:
- workshop ideation
- concours d'idées
- s'inspirer du backlog
- proposer intégration avec autres équipes: station 40/41 / BSE

IOT / real time / smart manufacturing
- nantes: smart manufacturing: Nantes / Stade
- intégration avec équipes VP IOT DTO (high level) / Connectivity /

Court-terme:
- finir industrialization

### 2019-01-28T14:09:03+01:00

PC-SPC retrospective:
- présentation: nouveau process demandes ingestion

Orlando:
- demandes ingestion: backlog fixé pour le PI mais il y a quand même de la marge.
- Saint-Eloi: peu satisfait à propos du planning prévu pour leurs ingestions
- problématique inclusion équipe ZIL dans la gestion des ingestion requests: PC-SPC
- discussion autour de notre rôle

Kevin Lanioux:
- AOSIS
- Master MAPI3
- Stage avec Christophe REGOUBY
- Raphaël Smith a démissionné
- Mis en place du support:
    - Support L2 / L3:
    - Livraison des nouvelles features

Hadi MAHIHENNI:
- Première rencontre avec Bernard RIBERE
- Définition d'une roadmap à long-terme
- Workshop avec utilisateurs pour définir une roadmap, du futurs use-cases

Ali DIAB:
- Point avec Hugo Cascarigny pour faire un "Best practices assessment".
- Orlando: liste des assets déjà faite.
- évolution Toolbox:
    - Travail en chambre risqué pour l'adoption, mais pas simple de bosser avec les plants pour faire ces évolutions, tout en respectant les bonnes pratiques
    - Voir ce que Benjamin ROUSSEL veut faire pour embarquer: QMP: rôle d'animateur de la communauté.
- Toolbox: prochain déploiement: Bremen
- Puerto Real: revoir avec Orlando le ticket de Puerto Real
- Hambourg: ...
- Capability Library:
    - Instruction du backlog à faire pour des évols
    - Saint-Eloi qui pousse pour faire les évols rapidement.

Marie VACHELARD: Take away Jetafe/Puerto Real :
- Importance d'impliquer de onboarder Data Scientists des Plants
- Possible de déployer en 1 semaine la Toolbox mais grâce à prépa en amont avec Orlando --> Single Minute Exchange (SMED)
- Data Scientist Guide est assez complet

Anouk ANTIBI:
- Identifier les données sources, fonctionnellement.
- Recherche des données, c'est difficile:
    - essayer d'utiliser Data Explorer
    - Data Product (pas encore déployé) ==> pour remplacer les "data catalogs".
        - renseigner quoi, qui, comment ?
- Pour répondre à Nuno: faire une demo des outils actuels sur Foundry

Imane BEN-ELMAMOUN:
- à Hambourg...

Chaimaa BABAY:
- Rassurée sur le dashboarding
- En cours: faire le data mapping avec le métier
- Routines Agile en cours.

Quentin CHENEVIER:
- Début de travaux conjoints BSE/Station 40/41 ==> positif, à continuer.
- Vigilance sur l'Agile et comment le présenter à nos clients: il faut de la marge pour gérer le risque.
- Vision sur la toolbox à terminer ==> prévoir un point avec Ali/Marie pour clarifier un reste à faire à Bernard et les plants

TODO:
- Point RASCI ingestion: rôles entre plant. Mardi 15h30.
- Point Vision + Backlog toolbox.
- Se coordoner avec Mathieu IZORE pour les data qualité.

### 2019-01-28T16:03:31+01:00

Point avec Hadi: revue du Funnel

Forecaster le CA: impossible
Forecaster les coûts: possible

Ressouces:
- XBOM: 7.5 FTE vendu
    - Bruno / Florent / Nicolas / Aurélien (50%)
    - Mehdi / Tarek / Hachem / Pierre
- PC-SPC: 7.6 FTE vendu / 1.4 FTE bizdev
    - Ali / Marie / Hadi (30%) / Quentin (30%)
    - Orlando / Kevin
    - Anouk / Imane / Chaimaa
- RCA/DIVA: 0 FTE vendu / 1.5 FTE bizdev
    - Alexis / David (50%)
- QWT: 0 FTE vendu / 2 FTE bizdev / 1 FTE potentiel
    - Alexandre / Sacha / Celia
- SFS: 0 FTE vendus / 1 FTE bizdev / 0.5 FTE potentiels
    - Valentin / Benjamin (50%)
- Unified NC: 2.5 FTE potentiels
- Quality Data Product: 2 FTE vendu / 2 FTE potentiels
- QBGG: 0 FTE / 2.25 FTE potentiels

FTE Quality & Industrial au 28/01/18:
    - vendu: 17.1 FTE
    - bizdev: 5.9 FTE
    - potentiel: 8.25 FTE
==> actionner sur le BD pour mieux vendre

TODO cette semaine:
- gestion FTE & bizdev court-terme:
    - demander à Elodie comment Benjamin est facturé
    - propale PC-SPC avant fin semaine ==> Ali
    - propale XBOM avant fin semaine ==> Florent / Bruno
    - propale RCA/DIVA ==> Mathieu
    - propale Unified NC ==> Alexandre
    - propale QBGG ==> Anouk / Valentin / Quentin
    - formation simu financière avec fichier followup ==> Hadi
- bizdev long-terme:
    - NLP for information extraction: proposer un point à Benjamin Roussel sur NLP avec NC ==> QC
    - QWT: appeler Benjamin Roussel en fin de semaine ==> Hadi
    - IOT: pousser un rapport à Anes HODZIC ==> Hadi
    - SFS: appeler James Snow ==> Hadi
    - SFS: appeler Mathieu Landman sur WP2 "data centric approach" ==> Hadi

### 2019-01-29T09:39:59+01:00

Point PC-SPC avec Chaimaa:

futur:
- data explo: comprendre la donnée:
    - trouver la bonne personne & savoir poser la bonne question
- data engineering:
    - refaire un dataset auquel on n'a pas accès

==> Point avec Anouk et Chaimaa sur la gestion du risque Agile
==> finir article de blog sur le risque agile
==> voir avec anouk: aller à une sprint demo

==> tester accès au path contour Orlando

passé:
- "j'ai eu peur d'être vendue comme un front-end expérimenté"

### 2019-02-04T13:48:47+01:00

Point avec Imane:
- Virtual assembly tool: sécuriser un consultant pendant 1 semaine pour le déploiement de l'outil.
    - value assessment à faire pour prouver la valeur
    - capitalisation
    - presta à titre gracieux
- Support chaimaa: Front-end.
    - passer voir BSE pour rassurer le client.

### 2019-02-04T14:04:27+01:00

Point PC-SPC:

Marie: industrialisation de la toolbox
- partager la vision avec les plants et avec @Orlando
- construire la todolist la toolbox
- point capability library, avec Guillaume, Luis et Rémi:
    - integration OK ? bugs ?
    - integration banc de test ? ==> sujet important à aborder.
- point avec Marwan: bug sur dashboard orbital measurements.
- hackathon Invent supaero: récupérer un stagiaire.

Imane: analyse one-shot: problème assemblage Nantes (station 40)
- analyse présentée demain ==> à partager pour feedback
- travailler avec les ressources Airbus: intégration d'une nouvelle ressource ZI
- action chez Hadi pour trouver un consultant fonctionnel pour faire une business analysis: demander à Pierre Gabet / Anthony Gros

Orlando:
- event sur ingestion:
    - nouveau process d'ingestion avec value assessment WSJF
    - vision sur le backlog
- support incident ingestion à résoudre:
    - 34 flux machine sur 37 qui sont cassés: P0
    - testing à faire
- Qualité des builds:
    - monitoring: splunk
    - action à pousser vers l'équipe data product
- API supplier:
    - delai à prévoir à cause des autres tâches
    - pb d'architecture, actions lancées: pour traiter un souci.
- SMS / e-mail alerting:
    - implémenter

Hadi:
- l'équipe doit prendre du temps avec Estelle pour l'audit technique, mardi après-midi

TODO:
- @Marie & @Quentin: faire un point pour définir la todolist de l'indus toolbox
- @Imane: partager les slides pour feedback
- @Imane: présenter lors du prochain point un des sujets
- @Marie: trouver les gens de l'équipe qui ne sont pas sur le slack
- @Orlando: parler avec Bernard, faire mail de pédagogie vers Bernard sur les sujets chauds (ingestion).
- @Marie: prendre du temps avec Estelle pour l'assessment technique.

### 2019-02-05T09:44:43+01:00

Point avec Hadi:

TODO semaine dernière:
- gestion FTE & bizdev court-terme:
    - ✔️ demander à Elodie comment Benjamin est facturé
    - ✔️ propale PC-SPC avant fin semaine ==> Ali
    - ✔️ propale XBOM avant fin semaine ==> Florent / Bruno
    - ✔️ propale RCA/DIVA ==> Mathieu
    - ✔️ propale Unified NC ==> Alexandre
    - propale QBGG ==> Anouk / Valentin / Quentin
    - formation simu financière avec fichier followup ==> Hadi
- bizdev long-terme:
    - ✔️ NLP for information extraction: proposer un point à Benjamin Roussel sur NLP avec NC ==> QC
    - ✔️ QWT: appeler Benjamin Roussel en fin de semaine ==> Hadi
    - IOT: pousser un rapport à Anes HODZIC ==> Hadi
    - SFS: appeler James Snow ==> Hadi
    - SFS: appeler Mathieu Landman sur WP2 "data centric approach" ==> Hadi

TODO cette semaine:

TODO semaine dernière:
- gestion FTE & bizdev court-terme:
    - propale QBGG simu financière ==> Quentin
    - formation simu financière avec fichier followup ==> Quentin
    - pitcher propale data product ==> Quentin, Valentin & Hadi
- bizdev long-terme:
    - IOT: pousser un rapport à Anes HODZIC ==> Hadi
    - SFS: appeler James Snow ==> Hadi
    - SFS: appeler Mathieu Landman sur WP2 "data centric approach" ==> Hadi

### 2019-02-18T09:48:27+01:00

Point avec Hadi:

Short-term:
- SFS:
    - DS: Arthur + Benjamin ou autre senior
    - DE: Hachem ? (attention vendu jusqu'à mi-mars)
- Unified NC: Valentin + Patrick ou Benjamin

- Discuter avec Benjamin + Reynald pour voir le sujet du staffing de Benjamin
- Appeler Reynald: Est-ce qu'on peut pas faire plus simple et décharger Benjamin ?

Long-term:
- QBGGS: shooter propale en disant qu'on ne peut pas et voir si on peut gagner du temps
- QWT: Benjamin ROUSSEL à rappeler
- Industrial ramp-up: pitch à préparer avec Charlotte
- DDMS:

### 2019-02-18T15:04:54+01:00

Point PC-SPC:

Hadi:
- data factory: aller les rencontrer (Patrick FERNANDEZ CANAL)

Marie: toolbox industrialisation
- backlog chiffré pour l'industrialisation --> objectif de la semaine
- résolution bugs getafe
- mise en place d'un backlog commun avec orlando et kevin

Imane: st40/41
- passage de Philippe MIRALLES sur le plateau station 40/41: il a essayé de vendre le projet Unified NC
- livraison d'une documentation sur les données
- monthly data science analysis station 40, partager l'info
- meeting jeudi avec end-users du virtual assessement tool: à montrer en interne aussi: meeting à 17h30 le mardi
- semaine 9: à Hambourg
- semaine 12: à Nantes
- semaine 13: à Hambourg

Anouk: BSE
- sidenote: slide qui décrit les différents
- sprint 2: mardi semaine prochaine (W9)
- mise en place contacts pour electronic passport: récupérer données planning, NC
- NC_SA_QMP: dataset plus disponible. Travaux sur un extract.
- client au fait d'un sprint 3 industrialisation
- faire un one-pager pour exprimer le besoin de données à Philippe, qui fera pression sur l'équipe de Guillaume POIRIER (Quality Data Product). Reboucler avant tout avec Hadi et les collègues de cette équipe
- 1er in-flow board (demand management) semaine dernière: pas mal de têtes présentes --> possible de rencontrer des gens chez BSE
- début framing sur BSE cockpit: dashboard avec tous les KPIs de BSE

Chaimaa:
- première démo du dashboard ce matin: graphe avec les défauts
- 3 datasets
  - NC: travail sur dump pour l'instant
  - OOT: explo en cours
  - planning: dataset OK, prêt
- points bloquants:
  - données Hambourg pas encore disponible: sera géré pendant l'industrialisation
  - information section: a gérer demain avec Sorina
- travailler avec un contour pendant la réunion

Quentin:
- meetings coaching P2P data science

Ali:
- audit high-level: plus que l'audit technique à insérer.
- restitution le 26.
- faire un point avec Martin Harrop: toujours d'actualité.
- formation skywise academy.

TODO:
- @Imane: prez virtual assembly tool (et autres applications st40/41) semaine 10
- @AllDatascientists: commencer les meeting coaching P2P

### 2019-02-21T18:35:41+01:00

Point avec Hadi:
- XBOM
- Unified NC
- PC-SPC
- SFS
- RCA/DIVA
- QWT
- QBGG
- Industrial ramp-up
- IoT

### 2019-02-25T14:59:31+01:00

PC-SPC retrospective:

Chaimaa:
- présentation demain au client
- 3ème sprint d'industrialisation
- Data exploration plus longue que prévu

Marie:
- Backlog, Industrialisation --> figer backlog pour 4 prochaines semaines ce soir. Début de sprint ce soir.
- Faire une slide avec pour présenter le backlog macro et les tâches où on est dépendant des plants
- Hackathon Supaero: lundi toute la journée, mercredi après-midi

Orlando:
- Data Factory: arrivée
- Ingestion: grosse activité
- Précision organisationnelle:
  - ZILOL: les applis pour le shop floor,  personnes dédiées sur site. --> ils sont censés reprendre le portefeuille d'applications et l'ingestion des données.
  - ZIX: IT cross programme. Bernard Stevens.
- SMS / Email alerting: ça redémarre fort suite au workshop
- API supplier: sujet important également:
  - Hexcel déjà développé, support à fournir

Ali:
- Meeting avec Bernard Stevens: meeting avec ZIX (Bernard Stevens)
- Passage en run mode: ZIX / ZILOL
- Workshop:
  - Bernard agacé par le comportement de Grégoire
  - Guillaume CORMONT organise un 1er workshop métier pour:
    - revoir le dashboard
    - définir les critères métier
  - Outcomes:
    - Bernard MARQUEZ: augmenter le rate
    - Aujourd'hui on bute souvent sur la digitalisation.
    - Déployer le Virtual Assembly Tool (d'Imane) plus largement
  - Synthèse à faire.
  - Refaire le workshop tous les trimestres, avec Philippe MIRALLES.

Anouk:
- Communication avec le client du manque de données
- Prochain In-Flow board (demand management) mercredi: définir la roadmap sur les 2 semaines suivantes
- Début de framing sur automatisation de cockpits de KPIs.

Quentin:
- Backlog commun pour ce soir
- Objectif communiquer au moins sur notre occupation des 4 semaines suivantes.

Hadi:
- Workshop outcomes: plants espagnoles très dynamiques:
  - Puerto Real (Damien)
  - Illescas (Alex, Torben)
- Prio 1: démarrage Unified NC:
  - Nouvelles têtes: data stewards: Alexandre, Antoine
- Prio 2: concrétiser Skywise for Suppliers

TODO:
- @Marie & @Quentin: Communiquer à Guillaume les contraintes d'industrialisation à prendre en compte pour les dashboard alerting (données input)
- @Hadi: shooter un mail à Torben pour le use-case ML

### 2019-02-27T10:17:06+01:00

Go-Look-See Chaimaa:
- Slate: les charts doivent tenir sur une page / ne doivent pas dépasser la taille de la page
- Dataset versioning: utiliser les branches et les dates de snapshot pour aller voir une précédente version ou garder une version qu'on pense importante. Explorer avec contour (on peut choisir facilement la date du snapshot)
- Nommage folder & datasets:
  - enlever les mots superflus comme "dataset", "dashboard"
  - si folder avec 1 seul dataset: supprimer le folder
  - utiliser les noms des concepts pour nommer les datasets:
    - ex: jointure entre dataset "NC" et dataset "planning" = dataset "NC_planning"
- Contour report: se renseigner sur comment faire un rapport contour dynamique (avec des widgets input (toggle, saisie, ...))

### 2019-03-04T13:25:32+01:00

Point avec Imane - PC-SPC:
- participe au steering committee de la MFT - station 40/41

Data preparation:
- message: "on a créé un référentiel de donnée commun à toutes les plants qui n'existait pas avant."
- common data formatting --> common referential

Applications:
- message: "on a craqué divers use-case pour XX utilisateurs, nous vous en présentons qu'un seul."
- faire un menu des use-case
- virtual assembly tool --> en présentation
- retolerancing application --> en slides backup
- root end volume --> en slides backup
- root cause analysis --> en slides backup

Virtual Assembly tool business case:
- message: "cette application a le potentiel de sauver XX h d'over lead-time et YY h de temps de travail en déployant"

### 2019-03-04T14:17:13+01:00

Point PC-SPC retrospective:

Chaimaa:
- produit qui s'aligne avec les besoins du client
- point à améliorer:
  - accès à la donnée
  - intégrer le shopfloor
- nouveau UC: BSE performance cockpit:
  - dashboard pour monitorer les activités BSE
  - business value: réduire le temps de construction (2h / semaine)
  - data par sur skywise

Kevin / Orlando:
- Incident P0 clos, mise en place d'un outil python pour monitorer la data quality des flux machines. Outil en gestion.
- Data feature team: Aymeric / Jérôme (Airbus) --> Kevin Dreyfus les connaît.

Quentin:
- point avec Bernard ce soir ?
- fusion des backlogs aujourd'hui !

Orlando:
- SMS / e-mail alerting: fournir un planning: prévoir le workload / ressources
- API supplier:
  - Hexcel est en train de développer leur API
  - contacts: API squad Airbus, architectes Skywise
- Data quality monitoring tool

TODO:
- faire point avec Orlando/Kevin pour voir leur outil desktop de data quality monitoring
- demander à Mathieu comment sont ingérées les données des fournisseurs pour l'instant:

### 2019-03-11T14:01:32+01:00

Point PC-SPC:

Anouk:
- Framing BSE Cockpit: décevant: aucune donnée dans Skywise
- Digital Control Room --> Pages de liens vers des Sharepoints
- PCT: avec un compte service, faire un upload.
- Contacter: Adeline VATELIER
- Rencontrer Nuno: proposer de pitcher plusieurs sujets !
- Faire un inventaire des données BSE: contacter les data officer.

Quentin:
- QBG: gros risque PO.
- BSE Datalab: faire le point avec Anouk et Chaimaa.
- PC-SPC: Programmer début de sprint mercredi matin.
- Skywise for suppliers: y aller l'après-midi.

Chaimaa:
- Données pas vraiment fiable
- Unified NC: data engineer qui font le dataset

Marie:
- PC-SPC central:
  - On-boarding Tarek, Kevin
  - Test unitaires / Foundry
  - Passer sur la définition de l'architecture pour être en mesure d'alimenter Kevin/Tarek
- Premier point par téléphone à 17h
- Poser un sprint 1 début: mercredi matin.

Kevin:
- Incident Management: au courant
- Outil Centreon présenté par Alexis Lepierre de POPE: évangélisation à faire de ZILO et l'ingestion pour qu'ils utilisent cet outil.
- Workload:
  - Matin sur la toolbox
  - Après-midi sur les incidents

Imane:
- Root cause analysis sur le sujet du bootstrap: pb sur le process d'assemblage de l'aile: prez vendredi. Faire le point avec Hadi aujourd'hui.
- Point mercredi.

Ali:
- Pas de vision sur 2019.
- Ne prends pas le temps de rentrer dans les sujets.

### 2019-03-11T16:44:51+01:00

Point RH: que montrer à Ali pour le coacher:
- la communication par mail, c'est foireux: la PNL, le system 1 et le system 2, HBR feedback non verbal cues
- culture écrite vs culture orale
- la regle d'or de la communication par mail: que de la technique, pour le reste, privilégier la CNV et EN PERSONNE
- le triple moi: les positionnements du managements (et comment sortir du parent normatif en tant que manager)

Bonus:
- le SCARF model

### 2019-03-18T14:33:09+01:00

TODO:
- Voir avec Hadi:
  - Imane: pour journées digitalisation Single Aisle
  - Marie, Kevin: pour changement staffing
  - Anouk, Chaimaa: intégration dans un train
  - Anouk, Chaimaa: feedback de la discussion avec Benjamin ROUSSEL

Imane:
- Présentation le 3 avril
- Virtual Assembly Tool
- Outil sur Skywise pour anticiper l'overwork:
  - présenté par Antoine GAUDIN - BSEMO
- Connecter les 2 outils
- +1 ressources en cours: à voir

Marie:
- Tarek out ? comment on gère ? Revoir le backlog.

Ali:
- DSM: initiation du management visuel
- slides pour propale

Kevin:
- convention de nommage sur le backend
- convention de nommage sur le frontend: géré par Tarek: qui le reprend ?

Chaimaa:
- Frontend dev done
- Framing BSE cockpit: 3 workshops de design.
  - plusieurs maquettes: 1 dashboard commun + plusieurs dashboards
- Phonograph ?
- Perception de la valeur

Anouk:
- Lien avec la qualité: intégration dans un train pour gagner en visibilité pour pouvoir faire des demande d'ingestion
- Gestion de projet: mettre en place un weekly: avec Nuno.

### 2019-04-01T14:40:16+02:00

Point PC-SPC:
- Nouvel incident: action à prendre ?
  - ZILO passent en direct avec ZIID pour remettre en place le monitoring.
  - Marianna: mercredi meeting lancé par ZILO pour faire la FMEA:
    - François Michaud (ZIID)
    - Nicolas Bregniaux (ZILOL)
- Bernard RIBERE voit ZIPB ce lundi aprem !
- Monter une équipe data product Manufacturing: personne va vouloir payer (ni ZILOL, ni QMP) --> ZIPB ? A discuter avec Hadi ?
- Monitoring qui va être réactivé --> timeline à communiquer.
- Robin (Accenture): API supplier --> point à préparer.
- Plus communiquer la liste support PC-SPC

TODO:
- Hadi/Orlando: appeler Jean-Noel RIO ou Mariana PAVLIDI pour lui parler gouvernance et dire qu'il faut se coordonner avec ZIPB, ZILX
- Orlando: appeler Bernard pour savoir quand il voit ZIPB et essayer de pousser nos convictions:
  - faire une team data product manufacturing ?
  - se coordonner avec ZILOL, ZILX
- Quentin: faire relecture du la merge request de Marie
- Quentin/Ali: communiquer besoin d'implication des usines lors du scrum demain matin:
  - Industrialisation:
    - Point avec owner/designer Semaphore (Saint-Eloi/Nantes):
      - Répondre aux questions de Marie sur le contenu
      - Queries qui plantent dans le front
    - Point avec owner/designer Capability Dashboard (Stade): Gérer le point sur le naming dynamique des filtres.
  - Capability Library: développements en cours --> notre conviction: tant qu'il n'y a pas de framework de test de perfo de la lib: arrêtez les évols.
- Orlando/Ali: préparer point API supplier avec Robin.
- Marie/Orlando: finir mail / document process support

Point Station 40/41:
- Nouvelle orga: Implication ZI pour la data analysis / le data management. Méthode de travail qui se met en place.
- à Hambourg pour la digital week. Head of Digital. Présentation du virtual assembly tool en compétition pour des awards.
- Lundi prochain à Toulouse

Point Ground Tests:
- Mercredi: weekly
- Jeudi semaine prochaine: sprint review reportée --> pour avoir les stakeholders
- Livraison de la semaine:
  - Backlog: jeudi
  - Explo Data: vendredi
- Revoir le planning pour s'adapter aux craintes d'Emmanuel.
- Localisation: le matin, plutôt au M93 l'après-midi pour pouvoir travailler sereinement.
- Stakeholders

TODO:
- Marie/Quentin/Hachem: point 1h data NLP pour forger les convictions.
- Reda/Ali: point 30 min pour passer en revue le backlog (Ali contacte Reda si besoin).

Point BSE:
- début dev BSE Cockpit
- en parallèle: analyses sur les NC à finir: trouver les NC qui sont en rapport avec les pylônes
  - point avec Antoine: il n'y a pas les bonnes infos dans les colonnes ou les colonnes utiles (ex: "major component") ne sont pas bien remplies.
- Skywise Academy: Pablo ESCALADA-GOMEZ
- Requêtes analyse one-shot:
  - ACMS: Lundi, Nuno demande analyse pour répondre rapidement mercredi

TODO:
- Anouk/Chaimaa/Ali: Faire le feedback à Guillaume POIRIER des données manquantes dans le dataset NC.
- Anouk/Chaimaa/Ali: Faire le tour des data officer (Engineering, In Service) pour savoir quel est le contenu des données, avoir accès, pousser les demandes d'ingestion.
- Quentin: relancer Hadi sur les sujets d'amélioration continue: qui fait quoi sur le Knowledge Management (ici: le pb c'est qu'on a pas de catalogue qui permet de s'orienter vers les données).

### 2019-04-08T09:59:09+02:00

Point staffing:

Besoins:

- Station 40/41:
  - 1 DE --> ❓ Tiffanie SCHREYECK

- SfS - RCA:
  - 0.5 senior DS --> Benjamin
  - 1 DE --> Mehdi
  - 2 front --> ❓
  - 1 tech lead --> ❓
  - 0.5 UX --> ❓

- SfS - Dispatch: (on hold)
  - 1 Scrum/PPO
  - 1 DE
  - 1 front


### 2019-04-08T15:51:18+02:00

Point avec Imane Station 40/41:
- Travail sur predictive assembly tool
- Besoin de nouvelle ressource sur le sujet: Work sharing:
  - Management --> Imane
  - Root cause analysis --> Imane
  - Predictive Assembly Tool --> Imane
  - Industrialiser pipelines de données existant: Analyse statistique des mesures (capalib, Cp/Cpk) --> Nouvelle ressource
  - Data engineering & cleaning pour les prochaines campagnes de mesures --> Nouvelle ressource
- Echange sur les modèles prédictifs mardi

TODO:
- @Quentin/Hadi: Trouver un staffing et laisser Imane souhaite pouvoir l'appeler.

Point avec Ground Tests:
- Figer le sprint planning: lundi
- Contenu pour Restitution: jeudi soir

Point avec BSE Datalab:
- 7 sujets en même temps à instruire.
  - problématique: charge mentale, éparpillement


### 2019-04-08T17:21:27+02:00

Engagement PC-SPC:
- Faire entre 4 et 5.2 millions par rapport au coûts de 2017.

(BSE support) Station 40-41

Budget à zero sur l'A350: convaincre Patrick Chanet.

### 2019-04-09T09:33:39+02:00

RCA Skywise for suppliers - Time series:
- A320
- Anonymisation:
  - 2 vols consécutifs
  - certains paramètres sont enlevés
- Extraire les 2 vols autour d'un évènement choisi
- Chaque fournisseur a des paramètres pertinents pour son problème

Data science: on pourrait faire de l'anomaly detection, pour guider le fournisseur, mais pour l'instant c'est pas ce que veut Matthieu: faire simple.

Architecture scalable.

Arcane -->

### 2019-04-15T14:38:05+02:00

Point PC-SPC:

PC-SPC:
- meeting ZILO / ZIPB / ZIID / ZILX:
  - TODO: analyser la situation, identifier les contacts et lancer ce meeting

- planning sprint 2 à faire:
  - un premier meeting cet après-midi
  - un second meeting: 1h sans Marie

- capacity library: vendre à Patrick CHANET & Martin HARROP. D'abord montrer les inconvénients à Martin.
  - TODO @Ali: prévoir Martin HARROP - 16 mai (utiliser le 13/14/15 mai)

- Semaphore dashboard:
  - refactoring par les plants
  - requirements communiqués aux plants

- sprint précédent: 75% fait
- préparation point Pedro cet après-midi

Ground Tests:
- Démarrage des activités: sur RTI / DU:
- Points à poser:
  - Weekly --> mercredi
  - Weekly delivery: à poser, mercredi par exemple ?
- Workshops à préparer:
  - Identifier les participants:
    - Contour: Patrick ? Karim ? Manfred ?
    - Labelling: Patrick ? Karim ? + d'autres experts
  - Positionner les points
- Deliverable:
  - Quelques stats sur les NC qu'on remonte
  - Un ou deux bar charts bien sentis dans Contour

- Faire valider les labels par les stakeholders

BSE:
- meeting Pierre-Henri BROUSSE
- restitution avec Nuno:
  - assez picky sur le résultat, a demandé beaucoup d'adaptations, alors qu'il était PO.
- Learning:
  - être au maximum là-bas (au M91 pour le Weighing)
  - prépositionner les livraisons: envoyer la maquette 2 jours avant la demo au PO, s'il n'a pas pu la voir

- Règles de data gouvernance qui ne sont pas connues par tout le monde.
- Mise à jour de l'on-boarding toolkit à faire.
- Weighing: démarré

Station 40/41:
- Monthly WP6: slides en collaboration avec ZI
- Caroline CHABRE remplacée par Adeline WATTELIER (IM for SA)
- Team building ? On participe ou pas ?
- Organiser point avec Adeline pour parler de ses activités et ses besoins
- Relation avec ZI
- Brice RAILLER & Anthony remplace Stéphane SOUMILLON
- On-boarding:
  - récupérer PC
  -

TODO:
- @Ali: contacter Imane pour contacter Martin HARROP - réunion à partir du 16 mai sur la capacity library
- @Quentin, @Orlando: préparer meeting avec ZIL...
- @Reda: proposer template pour weekly et valider avec @Quentin
- @Hachem: proposer la stack du projet

### 2019-05-13T10:03:08+02:00

Pitch & Proposals:
- Q Ontology
- Unified NC
- SFS Dispatch
- IRU (Industrial Ramp-Up) Brainstorm

Comment communaliser les ressources - PC-SPC ?
- BSE Datalab
- PC-SPC: PRM à faire
  - voir les workpackages
  - montrer les livrables
  - capalib: nouveau process owner "Juan Jose"
  - Structuration:
    - Mise en place run mode:
      - Nouveaux Use-Cases (Ali)
      - Flux de données / Ingestion (Orlando):
        - Support
        - Setup
      - Applicatif / Industrialisation (Ali):
        - Dashboards
        - Capalib
        - Fin d'assessment (en discuter avec Ali)
    - Autres use-cases: Station 40/41 / BSE Datalab (Imane / Anouk)

TODO:
- PRM à préparer: date ?
- SFS: faire un point effet miroir avec Benjamin
- POE: appeler Pierre FORASTE: qui fait quoi ? objectifs ? planning du workshop
