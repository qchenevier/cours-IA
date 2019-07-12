
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
