---
title: IA & managers
presentation:
  theme: black.css
  enableSpeakerNotes: true
  maxScale: 0.8
  slideNumber: true
  previewLinks: true
---

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

# IA & managers

- Comment gérer un projet IA ? Quelles spécificités ?
- Comment intégrer l'IA dans mon processus ?

<!-- slide vertical=true data-background-color="#222233"-->

| Plage horaire | Atelier             |
|:-------------:|:------------------- |
| <small>08:00  | 🤔 Partie Théorique |
| <small>08:30  | ^                   |
| <small>09:00  | ^                   |
| <small>09:30  | ^                   |
| <small>10:00  | ☕️Pause             |
| <small>10:30  | 😅 Atelier pratique |
| <small>11:00  | ^                   |
| <small>11:30  | ^                   |

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

|||
|:--|:--|
| Modèle   |  <small><b>fait la prédiction</b><br>régression linéaire, réseau de neurones, ...</small> |
| Optimiseur   |  <small><b>modifie le modèle pour réduire son erreur</b><br>descente de gradient, algorithmes génétiques</small> |

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

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Demo time ! 🥳

<!-- slide data-background-color="#222233" vertical=true -->

### Echauffement: un neurone

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=gauss&regDataset=reg-gauss&learningRate=0.001&regularizationRate=0&noise=10&networkShape=&seed=0.81671&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### Cas simple: un neurone

Mauvaise performance ☹️

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.001&regularizationRate=0&noise=10&networkShape=&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### Cas simple: couche intermédiaire

Composition des neurones en rajoutant une couche:
Prédictions plus évoluées,
mais mauvaise performance ☹️

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0&noise=10&networkShape=2&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### Cas simple: couche + large

Rajouter des neurones:
Bonne performance 😊

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0&noise=10&networkShape=4&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### cas complexe

Un réseau simple ne fonctionne pas:
Mauvaise performance ☹️

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.1&regularizationRate=0&noise=10&networkShape=6&seed=0.47132&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### cas complexe: _Feature engineering_

Création manuelle de variables adaptées ✋,
en exploitant un savoir métier:
Prédictions suffisament précises 😊

L'ancienne méthode, efficace
mais coûteuse en temps de conception

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.03&regularizationRate=0&noise=10&networkShape=6&seed=0.47132&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=false&problem=classification&initZero=false&hideText=false" -->

<!-- slide data-background-color="#222233" vertical=true -->

### cas complexe: _Deep learning_

Composition de nombreuses couches:
Prédictions suffisament précises 😊
sans faire de _feature engineering_ manuel 😏

👉 Résolution de problèmes
à l'aide des données brutes,
sans savoir métier.

<!-- slide vertical=true data-background-iframe="https://playground.tensorflow.org/#activation=tanh&regularization=L2&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0.001&noise=10&networkShape=8,8,8,8&seed=0.67185&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false" -->

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

<img src="https://theknowledgefactory.org/wp-content/uploads/2019/09/crispdm2.png" width=45%>

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

Un mix entre business, statistiques et informatique

```vega-lite
{
  "config": {
    "background": "#333",
    "title": {"color": "#fff"},
    "style": {"guide-label": {"fill": "#fff"}, "guide-title": {"fill": "#fff"}},
    "axis": {"domainColor": "#fff", "gridColor": "#888", "tickColor": "#fff"}
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "title": {
    "text": "Appétences du data scientist et besoins projet",
    "fontSize": 30,
    "anchor": "middle",
    "offset": 20
  },
  "width": 450,
  "height": 200,
  "data": {"values": [
    {"Activité": "Données", "Charge": 0.9, "rank": 1, "reality": "Besoin", "opacity": 0.4},
    {"Activité": "Modèle", "Charge": 0.1, "rank": 2, "reality": "Besoin", "opacity": 0.4},
    {"Activité": "Déploiement", "Charge": 0.9, "rank": 3, "reality": "Besoin", "opacity": 0.4},
    {"Activité": "Données", "Charge": 0.1, "rank": 1, "reality": "Appétence", "opacity": 1},
    {"Activité": "Modèle", "Charge": 0.9, "rank": 2, "reality": "Appétence", "opacity": 1},
    {"Activité": "Déploiement", "Charge": 0.1, "rank": 3, "reality": "Appétence", "opacity": 1}
  ]},
  "mark": {
    "type": "bar"
  },
  "encoding": {
    "x": {
      "field": "Activité",
      "type": "nominal",
      "axis": {
        "labelFontSize": 30,
        "titleFontSize": 0,
        "labelAngle": 0
      },
      "sort": {"field": "rank"}
    },
    "y": {
      "field": "Charge",
      "type": "quantitative",
      "scale": {"domain": [0, 1]},
      "axis": {
        "labelFontSize": 30,
        "titleFontSize": 0,
        "tickCount": 0,
        "format": "%"
      }
    },
    "row": {
      "field": "reality",
      "type": "nominal",
      "title": "",
      "header": {
        "labelFontSize": 30,
        "labelAngle": 0,
        "labelAlign": "middle",
        "titleFontSize": 30
      }
    },
    "color": {
      "field": "Activité",
      "legend": null
    },
    "opacity": {
      "field": "opacity",
      "legend": null
    }
  }
}
```
<small>Beaucoup de data scientists ne pensent qu'aux algorithmes
et pas au problème qu'ils cherchent à résoudre.</small>

<!-- slide vertical=true data-background-color="#222233"-->

### La connaissance des algorithmes ne se suffit pas à elle-même

Un bon data scientist doit être full-stack developer,
ou être intégré à une équipe plus large.

![ML system infrastructure.png](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/11-13-30-59-ML%20system%20infrastructure.png)

<small>Faire du machine learning en laboratoire c'est facile,
mais savoir livrer une solution fonctionnelle est difficile.<br>
Source [Machine Learning: The High-Interest Credit Card of Technical Debt](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf)</small>

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Exercice

|||
|:--|:--|
|Secteur|<small>Choisir un secteur, choisir une entreprise emblématique</small>|
|Brainstorming|<small>En explorant les 3 values disciplines: brainstormer sur les idées de transformation IA qu'on peut proposer</small>|
|Valeur|<small>Evaluer la valeur en analysant les décisions améliorée par cette IA</small>|
|Faisabilité|<small>Evaluer la faisabilité en trouvant des exemples analogues</small>|
|Données|<small>Imaginer quand et comment on pourrait obtenir des données</small>|
|Pitch|<small>Pitcher</small>|
