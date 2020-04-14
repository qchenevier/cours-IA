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

Le mariage de l'expérimentation et des statistiques:
Le savoir est extrait des données.

<img src="https://imgs.xkcd.com/comics/machine_learning_2x.png" width=40%>

<small>En bref, c'est de la cuisine avec des algorithmes
Source: [xkcd](https://xkcd.com/1838/)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Comment ça marche le _machine learning_

"Label" = information de valeur que l'on veut prédire.

<img src="https://qph.fs.quoracdn.net/main-qimg-ee5c644cf646c720a0961241b80a9b7c.webp">

<small>Il est impossible d'entraîner un algorithme sans une base de labels.
Source: [Quora](https://www.quora.com/What-deep-learning-method-to-use-to-classify-text-files)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Train-test split

<img src="https://elitedatascience.com/wp-content/uploads/2017/06/Train-Test-Split-Diagram.jpg" width=80%>

<small> Source: [Elite data science](https://elitedatascience.com/model-training)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### L'Overfitting: limitation majeure

Se "surajuster" aux données d'entraînement sans retenir le savoir sous-jacent (bachottage)

<img src="https://qph.fs.quoracdn.net/main-qimg-17ec84ff3f63f77f6b368f0eb6ef1890.webp" width=50%>
<img src="https://i.redd.it/ze7i4nhq0se41.jpg" width=40%>

<small>Cela fait croire qu'un modèle est performant (en laboratoire),
alors qu'il est médiocre (en conditions réelles).
[Démo (playground tensorflow)](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.03&regularizationRate=0&noise=25&networkShape=8,8&seed=0.10694&showTestData=false&discretize=false&percTrainData=20&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=false&problem=classification&initZero=false&hideText=false)<br>
Source: [Quora](https://www.quora.com/Is-it-possible-for-a-Machine-Learning-model-to-simultaneously-overfit-and-underfit-the-training-data)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Differentiable programming: Gradient descent & loss optimisation

Empilement de modèles différentiable et optimisation pour réduire l'erreur
[Démo: optimisation à la main](https://www.geogebra.org/m/xC6zq7Zv)

![](https://miro.medium.com/max/1414/1*IjxpxWcKX8EJUVFBNFeKdA.gif)

<small>Source: [Linear Regression by using Gradient Descent Algorithm: Your first step towards Machine Learning (medium)](https://medium.com/meta-design-ideas/linear-regression-by-using-gradient-descent-algorithm-your-first-step-towards-machine-learning-a9b9c0ec41b1)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Métriques

Attention aux évènements rares:

Pour prédire un évènement qui arrive 1% du temps, un modèle qui prédit tout le temps 0 aura raison 99% du temps !

Modèle simple (predit tout le temps)

<!-- slide vertical=true data-background-color="#222233"-->

### La révolution deep learning: plus de feature engineering

![](https://bluehexagon.ai/wp-content/uploads/2019/04/Screen-Shot-2019-04-04-at-1.05.20-PM-1024x600-1024x600.png)

<small>Source: [Blue Hexagon](https://bluehexagon.ai/blog/what-is-deep-learning-and-how-is-it-different-from-machine-learning/)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Comment ça marche le deep learning et ce qu'on peut faire avec

![](https://www.pnas.org/content/pnas/116/4/1074/F2.large.jpg?width=800&height=600&carousel=1)

<small>Source: [News Feature: What are the limits of deep learning? (PNAAS)](https://www.pnas.org/content/116/4/1074)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Etat de l'art computer vision

<!-- slide vertical=true data-background-color="#222233"-->

#### Etat de l'art natural language processing

<!-- slide vertical=true data-background-color="#222233"-->

#### Etat de l'art time series analytics

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Comment mener le projet ?

<!-- slide vertical=true data-background-color="#222233"-->

### qu'est-ce qui fait la valeur d'un projet ? Decision

📊 Information + ✋ Décision = 💰 Valeur

Cadre mental DPDV pour qualifier une idée:
Données → Produit → Décision → Valeur

<!-- slide vertical=true data-background-color="#222233"-->

| Données                   | Produit         | Décision                                               | Valeur       |
|:------------------------- |:--------------- |:------------------------------------------------------ |:------------ |
| Senseurs météo | Prévision Météo | Le citadin prend un parapluie avant de sortir          | ~ 0 €        |
| Senseurs météo | Prévision Météo | Le producteur de vin protège ses vignes avant la grèle | > 100 € / an |

<!-- slide vertical=true data-background-color="#222233"-->

| Données                                     | Produit                                         | Décision                                          | Valeur       |
|:------------------------------------------- |:----------------------------------------------- |:------------------------------------------------- |:------------ |
| Images satellites des réservoirs de pétrole | Estimation des réserves réelles de pétrole brut | Le trader achète ou vend du pétrole sur le marché | > 10M € / an |

<!-- slide vertical=true data-background-color="#222233"-->

### c'est quoi un projet IT Agile

- gérer l'incertain:
  - réévaluation fréquente du contexte: "les informaticiens ne font pas les choses parce qu'ils pensent que c'est faisable, mais parce qu'ils croient que c'est facile."
    - se concentrer sur la livraison de quelque chose d'utilisable pour apprendre, collecter des retours du terrain
  - replanification itérative:
  - intelligence collective
- loi des grands nombres pour le chiffrage

<!-- slide vertical=true data-background-color="#222233"-->

### c'est quoi un projet data science

- expérimentation: être prêt à payer pour voir (fail fast, learn quick)

<img src="https://theknowledgefactory.org/wp-content/uploads/2019/09/crispdm2.png" width=50%>

<small>Source: [CRISP-DM (Wikipedia)](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Qualifier une idée de projet

- se renseigner sur l'état de l'art: site paperswithcode

<img src="https://imgs.xkcd.com/comics/tasks_2x.png" width=30%>

<small>Source: [xkcd](https://xkcd.com/1425/)</small>

<!-- slide vertical=true data-background-color="#222233"-->

### Les clés de succès d'un projet IA

<!-- slide vertical=true data-background-color="#222233"-->

#### La donnée avant les algorithmes

~~algorithms~~ → datasets !
<img src="https://images.squarespace-cdn.com/content/54345ed8e4b0fa5705e1825b/1459449530701-68FQZ878JRPQCE97XVCC/AIBreakthrough.png?content-type=image%2Fpng" style="background-color:white;">

<small>Source: [Datasets Over Algorithms (kdnuggets)](https://www.kdnuggets.com/2016/05/datasets-over-algorithms.html)</small>

<!-- slide vertical=true data-background-color="#222233"-->

#### Tirer parti de l'open source

open competition: open source / open publication (model hubs, papers with code, etc.)

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Qui sait faire de l'IA ?

<!-- slide vertical=true data-background-color="#222233"-->

### c'est quoi un data scientist

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
    "text": "Les envies du data scientist face aux besoins projet",
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
    {"Activité": "Données", "Charge": 0.1, "rank": 1, "reality": "Envie", "opacity": 1},
    {"Activité": "Modèle", "Charge": 0.9, "rank": 2, "reality": "Envie", "opacity": 1},
    {"Activité": "Déploiement", "Charge": 0.1, "rank": 3, "reality": "Envie", "opacity": 1}
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

Les data scientists d'aujourd'hui ne sont pas autonomes pour livrer une solution

<!-- slide vertical=true data-background-color="#222233"-->

### Paysage des compétences à maitriser

- le background classique:

  - chercheur qui s'est reconverti
  - newbie qui sort d'école

- ce qu'il faut pour être un full stack data scientist (ou au moins comme compétences dans un projet)

<!-- slide data-background-color="#222233" data-background-video="https://github.com/qchenevier/public_images/raw/master/videos/Space.mp4" data-background-video-loop="loop" data-background-opacity=0.3-->

## Exercice
