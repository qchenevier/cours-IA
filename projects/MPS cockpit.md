
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
