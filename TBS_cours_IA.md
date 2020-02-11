---
title: IA for managers
---

# Content

## Introduction

- https://xkcd.com/1425/

## Contexte

### Glossaire

- Devops / Continuous Integration
- Agile
- Data Scientist
- Machine Learning / Deep Learning

### Technologie & Société

#### Technological revolution & media revolution:

- History of technological revolutions (carlota perez): we live a new industrial revolution:
  - la révolution digitale arrive après le charbon, l'électricité, le pétrole, ...
- Media revolution: (voir intro de "program or be programmed" de Douglas rushkoff)
  - la révolution digitale arrive après l'alphabet, l'imprimerie, les télécoms analogiques (TV = "broadcast", téléphone = "point à point"), ...

#### IT & AI dans la société:

- salaire moyen d'un devops / data scientist dans le monde
- combien d'IT specialist et de data scientists par rapport à la population ?
- ne vous méfiez pas de l'IA mais de ceux qui possèdent le pouvoir de créer/modifier l'IA: actionnaires & data scientists

### History of digitalization: exponential laws and constant acceleration...

- moore law: [article sur le sujet à lire](https://www.nextplatform.com/2019/02/05/the-era-of-general-purpose-computers-is-ending/)
- penetration of technologies
- [number of processors / transistors](https://www.darrinqualman.com/global-production-transistors/)
- number of telecoms / available broadband
- number of websites

### History of AI:

- [timeline](http://digitalintelligencetoday.com/wp-content/uploads/2017/08/Artificial-Intelligence-AI-Timeline-Infographic.pdf)

- état de l'art suivant X domaines:
  
  - computer vision
  - natural language processing
  - time series analytics
  - ??

- La révolution deep learning → plus de feature engineering

- Pourquoi l'IA progresse si vite
  
  - ~~algorithms~~ → datasets ! (voir article [Datasets Over Algorithms](https://www.kdnuggets.com/2016/05/datasets-over-algorithms.html))
    
    ![Datasets over Algorithms](https://images.squarespace-cdn.com/content/54345ed8e4b0fa5705e1825b/1459449530701-68FQZ878JRPQCE97XVCC/AIBreakthrough.png?content-type=image%2Fpng)
  
  - open competition: open source / open publication (model hubs, papers with code, etc.):
  
  - Révolution en marche (extrait rapport [AI index](https://hai.stanford.edu/sites/g/files/sbiybj10986/f/ai_index_2019_report.pdf)):
    
    - nombre de publications deep learning
      
      ![AI papers on Arxiv](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/11-22-27-46-AI_papers_arxiv_2010_2019.png)
    
    - nombre de participants aux conférences deep learning
      
      ![AI conferences attendance](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/11-22-16-53-AI_conferences_attendance_1985_2019.png)
    
    - nombre de jobs de machine learning aux US (répartition inégale !)
      
      ![AI jobs](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/02/11-22-45-29-AI_jobs_per_industry_2010_2019.png)
    
    - IA qui bat les humains (voir rapport AI index ou plus d'infos sur cette [page de l'EFF](https://www.eff.org/ai/metrics))

| Année | Activité                                                                                                                                                 |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1980  | Othello                                                                                                                                                  |
| 1995  | Dames                                                                                                                                                    |
| 1997  | Echecs                                                                                                                                                   |
| 2011  | Jeopardy!                                                                                                                                                |
| 2015  | Jeux Atari                                                                                                                                               |
| 2016  | - Classification d'objets sur ImageNet<br/>- Go (AlphaGo)                                                                                                |
| 2017  | - Classification du cancer de la peau<br/>- Reconnaissance vocal sur Switchboard<br/>- Poker<br/>- Pac-Man                                               |
| 2018  | - Traduction Chinois-Anglais<br/>- Quake 3: Capture the flag<br/>- DOTA2<br/>- Classification du cancer de la prostate<br/>- Protein Folding (Alphafold) |
| 2019  | - Starcraft II (AlphaStar)<br/>- Diagnostic de la rétinopathie diabétique                                                                                |

- transition to services: voir [article](https://www.atys-concept.com/blog-de-la-performance/articles-performance-industrielle/iaas-paas-saas-modele-cloud-choisir-solutions-de-performance-industrielle/)
  
  - SaaS
  - PaaS
  - IaaS

- Demain: la singularité ? Débat
  
  - Pour: Ray Kurzweil - The Singularity is near
  
  ![](https://28oa9i1t08037ue3m1l0i861-wpengine.netdna-ssl.com/wp-content/uploads/2015/01/Howard-Graph.png)
  
  - Contre: François Chollet [The Impossibility of Intelligence Explosion (François Chollet)](https://medium.com/@francois.chollet/the-impossibility-of-intelligence-explosion-5be4a9eda6ec), etc.

### Business analysis Framework:

- 3 value disciplines (Treacy):
  - customer intimacy
  - product leadership
  - operational excellence
- tech companies paradigm ([article Nicolas Colin](https://salon.thefamily.co/whats-a-tech-company-515960d76c21)):
  - increasing returns
  - exceptional user experience
  - regular & systematic collection of user-generated data
- en quoi l'IA et le digital ont permis à certaines compagnies de surclasser les autres
- une vision de nos organisations: (à mettre dans [technologie et société](#technologie&société))
  - d'abord stratifiées
  - maintenant en réseaux
  - structurées par des algo / apps
- exercices:
  - étude de cas:
    - amazon vs wallmart
    - spaceX vs arianegroup
    - tesla vs GM
  - étude de cas par secteur
  - construire une vision à 10 ans:
    - à l'échelle macro
    - à l'échelle micro
    - comment s'y préparer
    - premières actions
- Articles à citer:
  - [Data Driven Think Again (Hackernoon)](https://hackernoon.com/data-inspired-5c78db3999b2)
  - Attention aux écueils: essayer de prédire la sexualité des gens à partir de leur visage: 2 critiques: [article medium](https://medium.com/@blaisea/do-algorithms-reveal-sexual-orientation-or-just-expose-our-stereotypes-d998fafdf477) et [article The Register](https://www.theregister.co.uk/2019/03/05/ai_gaydar/)

### C'est quoi l'IA:

WIP

# Demos / Manips

- Demos repositories:
  - [AI Experiments | Experiments with Google](https://experiments.withgoogle.com/collection/ai)
  - [tensorflow.js examples](https://github.com/tensorflow/tfjs-examples/)
- Google AI experiments:
  - [Teachable Machine](https://teachablemachine.withgoogle.com/)
  - [Melody Mixer](https://experiments.withgoogle.com/ai/melody-mixer/view/)
  - [Beat Blender](https://experiments.withgoogle.com/ai/beat-blender/view/)
  - [Sound Maker](https://experiments.withgoogle.com/ai/sound-maker/view/)
  - [Thing Translator](https://thing-translator.appspot.com/)
  - [Quick Draw](https://quickdraw.withgoogle.com/)
- Other deep learning:
  - [GitHub - NVlabs/stylegan2: StyleGAN2 - Official TensorFlow Implementation](https://github.com/NVlabs/stylegan2)
- Tensorflow js demos:
  - [Boston Housin with tfjs](https://storage.googleapis.com/tfjs-examples/boston-housing/dist/index.html)
  - [MNIST in TensorFlow.js Layers API](https://storage.googleapis.com/tfjs-examples/mnist/dist/index.html)
  - [Webcam Pacman](https://storage.googleapis.com/tfjs-examples/webcam-transfer-learning/dist/index.html)
  - [RNN text generation](https://storage.googleapis.com/tfjs-examples/lstm-text-generation/dist/index.html)
  - [BodyPix - With a Webcam Demo](https://storage.googleapis.com/tfjs-models/demos/body-pix/index.html)
- NLP:
  - [Stanford Named Entity Tagger](http://nlp.stanford.edu:8080/ner/process)
  - [Dandelion Named Entity Tagger](https://dandelion.eu/semantic-text/entity-extraction-demo/?text=Barack+Hussein+Obama+II+is+an+American+attorney+and+politician+who+served+as+the+44th+president+of+the+United+States+from+2009+to+2017.+A+member+of+the+Democratic+Party%2C+he+was+the+first+African+American+president+of+the+United+States.+He+previously+served+as+a+U.S.+senator+from+Illinois+from+2005+to+2008+and+an+Illinois+state+senator+from+1997+to+2004.&lang=auto&min_confidence=0.6&exec=true#results)
- Linear regression:
  - [GeoGebra demo](https://www.geogebra.org/m/xC6zq7Zv)
- Spreadsheet tutorial:
  - Boston House Price Dataset:
    - [House Prices: Advanced Regression Techniques | Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
    - [Comprehensive data exploration with Python | Kaggle](https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python)
  - [Statistics for Google Sheets](https://sites.google.com/site/statisticsforspreadsheets/)
    - Summarize a single variable
    - Summarize the relationships between pairs of variables
    - Fit (and critique) a regression model.
- automl H20

# Objectifs de formation

- toucher du doigt et comprendre ce qu'est l'IA
- savoir gérer un projet IA dans son entreprise
- savoir anticiper l'impact de l'IA à moyen-terme dans la société
- anticiper la transformation de son entreprise avec l'IA

# Profils visés

- Public cible: managers
  - techniques / pas techniques (niveau de technicité)
  - PME / grands groupes ? (contexte d'évolution)
  - hands-on & doer (aime bien les manips) ou parleur (étude de cas)
- Tout le monde:
  - Qu'est-ce que l'IA ?
  - IA et travail: comment l'IA est en train de changer le monde du travail ?
  - IA et société/gouvernement: enjeux éthiques autour de l'IA
- Project Manager:
  - Comment gérer un projet IA ? Quelles spécificités ?
  - Comment intégrer l'IA dans mon processus ?
- Strategist / CEO:
  - Quelles tendances doit-on anticiper ?
  - Comment dois-je transformer mon entreprise ? Quel type d'organisation dois-je mettre en place pour tirer parti de l'IA dans mon entreprise ?
    - dans une PME ?
    - dans un grand groupe ?

# Planning type & liste d'activités

## Liste d'activités

- Introduction
  - Accueil
  - Collecte attentes élèves
  - Présentation des objectifs & profils cibles
  - Présentation Plan
  - Ice-breaker: petite démo
- IA pour le citoyen
  - Démo:
- IA pour le CEO:
  - Case study: expliquer le passé: analyse comparative & disruption:
    - Couples:
      - Amazon ↔ Walmart, Carrefour, ...
      - SpaceX ↔ Boeing, Arianespace, ...
      - Tesla ↔ GMC, Renault, ...
      - AirBnB ↔ Accor
      - Uber ↔ Taxis
      - Kiwi ↔ Air France
      - BlaBlaCar ↔ SNCF, Bus, ...
      - Pixar ↔ Film studios
    - Axes d'analyse
      - selon quelles dimensions
      - avec quelles technologies ?
  - Case study: prédire le futur: prendre une compagnie emblématique, leader de son industrie et prédire où elle sera dans 10 ans
    - Trouver des ordres de grandeur de changement technologiques dans 10 ans
    - Appliquer les bons changements d'ordres de grandeur pour faire un scenario d'évolution de la boîte
    - Penser quelles sont les actions que doit mettre en place en premier cette compagnie, dès aujourd'hui
- IA pour le manager:
- 
- Démo:

## Planning

| Demi-journée                           | Plage horaire |                                                                                                                                                      |
|:--------------------------------------:|:-------------:| ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span style="color: red">1</span>      | 08 - 09       | - Accueil<br/>- Collecte attentes élèves<br/>- Présentation des objectifs & profils cibles<br/>- Présentation du plan<br/>- Ice-Breaker: petite démo |
| <span style="color: red">1</span>      | 09 - 10       | IA dans la société                                                                                                                                   |
| <span style="color: red">1</span>      | 10 - 11       |                                                                                                                                                      |
| <span style="color: red">1</span>      | 11 - 12       | - Débat-Réflexion sur l'IA dans la société                                                                                                           |
| <span style="color:darkgreen">2</span> | 14 - 15       |                                                                                                                                                      |
| <span style="color:darkgreen">2</span> | 15 - 16       |                                                                                                                                                      |
| <span style="color:darkgreen">2</span> | 16 - 17       |                                                                                                                                                      |
| <span style="color:darkgreen">2</span> | 17 - 18       |                                                                                                                                                      |
| <span style="color:lightblue">3</span> | 08 - 09       |                                                                                                                                                      |
| <span style="color:lightblue">3</span> | 09 - 10       |                                                                                                                                                      |
| <span style="color:lightblue">3</span> | 10 - 11       |                                                                                                                                                      |
| <span style="color:lightblue">3</span> | 11 - 12       |                                                                                                                                                      |
