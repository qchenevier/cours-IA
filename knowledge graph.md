
### 2019-01-16T16:16:00+01:00

GraphX / GraphFrames

Alexandre Desroques:
- graphX tourne sur Foundry
- API java pose un certains nombre de problèmes
- pas de benchmark en perfo:
    - pas eu le temps de faire tourner
    - pas forcément représentatif: données d'entrée dans le pipeline, très différente d'un graphe

pb rencontrés par Alexandre:
- découverte de la lib
- adaptation de l'API - graphX
- manque de temps

- graphframes:
    - pas installé
    - test avec graphX

- construction des paths
- export

url: XBOM / repertoire "Alexandre files".

En gros: trade-off entre:
- graphx:
    - composant natif 😄
    - testé à 80 % par alexandre 😄
    - en java 😞
    - sur des RDD 😞
- graphframes:
    - dispo 3 langages (python, scala, java) 😄
    - sur des dataframes 😄
    - doit être packagé dans conda pour installation sur Foundry 😞
    - testé à 0 % 😞

### 2019-01-17T14:08:01+01:00

GraphX - pregel

Connait mal la structure de données
Implémentation bête et méchante pour coller à l'implémentation existante

Pire des 2 mondes:
- java en scala. implémentation de fonctions anonymes dans des classes.
- code lourd: pregel et graphX.
- data lourd: tabulaires au lieu d'un data model graphe optimisé.

==> souvent pb de mémoire sur le pipe implémenté

pour l'instant: le pipe tourne mais le dataset de sortie est vide.

GraphFrames:
- API python
- ne supporte pas pregel ==> optimisation

### 2019-02-22T15:15:34+01:00

Skywise graph for XBOM
- Neo4j
- Neptune
- pour XBOM: ZIPA a demandé une étude sur quelle serait la bonne solution technique
- trade-off entre:
  - lib graph sur Foundry: graphX, GraphFrames
  - database graph: neptune, neo4j

### 2019-07-09T14:24:51+02:00

Point Knowledge Graph avec:
- Nicolas PLATTEAU
- Hadi MAHIHENNI
- Stéphane BIARD
- Ludovic FARNAUD (Airbus)



- base neo4j
- graphX
- Hubble
- tables


Ludovic
- pote avec Florent BOUIX
- Value Stream: PLM, Stress Data

Equipe Airframe Data Analytics:

Benchmark: Neo4j vs Marklogic
