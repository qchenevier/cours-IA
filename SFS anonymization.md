
### 2018-12-20T17:08:12+01:00

Point avec:
- Emmanuel Vigreux:
    - Ingestion
    - Data gouvernance avec data officer
- Christophe Regouby: Advanced Analytics DTO:
    - Mise en place pipeline anonymisation tech requests (repair dossiers) pour Smart Repair Wizard
    - Mise en place d'une solution End2End avec une startup: Anonymisation, Extraction Entité Nommées avec labellisation
- Quentin Chenevier

Anonymisation déjà faite sur NC pour partage avec Thales

- Conception par Christophe Regouby
- Mise en prod par Julien Etieve (dans équipe de Stéphane Raymond) ==> sur Foundry ou sur COP

- java: Stanford.CoreNLP ==> CRF:
    - sort un fichier jz (paramètres du modèle serialisé) qui est exploitable sur Foundry et COP

DPO (Data Protection Officer):
- pour avoir un Go: accuracy en F2-score (plus de poids sur le recall) supérieure à au moins 95 %:
    - person name
    - organisation
    - phone number
    - mail
==> équipe Pierre PICQ (HAL - Legal)

- annoter à la main un dataset: "golden dataset": experts humains
    - echantillonnage représentatif
    - annoter à la main par des experts qualité:

REX: NC
- en prenant 3 sources seulement (sur 32 datasets différents), c'était pas suffisant. ==> donc attention au scoping et à l'annotation
- volume golden dataset (train + test set):
    - 39000 personnes
    - 1000 team id
    - pas d'organisations ==> pas besoin
    - 19000 token phone number (ce qui represente entre 5000 et 10000)

- test set:
    - 300 personnes: login (TO...), nom SAP,
    - 320 team ID
    - 761 organisations ==> dûe aux bas de pages
    - 460 token phone number (200)

- annotation pendant une journée avec des experts
- de manière colocalisée pour le partage d'info
- outil d'annotation ?
    - gate.co.uk
    - demander à Benjamin Roussel son outil qui a l'air assez bien foutu

Scope:
- NC: vérifier le statut avec Guillaume mais a priori c'est en cours de mise en prod.
- TLB: réutiliser le modèle de Christophe Regouby

Contenu des données TLB:
- fournisseurs
- prod airbus

Attention: Data officer TLB: Pascal FOUILLANT (chez B).

TODO QC:
- récupérer liste datasets anonymisés auprès d'Emmanuel
- pour l'ontologie: voir http://datalab-wiki.eu.airbus.corp: PII & Business Object Ontologies
- voir si on peut récupérer des annotateurs: Cap: qui ont bossé à:
    - essais en vol
    - flight line
    - delivery center
- prendre contact avec Julien Etieve pour avoir un statut sur le pipeline sur les NC.
- contacter Benjamin Roussel sur l'outil d'annotation (LEO).
- contacter Guillaume Poirier pour évaluer la charge de la session d'annotation.

### 2019-01-03T12:33:08+01:00

Anonymisation:
- modèle / implémentation:
    - étudier implémentation actuelle: contact Julien ETIEVE / Quentin AMIRAULT
    - chiffrer le temps d'implémentation dans foundry
    - étudier les ontologies définies sur le wiki du datalab

- data:
    - benchmarker outils d'implémentation: contact: Benjamin ROUSSEL (outil LEO)
    - évaluer charge d'annotation: contact Guillaume POIRIER + éval grossière si pas dispo
    - demander samples de données: samples tech request annotées ==> quel format ? contact Christophe REGOUBY
    - trouver experts capables d'annoter les TLB chez CAP: contact Eric FOCH

- Propale:
    - ???

### 2019-01-03T14:08:59+01:00

Réunion avec Pascal FOUILLAND: Data officer "programme" (B)
- homologue de Guillaume POIRIER

QLB: Guillaume POIRIER
TLB: Pascal FOUILLAND

Meeting avec Airbus India en parallele.

Golden dataset:
- _Organisation_ et _Team ID_ à taguer en PII, mais pas besoin d'anonymiser
- _PersonName_, _Email_, _TelNumber_, _UserId_ a anonymiser

Continuer à chercher des annotateurs.

LEA text-annotator.lea.bocacc.io:
- input:
- output: format

Dataset foundry:
vw_qa_logbook_snag_***

Texte:

Données PII à supprimer:
    A anonymiser, colonnes de texte:
    - snag_job_description
    - snag_cor_action

    A supprimer: colonnes structurées
    - snag_cor_action
    - dept_snag_creation (à cause des stamps dedans)

    A statuer:
    - colonnes qui ressemblent à du texte

Tagueurs:
- Didier DUMONT
- Mathieu LANDMAN
- Pascal FOUILLAND
- Annotateurs cap'

Confirmer si l'outil LEA c'est bon.

- Contacter Alexandre Arnold, Nicolas Schneider & Gérard Dupont pour vérifier que LEA text-annotator permet de faire l'annotation
