
### 2019-05-10T13:45:30+02:00

Point avec Marwan:
- updater le fichier known_anomalies
- choisir les différentes options qu'on va tester:
  - histogram-based mono dimensional (not sequential)
  - autoencoder mono dimensional (not sequential)
  - autoencoder RNN multi dimensional (sequential)
  - sequential feature engineering (sliding-windows) + histogram-based
  - sequential feature engineering (sliding-windows) + autoencoder
- mettre en place les métriques d'évaluation:
  - unsupervised: AUC mass*volume
  - supervised: False positive / True Positive
