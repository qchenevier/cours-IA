
### 2018-03-30T17:22:07+02:00

Rediriger Charles Renan vers ZOA Data scientists: POC

Point avec Patrice Brossier:
- code review sur l'ensemble des projets: KPIs. Pour éviter des écarts de qualité.
- prestation d'architecture (avec des vrais archis)
- process methods & tools (digital cockpit qui marche pas, jira/taiga, suivi de process: c'est un peu le bordel)
- focal points par métier

### 2018-04-13T17:30:54+02:00

Conviction sur support transverse:

Topics abordés pendant data meeting:
    07/02/2018: SRS data and builds monitoring
    24/01/2018: Foundry Build and Sync APIs
    17/01/2018: Phonograph
    20/12/2017: Importing Json as datasets and Foundry API
    13/12/2017: Foundry best practices (2/2) – Spark and Slate
    10/12/2017: Unit testing
    06/12/2017: Foundry best practices (1/2) – Project Setup and Pipelines authoring
    29/11/2017: branching best practices and import external code to Jupyter notebook
    22/11/2017: quick solutions
    15/11/2017: technical documentation (2/2), feature Single Aisle demo (quality gate)
    08/11/2017: tech lead and coach roles, technical documentation (1/2)

- code review sur l'ensemble des projets: KPIs. Pour éviter des écarts de qualité.
- prestation d'architecture (avec des vrais archis)
- process methods & tools (digital cockpit qui marche pas, jira/taiga, suivi de process: c'est un peu le bordel)
- focal points par métier

- technical quality:
    - code review sur l'ensemble des projets:
        - KPIs automatisés visualisés dans un dashboard ==> 1 fois par semaine (par jour ?)
            - code dupliqué
            - nombre de commentaires
            - longueur des fonctions
            - ...
        ==> 10 jours pour MVP
        - KPIs semi-manuels (au bout d'1 mois de projet + tous les 3 mois):
            - lisibilité des noms de fonctions, etc.
            - architecture / dette technique
        ==> 0.5 jours tous les 3 mois
    - architecture:
        - combien de jours par semaine ? 1 archi plein temps ?
        - les prestations d'architecture doivent être fait par les même personnes qui font les code reviews tous les 3 mois ==> permet d'identifier les points durs techniques et de transmettre les lessons learnt
    - process methods & tools:
        - ?
    - focal points par métier
        - ?

Reboucler:
    - Anouar: DevOps, qu'est-ce qu'il avait présenté à Chris Taylor ?

    - Annabelle:
        - Point focal métier ?

    - Aurélie Cazenave:
        - Qu'est-ce qu'il faudrait faire en tant que support ?
        - Comment pourrait-on sortir de la plateforme pour faire du front-end sur ce qu'on veut ?
        Mission:

### 2018-04-17T15:11:09+02:00

Bonnes pratiques: Talon

Comment vous visualisez vos dépendances (monocle) ?
Comment vous êtes organisés ?
    Branching ?

Preco back:
    - git clone en local (en se créant un token longue durée)
    - dev en local avec un vrai IDE
    - banc de test: sur les transfos python

Testing:
    - pytest (mais pas applicable aux dataframes)
    - reboucler avec Anouar sur pytest et le formattage du paquet pytest

Coding:
    - branching / merging: utiliser les merge requests et faire des revues de code à chaque branche, avec le niveau d'exigence que l'équipe peut se permettre.

Branching dans Slate:
    - avoir 1 export postgate par branche.
    - switcher d'une branche à une autre à l'aide d'une variable globale.

A rajouter dans le code quality support:
    - banc de test python (version marc)
    - test avec pytest modifié pour pysparl (version anouar (ou le faire moi-même))
    - dashboards de monitoring des apps pour chaque projet

### 2018-04-30T10:16:48+02:00

Propale:

Technique:
- Audit automatisé:
    - back: analyse de code ==> rapport automatique: 1 FTE pendant 1 mois
    - front: analyse perfo slate ==> rapport automatique: 1 FTE pendant 1 mois
- Audit manuel:
    - 10 projets / mois
    - 2h / back
    - 2h / front
- REX réguliers (erreurs à ne pas faire, lessons learnt, hacks):
    - identification pendant les audits
    - capitalisation dans un dossier pour tout le monde
    - 2 REX d'une heure / mois ==> entre 8 h de boulot par REX (slides plus capitalization).

IDENTIFIER LE QUI ?

Management plateau et méthodo:
- A l'échelle de l'équipe adherence au méthodo scrum: value tracking
    - Coaching sur la valeur
- A l'échelle du plateau: équipes indentifient bien leurs dépendances et les résolvent
    - Outillage pour ça ==> version one ==> training

### 2018-06-08T13:27:38+02:00

Code Quality:
- 1 **support ppt**

Feature_library = quick solutions
- code templatisé
- à récupérer auprès de la core team

On-boarding
- 2 sessions:
    - awareness sur le plateau, foundry ==> **support ppt**
    - 1 semaine après: deep dive sur la mission du dev
- exercices pour data scientists

### 2018-07-24T10:45:21+02:00

Point avec Pablo:

Slate audit: KPI dans developper tools:
- temps de chargement
- nb de requests
- nb d'erreurs au chargement ==> attention aux erreurs génériques de la librairie slate, ce qu'on cherche ces les erreurs de chargement de queries

Slate audit: KPI analyze json:
- nb events ==> doit rester limité
- nb queries
- est-ce que les queries sont conditionnées ==> fort impact sur perfo

### 2018-07-26T09:28:35+02:00

Actions:
- se refaire une passe sur un support de bonnes pratiques à respecter
    - mettre à jour la partie backend (Quentin)
    - mettre à jour la partie frontend (Pablo)
- prendre contact avec les projets (Quentin):
    - SHOP: Anthony Gros
    - PCT: Elodie Regis / Benjamin Farcy
    - SIF: Perrine Dupuy
- envoyer la propale à Patrice / Zohair

### 2018-07-30T10:14:58+02:00

SHOP audit:

- appli de gestions des ressources sur A380: charge capacité.

les utilisateurs:
- ingestion manuelle de fichiers CSV (tous les matins !!)
- trigger le build à la main

enjeu:
- passage à l'A320:
    - plus de personnes ==> meilleure gestion des droits
    - passage à l'échelle

- archi: schema archi ==> préciser le lead time entre ingestion et utilisation par les users

- performance: refresh actuel supérieur à 15s (peut-être dû à Phonograph)

- utilisation de phonograph pour faire du transactionnel.

### 2018-08-08T13:48:57+02:00

Code quality: Pablo:

A savoir: deploiement outil d'analyse perfo slate dans 1-2 mois.

Prérequis:
- accès aux dashboards slate en écriture
- accès au dossier projet (et aux repositories) en lecture
- savoir montrer la documentation existante du projet

09:00   Présentation de la démarche: 10 min
09:10   Présentation du projet & contenu fonctionnel: 35 min
09:45   Présentation des bonnes pratiques: 45 min
10:30   Pause: 15 min
10:45   Discussion et identification des "pain point" principaux: 30 min
11:15   Analyse automatique du front & du back: 15 min
11:30   Analyse manuelle du front & du back: 30 min
12:00   Lunch
13:15   Rédaction rapport audit (KPI + recommendations): 15 min
13:30   Présentation des recommendations: 45 min
14:15   Fin

### 2018-09-11T09:15:22+02:00

Réunion avec Patrice Brossier, Zohaire Ayoub, Eric Foch, Pablo Escalada-Gomez, Quentin Chenevier:

Actions:

- Coacher/Auditer qualitics

- Amélioration Audit feedback:
    - Illustrer sur chaque metrique quel est la bonne pratique: description
    - Rajouter des liens vers les bonnes pratiques (ou les tutoriels) pour les metriques

- Feedback collectif mis en standby: à remplacer par un feedback fait lors d'un Skywise-DevFest

A instruire techniquement et commercialement:

- Convergence avec le Skyfolio: Actions à faire pendant l'audit manuel: mettre à jour le skyfolio avec la liste des composants Palantir utilisés (Slate, Phonograph, ...)
- Automatisation/Packaging: Instruire techniquement: intégration des audits automatiques dans des dasboards, intégrés au Skyfolio

Vision à atteindre:

2 niveaux audit:
- 1 audit automatisé dans skyfolio
- 1 audit expert manuel (as a service)
    - audit obligatoire (push)
    - audit volontaire (pull)
    Prestations à définir (qui fait quoi, quand, livrables et prérequis)

### 2018-09-20T11:16:34+02:00

Meeting with Palantir on code quality coaching:

Palantir code qulaity check:
- tracking only on quality dashboards
- have defined thresholds (which are defined to strictly, so we need to feedback them)

Discussion:
- planning ahead the complexity of the app and structuring
- modularity: no libraries, no import in Slate

### 2018-11-08T16:00:56+01:00

Réunion avec Cedric Cormont et François Michaud:
- faire un support autoporteur pour expliquer aux dev comment faire un audit, front + back ==> rapport contour
- rajouter lien vers bonnes pratiques mises à jour (ou intégrer conseils).
- faire mise à jour des bonnes pratiques backend ==> QC
- ils vont intégrer cette feature (automatic audit) au PI planning ==> pas de proposition technique de notre côté à faire

Rapport contour avec ce plan:
- Faire son Audit tout seul (backend & frontend):
    - extraire le code
    - faire tourner l'outil d'analyse
    - analyser les KPIs et prendre des décisions (pourquoi il faut maintenir certains KPIs à une valeur donnée)
    - best practices et common pitfalls

2 Skuds:
- "Capgemini est un partner, vous auriez dû faire ça sans qu'on vous le demande et sans le facturer."
- "Les problèmes récurrents (sur le front notamment) doivent être renvoyés aux équipes Cap pour qu'elles balayent devant leur porte."
