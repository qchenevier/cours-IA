---
title: Annexes
presentation:
  theme: black.css
  enableSpeakerNotes: true
  maxScale: 0.8
  slideNumber: true
  previewLinks: true
---

<!-- slide -->

# Annexes

<!-- slide vertical=true-->

## Glossaire

- Devops
- Agile
- Data Scientist
- Machine Learning / Deep Learning
- Cloud
- API

<!-- slide vertical=true-->

## Contenu à placer:

- [Data Driven Think Again (Hackernoon)](https://hackernoon.com/data-inspired-5c78db3999b2) --> pour tirer parti de l'IA, il faut avoir une culture de la rationnalité et de la décision (citer [lettre aux actionnaire de Jeff Bezos en 1997](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm) sur les 2 types de décision et article de [business insider](https://www.businessinsider.fr/us/jeff-bezos-on-type-1-and-type-2-decisions-2016-4))
- Attention aux écueils: essayer de prédire la sexualité des gens à partir de leur visage: 2 critiques: [article medium](https://medium.com/@blaisea/do-algorithms-reveal-sexual-orientation-or-just-expose-our-stereotypes-d998fafdf477) et [article The Register](https://www.theregister.co.uk/2019/03/05/ai_gaydar/)
- ne vous méfiez pas de l'IA mais de ceux qui possèdent le pouvoir de créer/modifier l'IA: actionnaires & data scientists (citer [weapons of math destruction de Cathy O'Neil](https://www.goodreads.com/book/show/28186015-weapons-of-math-destruction))
- extraits de mon mémoire de MBA:
  - les 8 compétences clés dans le futur

<!-- slide vertical=true-->

## Demos / Manips

- Tensorflow playground:
  - [cas très simple: un neurone suffit](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=gauss&regDataset=reg-gauss&learningRate=0.001&regularizationRate=0&noise=10&networkShape=&seed=0.81671&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas simple: un neurone ne suffit plus](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.001&regularizationRate=0&noise=10&networkShape=&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas simple: une couche en plus, on voit le début de la composition, mais c'est pas suffisant](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0&noise=10&networkShape=2&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas simple: une couche plus large, ça fonctionne](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=xor&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0&noise=10&networkShape=4&seed=0.20315&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas complexe: un réseau simple, ne fonctionne plus](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.1&regularizationRate=0&noise=10&networkShape=6&seed=0.47132&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas complexe: feature engineering: ça marche en donnant des données plus complexes au réseau](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.03&regularizationRate=0&noise=10&networkShape=6&seed=0.47132&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=true&xSquared=true&ySquared=true&cosX=false&sinX=true&cosY=false&sinY=true&collectStats=false&problem=classification&initZero=false&hideText=false)
  - [cas complexe: deep learning: plus besoin de faire du feature engineering](https://playground.tensorflow.org/#activation=tanh&regularization=L2&batchSize=10&dataset=spiral&regDataset=reg-gauss&learningRate=0.01&regularizationRate=0.001&noise=10&networkShape=8,8,8,8&seed=0.67185&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

<!-- slide -->

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

<!-- slide vertical=true-->

- Other deep learning:
  - [GitHub - NVlabs/stylegan2: StyleGAN2 - Official TensorFlow Implementation](https://github.com/NVlabs/stylegan2)
- Tensorflow js demos:
  - [Boston Housin with tfjs](https://storage.googleapis.com/tfjs-examples/boston-housing/dist/index.html)
  - [MNIST in TensorFlow.js Layers API](https://storage.googleapis.com/tfjs-examples/mnist/dist/index.html)
  - [Webcam Pacman](https://storage.googleapis.com/tfjs-examples/webcam-transfer-learning/dist/index.html)
  - [RNN text generation](https://storage.googleapis.com/tfjs-examples/lstm-text-generation/dist/index.html)
  - [BodyPix - With a Webcam Demo](https://storage.googleapis.com/tfjs-models/demos/body-pix/index.html)
  - [Disappearing People - Person removal from complex backgrounds over time](https://glitch.com/~disappearing-people)
  - [Shader - Eye laser](https://shaderbooth.com/?85daa)
- NLP:
  - [Stanford Named Entity Tagger](http://nlp.stanford.edu:8080/ner/process)
  - [Dandelion Named Entity Tagger](https://dandelion.eu/semantic-text/entity-extraction-demo/?text=Barack+Hussein+Obama+II+is+an+American+attorney+and+politician+who+served+as+the+44th+president+of+the+United+States+from+2009+to+2017.+A+member+of+the+Democratic+Party%2C+he+was+the+first+African+American+president+of+the+United+States.+He+previously+served+as+a+U.S.+senator+from+Illinois+from+2005+to+2008+and+an+Illinois+state+senator+from+1997+to+2004.&lang=auto&min_confidence=0.6&exec=true#results)

<!-- slide vertical=true-->

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

<!-- slide vertical=true-->

## Links

- [Future of jobs - World Economic Forum](http://www3.weforum.org/docs/WEF_Future_of_Jobs_2018.pdf)
- [Prediction Machines (book)](https://www.predictionmachines.ai/)
- [Human + Machine (book)](https://www.goodreads.com/book/show/36465763-human-machine)
- [A new kind of growth for europe - Xynteo](https://xynteo.com/sites/default/files/download/2019/10/XT0330_ED_Report1_V2_SCREEN.pdf)
- [Artificial Intelligence for the real world - HBR](https://hbr.org/2018/01/artificial-intelligence-for-the-real-world)
- [The Latest Research: AI & Machine Learning - HBR](https://store.hbr.org/product/the-latest-research-ai-and-machine-learning/ARTINT)
- [Agile Machine Learning: from theory to production - Rob Hinds' talk @JAXLondon2017](https://www.slideshare.net/robhinds/jaxlondon2017-agile-machine-learning-from-theory-to-production)
- [Machine Learning: The High-Interest Credit Card of Technical Debt](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/43146.pdf)

![ML system infrastructure.png](https://raw.githubusercontent.com/qchenevier/public_images/master/2020/03/11-13-30-59-ML%20system%20infrastructure.png)

<small>Source: [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)</small>
