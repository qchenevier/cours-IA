
### 2017-10-03T09:33:05+02:00

Point avec MPS Cockpit (Antoine et Imane) (Master Planning Schedule = PDP) avec Fabrice SCHLEGEL et Eric BODINIER d'Airbus.

- data sources pas les mêmes pour UK et Hambourg
- à déployer sur 11 sites
- 4 mois depuis la première expression du besoin

MPS = PDP: a paritr de la demande client, dimensionner tous les moyens de production.

- meeting mensuel: revue de perfo des ressources, éval demande & validation planning 12 mois
- meeting hebdomadaire: validation des planning à 3-4 mois
- meeting daily: (hors scope) identification des problèmes

C'est valable pour 2 programmes: A350 & SA. En plus y'a un meeting chapeau pour chaque usine où le chef d'usine passe en revue la prod sur tous les programmes.

Objectifs du projet:

- Coût: Pour chaque revue, 3 jours de travail à chaque fois, juste pour récupérer toutes les data: les data sources et les data owners sont différents.
- Volumétrie: les extracts/requêtes de SAP sont trop gros pour excel.

Attention, il faut pouvoir saisir manuellement des données dans l'outil: quelles sont les capacités de salt ?.

Data sources. La personne qui compile les données est un adjoint de CDT. Y'a des cas d'utilisation un peu touchy: ex: IPK: refresh tous les mois, mais avec possibilité de compléter les données à la main au fil du mois.

Dashboard commun à tout le monde ? Le but c'est modéliser 80 % des indicateurs commun à tous les pays.

Way-forward: lancement de réunions avec les utilisateurs à saint-nazaire en commençant par le SA, jeudi la semaine prochaine.

Porté par Projet Quantum (sponsorisé par F.Brégier): éventuellement présentation le 12 octobre ==> projet visible.

### 2017-10-03T15:32:13+02:00

Point avec MPS Cockpit:

- le process de data ingestion a été vu, il faut remplir un fichier excel en ayant identifié: Data owner et contact ICT pour chaque. Normalement c'est Eric BODINIER qui devrait le faire. Le faire à la volée quand les gens sont rencontrés sur place.
- Mon rôle pour le sprint 0: former imane sur la plateforme (back-end et front-end) (y compris faire quelques pipelines + dashboard à 4 mains) & comprendre comment on va intégrer les saisies utilisateur.

### 2017-10-18T16:14:49+02:00

Chiffrage MPS Cockpit:

- séparer KPI:
    - entre front-end et back-end: ce qui nécessite un filtre ce sera fait en front, le reste en back.
    - quels sont les KPI les plus complexes et les quick-wins

2 data engineers pour 2 mois. Mais c'est risqué parce qu'on a jamais fait un projet aussi cours, mais ça paraît faisable vu que les KPI sont bien définis. Attention, projet similaire, avec des KPIs mal définis, tourne depuis 10 mois.

Version light:
- tableau
    - sans sélection de l'ordre
    - avec extract excel
    - avec input séparé (sheets)
    - en 2 à 3 versions différentes en fonction des _users rights_
- un graphique par KPI quand on clique
    - avec extract png

2 data engineer et un front-end sur 2 sprint + peut-être 1 peu plus.

high-business maturity si on reste dans le périmètre "light"
low-business maturity sur toutes les features front-end supplémentaires

A priori, cette app n'est pas destinée à être dans Foundry: la stack technique n'est pas adaptée pour faire du front-end complexe. Si on voit plus loin que le sprint de 2 mois, ça va être difficile d'intégrer les features restantes.

### 2017-10-20T10:43:44+02:00

Archi MPS Cockpit avec Cedric Cormont:

- feature 1: manual input + instant recompute: solution = input dans SALT (partagé entre les utilisateurs) et recalcul dans le front-end (fonctions js dans SLATE)
- feature 2: customizable HMI, report generation, fine user rights mangement: solution = custom front-end branché sur le SQL avec son back-end approprié.

Faire une archi step 1 qui implémente feature 1 dans foundry + slate
Faire une archi step 2 qui réimplémente feature 1 et implémente feature dans foundry + custom front-end ==> à instruire techniquement.

### 2017-10-23T10:04:19+02:00

MPS Cockpit:

Selon lui, pas un souci d'utiliser sheets. Etrange. réunion demain de visu avec lui pour voir confirmer/infirmer. On doit préparer un miniPOC pour ça.
