
### 2018-06-06T10:36:17+02:00

Management meeting:

Opportunité

Operations en cours: contenu et staffing

Finances

Redescente d'informations stratégique:

- point clés: forecast de demande:
    - propale
    - predictabilité et reste à faire
    - renseignement
- obtenir des POs.

Jérôme GrandClaude ==> a recontacter pour parler de déploiement d'outil d'analyse de code.

Point par Charlotte:
- Point avec Luc Hennekens:
    - a propos de "move2east": c'est pas une fin en soi
    - On est partenaire: Airbus veut faire du make. D'égal à égal.
    - Débrider le cadre dans lequel on travaille.
        - Quels sont les obstacles à
        - Comment acquérir des talents, suivre les talents ?

- Revenir avec une propale d'université des skills rares

- Continuer le value assessment, de manière mensuelle.
    - Faire la démonstration qu'on finit au plus tôt les projets
    - Faire la démonstration de la business value des applis déployés

- Targetter la valeur plutôt que le volume

==> Coordination sur la valeur

- Dual Sourcing: a priori c'est plus trop à l'ordre du jour

- Communication croisée avec Airbus: une première (toujours refusé par Marc Fontaine)

Feature library ==> cadeau ==> reboucler sur la feature library
==> récupérer le code
==> remettre en place la logique d'enrichissement

Vente: Focus sur le Manufacturing, Procurement

### 2018-06-27T11:06:15+02:00

Business data science:

Share:
-	Revue des opports DS sur Airbus, Go/no
-	Priorités et modalités d’investissement
-	Actions de marketing
-	Info sur les recrutements en cours pour Toulouse

Revue des opportunités:
- DART
- QuART
- support consulting
==> manque de temps:
    delivery complexe sur PC-SPC
    recrutements

Ask:
- Est-ce qu'on a un trou d'air bientôt (j'ai pas l'impression)

Propose:
- Aller chercher des bigs fishs
==> démonstrateurs ?
==> ZOA ?

Plateau Zero AOG:
SPM:

Forum: Use-case of the future


Manufacturing

Qualité

Procurement:

PCT:
- montée en charge

PC-SPC:
- win agency sur les use-cases
- sur le monitoring de modèles

Strategy / :
- qui travaille sur quoi ?
- qu'est-ce qui vous empêche de dormir ?

Digital Design & Manufacturing: Jérôme Javelle.

Actions:

- Strategy
    - Proposer sujet avec CSM: Mieux faire du digital marketing: info ciblée, etc.
    - Identifier les besoins de la stratégie sur la stratégie produit.

- Manufacturing
    - Capitalisation sur la sûreté de fonctionnement
    - Video
    - Retour vers Arnaud De Coudenove ==> DX !
        Lean: actionable / rapide

    - Retour vers Chassagne

Recrutement:
    SHM / SPM: futurs besoins data science.
    ISWT DME
    Satair

### 2018-07-18T10:46:40+02:00

Management meeting:

Share:
- PC-SPC: on-boarding Clément Franger
- ISWT: experience in the making on NLP
- SCQWT: heard that they have trouble delivering quickly results using NLP, opportunity to send a message to show our strength
- Oasis: bad setup between local team & DTO: few chances to get the follow-up, but we'll try to get identified as experimented in data science
- Quality: hackathon / DART: 2 proposals pitched, will get back to them for feedback
- Support consulting: asking for experimented resource to start the activity on back-end

### 2018-09-11T16:19:26+02:00

Point avec Nicolas Boussuge:
- Comment relancer l'on-boarding sur Skywise.
- Problèmes de bonnes pratiques de code qui ne sont pas appliquées.

==> impliquer plus les lead techniques

### 2019-01-30T13:47:25+01:00

Point finance Skywise avec Hadi MAHIHENNI:

Skywise commercial: Aircraft-Skywise FollowUp-2019-v1.0.xlsx

2 cas de figure:
- continuer un job de 2018 de l'ancien outil sur le nouveau
- déclarer un nouveau job en 2019

exemple avec QuWT (projet démarré en 2018 pas encore déclaré sur l'outil - cas 1):
1. renseigner la propale: onglet jobs > aller dans la première ligne vide > remplir:
    - ID: nom de projet (⚠️ même valeur que "proposal unique identifier" dans le cartouche de la propale)
    - domaine
    - status
    - net fees (même approximatif)
    - proposal ref (⚠️ même valeur que ID)
    - start date & end date (⚠️ de là découle tout le staffing en fonction des fees)

1. renseigner le PO: onglet PO > remplir une ligne vide:
    - domain
    - Capgemini proposal (⚠️ même valeur que ID)
    - PO refernce (❓ mettre à "wait" si pas encore de PO)

1. faire le staffing "baseline" du job: onglet "Staffing per job - daily" > remplir des lignes vides dans la section Baseline avec:
    - ID du projet
    - Resource ID
        - ⚠️ menu déroulant se base sur l'onglet "Resources roster daily": si la ressource n'est dans la base: la créer dans cet onglet
        - ❓ si pas de ressource identifiée: prendre une ressource dont le nom commence par "xTemplate"
        - ⚠️ si ressource non-vendue: l'inclure dans la baseline avec 0% de charge (si t'es pas dans la baseline, tu peux pas être dans le revised)
    - pourcentage de charge (ça remplit automatiquement le staffing journalier baseline dans les colonnes de droite)

1. réviser le prix: onglet "DevisFlash_Job"
    - filtrer en haut à gauche sur le job ID
    - SL (Situation Latente) doit être >= 0
    - "CM Delivery" et "CM Delivery SL included" doivent être >= 54 %
    - print en pdf du devisflash pour validation

1. faire le staffing "revised" du job: onglet "Staffing per job - daily" > mettre à jour les colonnes de staffing journalier dans la section Revised avec le staffing réel
    - ⚠️ vérifier que la SL (Situation Latente) reste >= 0%
    - ⚠️ vérifier que la CM (Contrib Margin) SL included reste >= 54%

NB:
- on peut loguer une propale avant même que ça soit un projet lancé
- INTERDICTION DE RAJOUTER / INSERER / COPIER-COLLER DES LIGNES
- fichier partageable à partir du grade senior (junior c'est un peu tôt / compliqué)
- onglet "Formulas" > désactiver le calcul automatique pour éviter que ça rame & sauvegarder pour updater les calculs
- SL = Situation Latente = Budget - Cashback - Governance - Valo - Expenses
- CM = Contrib Margin
