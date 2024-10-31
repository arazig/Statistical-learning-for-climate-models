# Statistical learning for climate models
*Tony Lauze & Amine Razig*
------------------------------------

> **The purpose of this work is to see if learning methods, and more particularly methods using decision trees, can be more efficient than conventional linear models, for the prediction of gravity waves. First, we will present the database and the methodology used. Then we will report on the modeling tracks that have been discussed, and will highlight some results.**

Gravity waves - of which the waves on the surface of the sea are the simplest example - refer to the propagation of waves on the surface of a free fluid subjected to gravity. In the atmosphere, such waves can occur when a dense air flow is found, on the occasion of a collision on the side of a mountain - which gives rise to so-called orographic waves - or on the occasion of a convection movement - the waves are then called non-orographic -, projected at altitude above less dense layers of air. When the atmosphere is stable, i.e. when the density of the air decreases with altitude, an oscillation phenomenon can then be triggered, and the waves formed, gaining in amplitude as they propagate, then play a major role in circulation and atmospheric dynamics. Understanding these waves is essential for modeling climate phenomena.

<div style="text-align: center;">
    <img src="Figure 1.JPG" alt="onde" width="250" />
</div>

However, current climate models – such as those used by the European Centre for Medium-Range Weather Forecasts (ECMWF) – use in their simulations too wide a resolution to accurately model gravity waves, which take place on a small scale. For example, the ECMWF global forecasting model, the Integrated Forecasting System (IFS), has a horizontal resolution of 9 km. However, increasing the resolution of a numerical simulation model can be very costly computationally: doubling it can multiply the calculation time by sixteen.

This is why it may be wise to use other methods to model gravity waves. In recent years, there has been a boom in the use of machine learning to account for gravity waves from the outputs of climate models. For example, Chantry, Mathew et al. (2021) [2] use neural networks to accelerate the parameterization of gravity waves.

> See report of the project available in the directory:  [Séminaire_de_modélisation-2.pdf](Séminaire_de_modélisation-2.pdf)
### Table des matières

Introduction : les ondes de gravité 

I- Données et méthodologie

    1.1 Variable cible et variables explicatives.......................... page 2 
    1.2 Méthodologie ....................................... page 3
    
II- Modélisation et résultats
  
    2.1 Choix et description des modèles concurrents : Lasso, RandomForest, XGBoost, K-plusprochesvoisins .................................. page 4
    2.2 Performances des modèles ................................ page 6
    2.3 Importance de svariables................................. page 10
    2.4 Améliorer la prédiction.................................. page 11 
        2.4.1 Transformation logarithmique des variables. . . . . . . . . . . . . . . . . . . page 11 
        2.4.2 Ajout de retards dans les modèles........................ page 12
    
III- Conclusion
