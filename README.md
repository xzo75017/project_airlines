


# I Objectif du projet Airline

Permettre à un utilisateur souhaitant partir en voyage d'avoir accès aux événements du pays en lui proposant un billet d'avion à destination de ce pays  


# II Architecture du projet 

Le projet va s'articuler de la manière suivante comme l'indique le diagramme ci-dessous : 


![Diagram_DST drawio (1)](https://user-images.githubusercontent.com/63191063/196041099-d75d486c-932e-4600-838e-e5af91849923.png)



# III Etapes du projet 

## 1. Extraction des données 


- Prise en main de FlightAPI (```https://www.flightapi.io/```) et Allevents (```https://allevents.in```) (création de compte, requêtage des différentes routes et comparaison des données retournées).
- Requêtage des données sur 3 endpoints :
 ```bash
     /onewaytrip/YOURAPIKEY/LHR/LAX/2019-10-11/2/0/1/Economy/USD
     /iata/api-key?name=american&type=airline
     /roundtrip/YOURAPIKEY/LHR/LAX/2019-10-11/2019-10-15/2/0/1/Economy/USD
```
- Utilisation de la classe ```BeautifulSoup()``` de la librairie ```bs4``` pour webscraper la page Allevents  en langage Python (version ```Python 3.10.7```)

- Récupération des cityCode de chaque ville sur le site ``` https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm``` pour effectuer les requêtes sur FlightAPI
- 
    - Technique de webscraping non réalisable car le site est protégé contre les bots
         - Isertion des données dans un fichier txt
         
- Résultats du webscraping 

Allevents :

 - Dataframe  

![image](https://user-images.githubusercontent.com/63191063/196368520-2d6dce0c-8195-48c5-b20b-3754d470492a.png)

 - JSON : 

![Capture3](https://user-images.githubusercontent.com/63191063/196041997-568bb682-018a-4970-8ff8-5dd928043565.PNG)

- Résutat de la requête pour flightAPI: 

FlightAPI : 

![Capture4](https://user-images.githubusercontent.com/63191063/196042082-59bfee7d-2001-4adf-a541-c3ec6fa744b2.PNG)


PriceFlightAPI :

![Capture2](https://user-images.githubusercontent.com/63191063/196041576-29086a1a-6937-4de8-b870-54e367c3b532.PNG)


AirportCodeAPI : 

![Capture](https://user-images.githubusercontent.com/63191063/196041376-0aeb8bdb-41f5-473c-82c2-941cbb834412.PNG)


## 2. Organisation de la base de donnée
   
 
 
  ### 2.1  Traitement des données en utilisant le NoSQL (MongoDB) : 



- Besoin d'information sur les vols, les prix, les aéroports, les compagnie aérienne
   - Stocker les informations sur MongoDB sous forme de collections:
       - Formats différents pour les données bruts notamment Airport et Airline (éviter les doublons)
        - Historiser les données dans MongoDB 
        - Capacité de stockage importante sur MongoDB 
    - Avant cette étape :

        - Sélection des fichiers JSON représentant les futures collections (récupération des données utilisées pour le projet):

          
             ```Vol ```

            ```Price```

            ```Airline```

            ```Airport```

            ```evenement```
        - Besoin de relier les futures collections entre elles:
            - Uniformisation de l'ID:

             ex  id de vol : ```LHR-LAX:BA5951~11:BA6123~11:0" ``` et de price ex : ```a6fca0f2a8a3e4f3msr:BA5951~11-BA6123~11``` en ```BA5951~11-BA6123~11 ```
            -  Selection des variables 
             Sélections de 9 variables sur les 30 présentes dans la collection ```Vol``` :

            ```departureTime```

            ```arrivalTime```

            ```duration```

             ```departureAirportCode```

            ```arrivalAirportCode```

             ```airlineCodes```

            ```departureDate```

             ```arrivalDate```

        
           - Sélection des variables suivantes pour la collection ```Price```:

           ```totalAmount```

          ```amountPerAdult```

          ```amountPerChild```

          ```amountPerInfant```

          - Sélection des variables suivantes pour la collection ```Airline```:

           - code de la compagnie aérienne ex : ```AF```
           - nom de la compagnie aérienne ex : ```Air France```

          - Sélection des variables suivantes pour la collection ```Airport```:

           - code de la compagnie aérienne ex : ```CDG```
           - nom de la compagnie aérienne ex : ```Charles de Gaulle```
        
         - Stocker les informations sur MongoDB sous forme de collections
            - Connexion au MongoDB :  ```client = MongoClient("mongodb+srv://DST-PROJECT:DST@cluster0.7wo11db.mongodb.net/?retryWrites=true&w=majority```
             -  Créations des collections (récupération des données utilisées pour le projet):

             
                  ```Vol ```


                 ```Price ```

                 ```Airline```

                 ```Airport```

                 ```evenement ``` 
                 
              - Visualisation du cluster : 
              
              
                 
 ### 2.2 Traitement des données en utilisant une base de donnée SQL 
   -  Tableau d'information sur le vol et les évènements : nécessité schéma fixe
   
   - Dans  le cas du SQL (SQLite soucis de rapidité, dans un vrai contexte un vrais SGBD MySQL) :
      - Nécessité de laisser les tables disjoinctes car les données provenant de MongoDB ont des structures différentes :
        - Collection Vol et Prix :  1 destination  = 200 vols 
        - Collection évènement : 1 clé = 1 évènement
        - Collection Airlines et Airport : 1 code aéroport = 1 nom aéroport


      - - Transformation des données sous le meme format que airline et airport
      -  création d'une table concernant les villes et leur code IATA pour obtenir le cityCode de chaque ville
      
      
      
      
      
          - Connexion + création d'une base de données sqlite :``` create_engine('sqlite:///travel.db', echo = True)``` 
           - Créations des tables  (récupération des données utilisées pour le projet):

              ```Vol ```

             ```Price ```

             ```Airline```

             ```Airport```

             ```evenement ``` 
        - Insertion des données SQL dans SQLite :  ``` INSERT OR REPLACE INTO Events VALUES ({markers}) ```
        - Affichage de la Jointure des table dans la base de donnée SQL pour obtenir une table résultante contenant les informations sur les vols, les prix, la destination et les activités:
                ```  SELECT ... INNER JOIN ... ON ...  ```
            
## 3. Consommation des données 

 


### 3.1 Création d'une application Dash
  - Affichage de la table jointe sur DASH
   
    - Représentation du Dash lors de son lancement : 
    ![unknown](https://user-images.githubusercontent.com/63191063/197458195-98739f2d-8253-42bb-8621-a7dd912edd1e.png)
    #### 3.1.1 Lancement d'un évènement sous Dash
    
     -  L'utilisateur sélectionne la ville d'arrivée + dates pour les évènements puis le Dash va récupérer les données de vol pour cette ville puis affiche les données de Vol dans Dash:
     
     ![unknown](https://user-images.githubusercontent.com/63191063/197458468-8e0f74cb-b3f8-4db0-bef5-b5b8b7bd2c87.png)

     - Lancement du programme "Trouver des evenements"
       - Récupération de la ville et des dates dans le SQL
         - ```If``` ville présente dans la table SQL ou que ça fait moins de 7j (choix du nombre de jour arbitraire) :
            - Récupération des informations des dates + affichage (temps de réponse : rapide)
         - ```Else ```:
            - Webscraping de la page allevents + création JSON + insertion MongoDB + remplacement des information de la ville dans SQL si SQL existe (temps de réponse : lente ~ 1-8mn cas à Londres)
                - Informations obsolètes dans le SQL effacées
                - Conservation des informations obsolètes dans le MongoDB + JSON
                
      - Résultat sous cette forme (format du SQL compacte pour la rapidité):
     
     
     ![unknown](https://user-images.githubusercontent.com/63191063/197460905-6c81edb4-3bcc-4e86-b41d-97501a211a2d.png)
     
    #### Lancement d'un vol sous Dash

     - Compléter les informations pour trouver un vol aller-retour
       - compléter la ville de départ, le nombre d'adulte, d'enfants et de bébés

       - ![unknown](https://user-images.githubusercontent.com/63191063/197513817-c9d6a1b9-9a05-45ef-941e-59b42437fc49.png)
       
       
       - Chargement de la requête :
       
       
   ![unknown](https://user-images.githubusercontent.com/63191063/197514031-a666091d-eede-48ee-b7e5-426442709a57.png)

      
 - Exécution de toute la chaine :requete, création des json, insértion dans la base MongoDB, insertion dans SQL
      
      - Résultat sous cette forme : 
      
      
      
      
      ![unknown](https://user-images.githubusercontent.com/63191063/197514421-563ae25d-62ae-466f-8e3e-89c6112d6800.png)




      
 - Stockage des données dans Data/json/requetes/Ville_de_Départ-Ville_d'arrivée/Jour_de_la_requete.json
      
      
      
      ![unknown](https://user-images.githubusercontent.com/63191063/197514568-0dc8db62-1178-4f8a-8b0c-82089ea1481f.png)


### 4. Containerisation et deploiement 

- Structure du code intégré dans une image Dockerfile pour le déploiement
- Construction de l'image 

``` docker image build -t xzo75/project_airlines:latest```

- Utilisation de Kubernetes pour déployer l'application

- Construction des fichiers yaml : 
  - Fichier de déploiement 
    - project-air-deployment.yml

  - Fichier yaml du contrôleur
    - project-air-ingress.yml
 
  - Fichier yaml pour le réseau dans kubernetes
    - project-air-service.yml
    
  - Résultat du déploiement
    
    ![unknown](https://user-images.githubusercontent.com/63191063/198229041-fddb4c43-013b-4c79-9634-e38292be4c2a.png)

    
    

### 5. Conclusion 

- Résolution de la problématique. 
-  Optimisation du projet en rajoutant une route pour les recommandation d'hôtel dans l'extraction de donnée 
-  Optimisation du projet en mettant les vols les plus populaire comme information


