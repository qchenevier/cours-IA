---
title: Intelligence Artificielle en 2021
presentation:
  theme: black.css
  enableSpeakerNotes: true
  maxScale: 0.8
  slideNumber: true
  previewLinks: true
---

<!-- slide data-background-color="#222222" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/World.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

# Intelligence Artificielle en 2021

<!-- slide vertical=true-->

## Qu'attendez-vous de ce cours ?

<!-- slide vertical=true-->

## Qui êtes-vous ?

Le cours s'adresse à tous publics ayant

- tous niveaux techniques (du plus bas au plus élevé)
- tout type de rôle dans une organisation (employé, manager, dirigeant)
- dans toute taille d'organisation (PME, grand groupe)

<!-- slide vertical=true-->

## Qu'allons-nous essayer d'apprendre ?

- anticiper l'impact de l'IA dans la société
- anticiper la transformation de son entreprise avec l'IA
- toucher du doigt et comprendre ce qu'est l'IA
- savoir gérer un projet IA dans son entreprise

<!-- slide vertical=true-->

## Au menu

2 sessions:

| Plage horaire | Atelier             |
|:-------------:|:------------------- |
| <small> 20m  | 🤗 Accueil & Intro  |
| <small> 1h 30m | 🤔 Partie Théorique |
| <small> 10m  | ☕️ Pause            |
| <small> 1h 30m  | 😅 Atelier pratique |
| <small> 30m | 🎁 Présentation |

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## C'est quoi l'IA

<!-- slide vertical=true data-background-color="#222233"-->

### Les 3 étapes de l'IA

<img src="https://www.researchgate.net/publication/323591839/figure/fig8/AS:601346701008897@1520383634410/Development-history-of-artificial-intelligence-AI.png" style="object-fit: cover; object-position: 0 0; width: 100%; height:250px;">

Des méthodes d'IA différentes au cours du temps:

1. code classique (`if → then → else`)
2. système expert utilisant des règles créées à la main
3. algorithmes statistiques _apprenant_ les règles (_machine learning_)

<small>Source: [State-of-the-Art Mobile Intelligence (research paper)](https://www.researchgate.net/publication/323591839_State-of-the-Art_Mobile_Intelligence_Enabling_Robots_to_Move_Like_Humans_by_Estimating_Mobility_with_Artificial_Intelligence)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Les systèmes experts

Le savoir est renseigné par des experts.

<img src="https://sites.google.com/site/mrstevensonstechclassroom/_/rsrc/1382374591344/hl-topics-only/4a-robotics-ai/5-expert-systems/expert%20system.png" width=62%>
<img src="https://sites.google.com/site/keremitgsnotes/_/rsrc/1456600594794/chapter-16---ai-and-robotics/expert-systems/Capture.PNG" width=35%>

<small>Sources: various ITGS courses: [here](https://sites.google.com/site/mrstevensonstechclassroom/_/rsrc/1382374591344/hl-topics-only/4a-robotics-ai/5-expert-systems/) and [here](https://sites.google.com/site/keremitgsnotes/_/rsrc/1456600594794/chapter-16---ai-and-robotics/expert-systems/).</small>

<!-- slide vertical=true data-background-color="#222233"-->

### L'IA, c'est du _Machine learning_

Le savoir est extrait des données.

<img src="https://imgs.xkcd.com/comics/machine_learning_2x.png" width=40%>

<small>C'est auss le mariage de l'expérimentation et des statistiques:
c'est de la cuisine avec des algorithmes<br>
Source: [xkcd](https://xkcd.com/1838/)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Principes du _machine learning_

|            |                                                                                                                 |
|:---------- |:--------------------------------------------------------------------------------------------------------------- |
| Modèle     | <small><b>fait la prédiction</b><br>régression linéaire, réseau de neurones, ...</small>                        |
| Optimiseur | <small><b>modifie le modèle pour réduire son erreur</b><br>descente de gradient, algorithmes génétiques</small> |

<img src="https://www.deepnetts.com/wp-content/uploads/2019/02/SupervisedLearning.png">

<small>Source: [From Linear Regression to Deep Learning in 5 Minutes](http://www.deepnetts.com/blog/from-linear-regression-to-deep-learning-in-5-minutes.html)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### La programmation différentielle

Apprentissage = optimisation de fonctions différentiables

![](https://miro.medium.com/max/1414/1*IjxpxWcKX8EJUVFBNFeKdA.gif)

<small>Une fonction différentiable permet de calculer le gradient de l'erreur.
A chaque itération, le gradient dit comment modifier les paramètres pour réduire l'erreur.<br>
Source: [Linear Regression by using Gradient Descent Algorithm: Your first step towards Machine Learning (medium)](https://medium.com/meta-design-ideas/linear-regression-by-using-gradient-descent-algorithm-your-first-step-towards-machine-learning-a9b9c0ec41b1)</small>

<!-- slide vertical=true data-background-iframe="https://www.geogebra.org/m/xC6zq7Zv"-->

<!-- slide vertical=true data-background-color="#222233"-->

### La révolution du _deep learning_

La **composition** de modèles simples (neurones)
crée un modèle complexe.

<img src="https://www.pnas.org/content/pnas/116/4/1074/F2.large.jpg?width=800&height=600&carousel=1" width=80%>

<small>Source: [News Feature: What are the limits of deep learning? (PNAAS)](https://www.pnas.org/content/116/4/1074)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Le deep learning facilite la conception de modèle

👍 Plus besoin de créer des variables
👎 Nécessite beaucoup de données  💾 et de calculs 🥵

<img src="https://bluehexagon.ai/wp-content/uploads/2019/04/Screen-Shot-2019-04-04-at-1.05.20-PM-1024x600-1024x600.png" width=70%>

<small>Source: [Blue Hexagon](https://bluehexagon.ai/blog/what-is-deep-learning-and-how-is-it-different-from-machine-learning/)</small>

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Demo time ! 🥳

<!-- slide data-background-color="#222233" vertical=true -->

### Demo computer vision

[Teachable Machine](https://teachablemachine.withgoogle.com/train/image)

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_petit_renard.png" width=70%>

<small>Comme un programme "bête", une IA ne sait pas gérer les cas imprévus
</br>Backup: [∅](https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_pas_de_figurine.png) [🦊](https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_petit_renard.png) [🐶](https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_petit_chien.png) [😸](https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_petit_chat_outlier.png) [❓](https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/demo_teachable_machine_toutes_les_figurines_outlier.png)
</small>

<!-- slide data-background-color="#222233" vertical=true -->

### Liste de démos

- Demos repositories:
  - [AI Experiments | Experiments with Google](https://experiments.withgoogle.com/collection/ai)
  - [tensorflow.js examples](https://github.com/tensorflow/tfjs-examples/)
  - [An Interactive Node-Link Visualization of CNN](https://www.cs.ryerson.ca/~aharley/vis/)
- Google AI experiments:
  - [Teachable Machine](https://teachablemachine.withgoogle.com/)
  - [Melody Mixer](https://experiments.withgoogle.com/ai/melody-mixer/view/)
  - [Beat Blender](https://experiments.withgoogle.com/ai/beat-blender/view/)
  - [Sound Maker](https://experiments.withgoogle.com/ai/sound-maker/view/)
  - [Thing Translator](https://thing-translator.appspot.com/)
  - [Quick Draw](https://quickdraw.withgoogle.com/)


<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## cadrer et mener un projet IA

<!-- slide vertical=true data-background-color="#222233"-->

### Analyser les décisions pour évaluer la valeur

📊 Information + ✋ Décision = 💰 Valeur
</br>

<table class="fragment" data-fragment-index="0">
  <tr>
    <th>Données</th>
    <th>Produit</th>
    <th><span style="color:cyan">Décision</span></th>
    <th>Valeur</th>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>Senseurs météo</td>
    <td>Prévision Météo</td>
    <td><span style="color:cyan" class="fragment" data-fragment-index="2"><small>Un citadin prend un parapluie avant de sortir</small></span></td>
    <td><span class="fragment" data-fragment-index="3">~ 0€</span></td>
  </tr>
  <tr class="fragment" data-fragment-index="4">
    <td>Senseurs météo</td>
    <td>Prévision Météo</td>
    <td><span style="color:cyan"><small>Un producteur de vin protège ses vignes avant la grèle</small></span></td>
    <td><span class="fragment" data-fragment-index="5"> 100€/an 💰</span></td>
  </tr>
  <tr class="fragment" data-fragment-index="6">
    <td>Images satellites</td>
    <td>Estimation des réserves de pétrole</td>
    <td><span style="color:cyan"><small>Un trader achète ou vend du pétrole sur le marché</small></span></td>
    <td><span class="fragment" data-fragment-index="7"> 10M€/an 💰💰💰</span></td>
  </tr>
</table>

<!-- slide vertical=true data-background-color="#222233"-->

### Agile: _fail fast, learn quick_

Expérimentation: il faut payer pour voir 🃏

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png" width=55%>

<small>Source: [CRISP-DM (Wikipedia)](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Qualifier une idée de projet

Se renseigner sur l'état de l'art:

- [Demander à Google](https://www.google.com/search?q=ai+applications+in+...)
- [Nvidia - AI Applications](https://www.nvidia.com/en-us/industries/)
- [OCDE - Applications de l’IA](https://www.oecd-ilibrary.org////sites/b7f8cd16-fr/1/2/3/index.html?itemId=/content/publication/b7f8cd16-fr&_csp_=4890b942b269008dad8522c358cb03ca&itemIGO=oecd&itemContentType=book#)
- [Papers with code](https://paperswithcode.com/sota)

<!-- slide vertical=true data-background-color="#222233"-->

### Qualifier une idée de projet

Demander son avis à un expert:

<img src="https://imgs.xkcd.com/comics/tasks_2x.png" width=30%>

<small>Source: [xkcd](https://xkcd.com/1425/)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Les clés du succès d'un projet IA

<!-- slide vertical=true data-background-color="#222233"-->

#### Les données avant les algorithmes

L'IA, c'est des vieux algorithmes
appliqués à des données récentes.

<img src="https://images.squarespace-cdn.com/content/54345ed8e4b0fa5705e1825b/1459449530701-68FQZ878JRPQCE97XVCC/AIBreakthrough.png?content-type=image%2Fpng" style="background-color:white;">

<small>C'est la collecte de donnée qui permet les percées en IA.
Source: [Datasets Over Algorithms (kdnuggets)](https://www.kdnuggets.com/2016/05/datasets-over-algorithms.html)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Open source et open data

Les meilleures solutions émergent
de la confrontation des idées.

- Tirer parti des modèles et publications open source (model hubs, papers with code, etc.)
- Faire des compétitions ouvertes en partageant vos données (hackathon).

Dans tous les cas, exiger d'avoir le code & les données.

<!-- slide vertical=true data-background-color="#222233"-->

### Des ressources multi-facettes

Entraîner un algorithme = 10% d'un projet

![ML system infrastructure.png](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/11-13-30-59-ML%20system%20infrastructure.png)

<small>Faire du machine learning en laboratoire c'est facile,
mais savoir livrer une solution fonctionnelle est difficile.<br>
Source [Machine Learning: The High-Interest Credit Card of Technical Debt](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### La connaissance des algorithmes ne se suffit pas à elle-même

Un bon data scientist doit être _full-stack developer_,
ou être intégré à une équipe plus large.

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2021/04/distracted%20data%20scientist.jpg" width=70%>

<small>Beaucoup d'équipes data peinent à livrer des solutions industrielles pour leur entreprise.</small>

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Exercice

|               |                                                                                                                           |
|:------------- |:------------------------------------------------------------------------------------------------------------------------- |
| Secteur       | <small>Choisir un secteur, choisir une entreprise emblématique</small>                                                    |
| Brainstorming | <small>En explorant les 3 values disciplines: brainstormer sur les idées de transformation IA qu'on peut proposer</small> |
| Valeur        | <small>Evaluer la valeur en analysant les décisions améliorée par cette IA</small>                                        |
| Faisabilité   | <small>Evaluer la faisabilité en trouvant des exemples analogues</small>                                                  |
| Données       | <small>Imaginer quand et comment on pourrait obtenir des données</small>                                                  |
| Pitch         | <small>Pitcher</small>                                                                                                    |

👉 [template google slides](https://drive.google.com/file/d/1BuLnveNRNJRNg_HIFCDQTxFSJ80jhyQM/view?usp=sharing)

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Performance de l'IA

<!-- slide vertical=true data-background-color="#222233"-->

### De multiples mesures de performance

La mesure de la performance est différente en fonction de l'utilisation de la prédiction.

☝️🧐 Se méfier des annonces impressionnantes. Toujours se poser 3 questions:
- quelles données pour faire l'apprentissage ?
- quelles données pour mesurer la performance ?
- quelle mesure de performance ?

<!-- slide vertical=true data-background-color="#222233"-->

### Quelles données pour évaluer ?

<img src="https://woborders.files.wordpress.com/2017/09/screen-shot-2017-09-09-at-10-23-23-am.png?w=1200" width=80%>

Une IA arrive détecte l'orientation sexuelle
à partir de la forme du visage !

<span class="fragment"> Vraiment ? 🤔</span>

<small>Source: [Do algorithms reveal sexual orientation or just expose our stereotypes?](https://medium.com/@blaisea/do-algorithms-reveal-sexual-orientation-or-just-expose-our-stereotypes-d998fafdf477)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Quelles données pour évaluer ?

L'IA utilise: barbe 🧔, lunettes 👓, maquillage 💄

<img src="https://miro.medium.com/max/1400/1*LMStwP_9zpt4f07ucikKAA.png" width=46.5%>
<img src="https://miro.medium.com/max/5868/1*0cejtAX8SmWFowTTNGDvNg.jpeg" width=35%>
<img src="https://miro.medium.com/max/1400/1*CgMr2mrMVafEzHfZIFpdnQ.png" width=46.5%>
<img src="https://miro.medium.com/max/1400/1*yBV4GuFfr33UPhbMiVF9XA.jpeg" width=35%>

<small>L'IA reproduit les stéréotypes qu'elle trouve dans les données 🤦‍
Source: [Do algorithms reveal sexual orientation or just expose our stereotypes?](https://medium.com/@blaisea/do-algorithms-reveal-sexual-orientation-or-just-expose-our-stereotypes-d998fafdf477)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Quelles données pour évaluer ?

_Train-test split_:
Séparer les données d'apprentissage
& les données d'évaluation

<img src="https://elitedatascience.com/wp-content/uploads/2017/06/Train-Test-Split-Diagram.jpg" width=80%>

<small> ⚠️ la performance mesurée sur le _train_ est toujours surestimée !
Source: [Elite data science](https://elitedatascience.com/model-training)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### L'Overfitting: l'erreur de débutant

Modèle qui "colle" aux données d'entraînement
sans retenir le savoir sous-jacent (bachottage)

<img src="https://qph.fs.quoracdn.net/main-qimg-17ec84ff3f63f77f6b368f0eb6ef1890.webp" width=50%>
<img src="https://i.redd.it/ze7i4nhq0se41.jpg" width=40%>

<small>Cela fait croire qu'un modèle est performant (en laboratoire),
alors qu'il est médiocre (en conditions réelles).<br>
Source: [Quora](https://www.quora.com/Is-it-possible-for-a-Machine-Learning-model-to-simultaneously-overfit-and-underfit-the-training-data)</small>

<!-- slide vertical=true data-background-color="#222233"-->

## Exemples

<!-- slide vertical=true data-background-color="#222233"-->

### Diagnostic de la maladie de lyme

- Difficile à diagnostiquer
- ⚠️ Maladie rare: 9 cas / 100 000 en France

Créons une IA qui fait un diagnostic automatisé ?! 💪😏

<small>Source: [Lyme disease in France: a primary care-based prospective study](https://www.sentiweb.fr/1023.pdf)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Modèle 1: faux positifs & faux négatifs de 1 %
N = 100 000 personnes, prévalence = 9 / 100 000

<table>
  <tr class="fragment" data-fragment-index="1">
    <td>Malades</td>
    <td></td>
    <td>9</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Faux négatifs</td>
    <td><small>1% * malades</small></td>
    <td>0</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Vrais positifs</td>
    <td><small>99% * malades</small></td>
    <td>9</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>Pas malades</td>
    <td></td>
    <td>99 991</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Faux positifs</td>
    <td><small>1% * pas malades</small></td>
    <td>999</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Vrais négatifs</td>
    <td><small>99% * pas malades</small></td>
    <td>98 992</td>
  </tr>
  <tr class="fragment" data-fragment-index="3">
    <td>Précision</td>
    <td><small>vrais prédictions / N</small></td>
    <td><span style="color:green">99 %</span></td>
  </tr>
  <tr class="fragment" data-fragment-index="5">
    <td><small>Chances d'être malade<br>si testé positif</small></td>
    <td><small>vrais positifs /<br>faux + vrais positifs</small></td>
    <td><del>99 %</del> <span style="color:red" class="fragment" data-fragment-index="6">&nbsp; 0.89 % 🤔</span></td>
  </tr>
</table>

<!-- slide vertical=true data-background-color="#222233"-->

### Modèle 2: toujours négatif ⚠️
N = 100 000 personnes, prévalence = 9 / 100 000

<table>
  <tr class="fragment" data-fragment-index="1">
    <td>Malades</td>
    <td></td>
    <td>9</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Faux négatifs</td>
    <td></td>
    <td>9</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Vrais positifs</td>
    <td></td>
    <td>0</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>Pas malades</td>
    <td></td>
    <td>99 991</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Faux positifs</td>
    <td></td>
    <td>0</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Vrais négatifs</td>
    <td></td>
    <td>99 991</td>
  </tr>
  <tr class="fragment" data-fragment-index="3">
    <td>Précision</td>
    <td><small>vrais prédictions / N</small></td>
    <td><span style="color:green">99.991 % 🤔</span></td>
  </tr>
  <tr class="fragment" data-fragment-index="5">
    <td><small>Chances d'être malade<br>si testé positif</small></td>
    <td><small>vrais positifs /<br>faux + vrais positifs</small></td>
    <td>❌</td>
  </tr>
</table>

<!-- slide vertical=true data-background-color="#222233"-->

### Diagnostic du Covid-19

Test PCR du frottis nasopharyngé

<img src="https://i.ytimg.com/vi/L8I7mum4eZw/hqdefault.jpg" width=40%>

|||
|:--|:--|
|Faux positifs| 1 % |
|Faux négatifs| entre 15 et 45 % 😱|
|Prévalence| entre 1 et 5 % en Ile-de-France |

<small>Source: [Performance du frottis nasopharyngé-PCR pour le diagnostic du Covid-19. Recommandations pratiques sur la base des premières données scientifiques](https://www.revmed.ch/RMS/2020/RMS-N-689/Performance-du-frottis-nasopharynge-PCR-pour-le-diagnostic-du-Covid-19.-Recommandations-pratiques-sur-la-base-des-premieres-donnees-scientifiques)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### PCR: faux positifs 1% & faux négatifs 30%
N = 100 000 personnes, prévalence = 3 %

<table>
  <tr class="fragment" data-fragment-index="1">
    <td>Malades</td>
    <td></td>
    <td>3 000</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Faux négatifs</td>
    <td><small>30% * malades</small></td>
    <td>900</td>
  </tr>
  <tr class="fragment" data-fragment-index="1">
    <td>&emsp;Vrais positifs</td>
    <td><small>70% * malades</small></td>
    <td>2 100</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>Pas malades</td>
    <td></td>
    <td>97 000</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Faux positifs</td>
    <td><small>1% * pas malades</small></td>
    <td>970</td>
  </tr>
  <tr class="fragment" data-fragment-index="2">
    <td>&emsp;Vrais négatifs</td>
    <td><small>99% * pas malades</small></td>
    <td>96 030</td>
  </tr>
  <tr class="fragment" data-fragment-index="3">
    <td>Précision</td>
    <td><small>vrais prédictions / N</small></td>
    <td><span style="color:green">98.13 %</span></td>
  </tr>
  <tr class="fragment" data-fragment-index="5">
    <td><small>Chances d'être malade<br>si testé positif</small></td>
    <td><small>vrais positifs /<br>faux + vrais positifs</small></td>
    <td><span style="color:orange" class="fragment" data-fragment-index="6">68.4 % 🤔</span></td>
  </tr>
</table>

<!-- slide data-background-color="#332222" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Bokeh.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Les principes de la révolution digitale

- Un monde chaotique mais structuré
- Des machines à croissance exponentielle
- Des humains à changements linéaires

<!-- slide vertical=true data-background-color="#332222"-->

### Identifier les tendances structurantes

Penser en **vecteurs de force**:

quelles sont les tendances qui ont une direction et une force constante ?

<!-- slide vertical="true" data-background-color="#332222"-->

### Les tendances structurantes sont exponentielles

Signaux faibles aujourd'hui = explosions demain

<img src="https://pbs.twimg.com/media/Ews3N6OUUAE32tL?format=jpg&name=large"  width=70%>

<small>Une tendance exponentielle ne change pas de nature: elle se renforce au cours du temps.</br>Source: [@vb_jens](https://twitter.com/vb_jens/)</small>

<!-- slide vertical="true" data-background-color="#332222"-->

### Machines exponentielles

La performance des technologies de l'information <br>est en accélération exponentielle

- Calcul: performance, coût
- Données: transmission, volume, pénétration

<!-- slide vertical=true data-background-color="#332222"-->

#### Intelligence bon marché

Puissance de calcul par dollar x2 tous les 18 mois

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/20-11-45-20-Moores_Law_over_120_Years.png" width=70%>

<small>Source: [Moore's Law over 120 Years (Ray Kurzweil)](https://commons.wikimedia.org/wiki/File:Moore%27s_Law_over_120_Years.png)</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Intelligence omniprésente

Nombre de transistors par humain x10 tous les 5 ans

<img src="https://254155-841844-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2017/04/Global-production-of-transistors-per-capita-selected-years-historic.png" width=70%>

<small>Source: [Darrin Qualman blog](https://www.darrinqualman.com/global-production-transistors/)</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Intelligence connectée & mobile

Le haut débit mobile devient une commodité

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/19-22-11-49-ITU%20-%20Telecom%20Penetration.png" width=70%>

<small>Nombre de lignes pour 100 habitants, dans le monde
Source: [Measuring digital development (ITU)](https://www.itu.int/en/ITU-D/Statistics/Documents/facts/FactsFigures2019.pdf)
</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Des données de plus en plus échangées

Données échangées x3 tous les 4 ans

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/19-22-11-31-ITU%20-%20Broadband%20Usage.png" width=50%>

<small>400 000 Gbit/s = 40 kbit/s / personne = 120 kbit/s / personne sur 8h
Source: [Measuring digital development (ITU)](https://www.itu.int/en/ITU-D/Statistics/Documents/facts/FactsFigures2019.pdf)
</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Des données de plus en plus stockées

Données stockées x5 tous les 4 ans

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/19-16-48-00-IDC%20-%20Data%20Growth.png" width=60%>

<small>400 exaoctets = 400 millions de téraoctets = 40 Go / personne
40 000 exaoctets = 40 milliards de téraoctets = 4 To / personne
Source:[The Digital Universe in 2020 (IDC)](https://www.cs.princeton.edu/courses/archive/spring13/cos598C/idc-the-digital-universe-in-2020.pdf)
</small>

<!-- slide vertical=true data-background-color="#332222"-->

### Humains: sociétés linéaires

- Changements sociétaux à vitesse linéaire
- Déséquilibre croissant et risque de décrochage
- Maitriser beaucoup de données avec peu d'humains

<!-- slide vertical=true data-background-color="#332222"-->

#### Plus facile de déployer une technologie que de faire changer l'Humain

Le changement par le renouvellement de population

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/19-22-11-21-ITU%20-%20Telecom%20Coverage.png" width=70%>

<small>
Les taux de couverture télécom évoluent plus vite que l'usage d'internet.<br>
En 2019, 50% des gens couverts en 3G/4G n'utilisent pas internet.<br>
Levier principal de changement: le renouvellement de population.
</small>

<small>Source: [Measuring digital development (ITU)](https://www.itu.int/en/ITU-D/Statistics/Documents/facts/FactsFigures2019.pdf)</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Des difficultés à former la population

Croissance lente du nombre de technologistes

<div>
    <a href="https://plot.ly/~qchenevier/1/?share_key=7TfTNeCoVP31u145bzJoJF" title="Employed ICT specialists (Eurostat) (plot)" style="display: block; text-align: center;"><img src="https://plot.ly/~qchenevier/1.png?share_key=7TfTNeCoVP31u145bzJoJF" alt="Employed ICT specialists (Eurostat) (plot)" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="qchenevier:1" sharekey-plotly="7TfTNeCoVP31u145bzJoJF" src="https://plot.ly/embed.js" async></script>
</div>

<small>Les pros de l'IT ont l'habitude d'être courtisés car peu nombreux.
Source: [Employed ICT specialists (Eurostat by DB nomics)](https://db.nomics.world/Eurostat/isoc_sks_itspt?dimensions=%7B%22FREQ%22%3A%5B%22A%22%5D%2C%22geo%22%3A%5B%22FR%22%2C%22DE%22%2C%22IT%22%2C%22ES%22%2C%22UK%22%5D%2C%22unit%22%3A%5B%22PC_EMP%22%5D%7D&tab=chart)
</small>

<!-- slide vertical=true data-background-color="#332222"-->

#### Les données massives sont l'enjeu majeur

L'IT se met au cloud, au _big data_ et aux algorithmes

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/20-11-04-21-EMC%20-%20IT%20burden%20v2.png" width=70%>

<small>Les départements IT se dottent de nouvelles compétences
Source: [The Business Imperatives - EMC](https://www.emc.com/leadership/digital-universe/2014iview/business-imperatives.htm)</small>

<!-- slide data-background-color="#223322" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Black.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## L'évolution sociologique des organisations digitales

<!-- slide vertical=true data-background-color="#223322"-->

Efficacité d'une organisation = Qualité et Quantité des décisions qu'elle prend.

<!-- slide vertical=true data-background-color="#223322"-->

### Le délitement des hiérarchies 1.0

Le point-à-point ✉️ 📞
nécessitait une seule hiérarchie stricte

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/30-00-15-16-hierarchy.png" width=50%>
<img src="https://i.pinimg.com/736x/25/7e/23/257e233a5de62ef6a32a7319e508212f.jpg" width=46.6%>

<small>Source: [Heterarchies: Reconciling Networks and Hierarchies](https://www.sciencedirect.com/science/article/abs/pii/S016953471630043X)</small>

<!-- slide vertical=true data-background-color="#223322"-->

### L'avènement des hétérarchies 2.0

Le _one-to-many_ 💬📱
permet plusieurs circuits d'information

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/30-00-15-22-heterarchy.png" width=50%>
<img src="https://www.lesplumesdaudrey.fr/wp-content/uploads/2019/02/coworking-agora-berlin2-e1517234141501.jpg" width=47.1%>

<small>🤔&nbsp;mais le mail, _one-to-many_, n'a pas changé la hiérarchie en entreprise.<br> On n'écrit pas directement au CEO...
Source: [Heterarchies: Reconciling Networks and Hierarchies](https://www.sciencedirect.com/science/article/abs/pii/S016953471630043X)</small>

<!-- slide vertical=true data-background-color="#223322"-->

### L'émergence des organisations 3.0

L'IA devient une noeud intelligent du réseau

<img src="https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/30-11-05-53-AI%20organization.png" width=46%>
<img src="https://static01.nyt.com/images/2019/10/17/multimedia/17wheels-apps/merlin_139785978_bc2dfffc-4504-4e83-bde7-39a4d51b168d-articleLarge.jpg?quality=75&auto=webp&disable=upscale" width=51%>

<small>Source: [diagramme](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoiZ3JhcGggVEQ7XG4gIEFbQ0VPXVxuICBCW0TDqXZlbG9wcGV1cl1cbiAgQ1tEw6l2ZWxvcHBldXJdXG4gIERbRMOpdmVsb3BwZXVyXVxuICBFKChBcHBsaWNhdGlvbikpXG4gIEZbQWdlbnRdXG4gIEdbQWdlbnRdXG4gIEhbQWdlbnRdXG4gIElbQWdlbnRdXG4gIEpbQWdlbnRdXG4gIHN0eWxlIEUgZmlsbDojRjY2LCBzdHJva2Utd2lkdGg6MDtcbiAgQSAtLT4gQjtcbiAgQSAtLT4gQztcbiAgQSAtLT4gRDtcbiAgQiAtLT4gRTtcbiAgQyAtLT4gRTtcbiAgRCAtLT4gRTtcbiAgRSAtLT4gRjtcbiAgRSAtLT4gRztcbiAgRSAtLT4gSDtcbiAgRSAtLT4gSTtcbiAgRSAtLT4gSjsiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)</small>

<!-- slide vertical=true data-background-color="#223322"-->

### Le monde devient une organisation

> Smartphones had put a camera in everyone’s hand, and Twitter had created a real-time platform from which those photos and text updates could be instantly disseminated to the world. Billions of connected humans and devices were being woven into a global brain. **That brain was all of us, augmented and connected.**”

<small>Source: [WTF?: What's the Future and Why It's Up to Us (Tim O'Reilly)](https://www.goodreads.com/book/show/34017076-wtf)</small>

<!-- slide data-background-color="#223322" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Black.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## La digitalisation du contexte stratégique des organisations

<!-- slide vertical=true data-background-color="#223322"-->

### L'effet de réseau: externalité positive

Valeur proportionnelle au nombre de connexions au carré

<img src="https://www.researchgate.net/profile/Roberto_Moro_Visconti2/publication/331983003/figure/fig1/AS:743992551538689@1554393055115/Value-for-the-User-according-to-Metcalfes-Law.png" style="background-color:white;" width="80%">

<!-- slide vertical=true data-background-color="#223322"-->

### Marché instable

Externalités positives: dynamique "winner-takes-all".

![Tippy Market](https://upload.wikimedia.org/wikipedia/commons/9/9a/PositiveFeedback.JPG)

<small>Passer d'oligopoles stables à des monopoles temporaires</small>
<small>Source: [Network Externalities (wikibooks)](https://en.wikibooks.org/wiki/Strategy_for_Information_Markets/Network_Externalities)</small>

<!-- slide vertical=true data-background-color="#223322"-->

### La transition vers les services et les biens intangibles

Les business model intangibles sont plus performants pour **extraire de la valeur**

![MIT business model archetypes](https://i0.wp.com/getresults.org.uk/wp-content/uploads/2016/04/business_model_archetype-e1459864165186.jpg?resize=700%2C397)
<small>Source: [MIT business model investors prefer](https://sloanreview.mit.edu/article/the-business-models-investors-prefer/) et [Do Some Business Models Perform Better than Others?](http://ccs.mit.edu/papers/pdf/wp226.pdf)</small>

<!-- slide vertical=true data-background-color="#223322"-->

### La recherche de coûts marginaux proche de zero

![Marginal Cost for physical & digital business models](https://lh3.googleusercontent.com/TGOZqTd_nkmWxQx7F3FbDxEM_ujftnoKGrRiMkl0wC0mlMPV1Zs7c2Pk6yFUjQ30KxVGPefVJ8eHMCXKIU8nfDbgozGFV7iOVYxWCSHlSRRzI_XTfP_q4cJshpn_MzYSqgHx0dJe)

![Coût marginaux](https://2xawx0gmudy471po527lbxcd-wpengine.netdna-ssl.com/wp-content/uploads/2017/03/marginal-cost-curve.jpg)
<small> Source: [Marginal Cost (Near-Zero) Pricing is a Major App Provider Advantage (Gary Kim)](https://ipcarrier.blogspot.com/2019/05/marginal-cost-near-zero-pricing-is.html)
Source: [Platform vs. Linear: Business Models 101](https://www.applicoinc.com/blog/platform-vs-linear-business-models-101/)</small>
