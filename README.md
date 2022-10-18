


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
       - Formats différents pour les données bruts provenant de Airport et Airline (éviter les doublons)
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

             ex  id de legs : ```LHR-LAX:BA5951~11:BA6123~11:0" ``` et de price ex : ```a6fca0f2a8a3e4f3msr:BA5951~11-BA6123~11``` en ```BA5951~11-BA6123~11 ```
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
                 
 ### 2.2 Traitement des données en utilisant une base de donnée SQL 
   - Dans  le cas du SQL (SQLite soucis de rapidité, dans un vrai contexte un vrais SGBD MySQL) :
      - Nécessité de laisser les tables disjoinctes car les données provenant de MongoDB ont des structures différentes :
        - Collection Vol et Prix :  1 destination  = 200 vols 
        - Collection évènement : 1 clé = 1 évènement
        - Collection Airlines et Airport : 1 code aéroport = 1 nom aéroport


      - - Transformation des données sous le meme format que airline et airport
      -  création d'une table concernant les villes et leur code IATA pour obtenir le cityCode de chaque ville
      
      
      
      
      - Tableau d'information sur le vol et les évènements (schémas fixe)
          - Connexion + création d'une base de données sqlite :``` create_engine('sqlite:///travel.db', echo = True)``` 
           - Créations des tables  (récupération des données utilisées pour le projet):

              ```Vol ```

             ```Price ```

             ```Airline```

             ```Airport```

             ```evenement ``` 
        - Insertion des données SQL dans SQLite :  ``` INSERT OR REPLACE INTO Events VALUES ({markers}) ```
        - Jointure des données dans la base de donnée SQL pour obtenir une table résultante contenant les informations sur les vols, les prix, la destination et les activités:
                ```  SELECT ... INNER JOIN ... ON ...  ```
            
## 3. Consommation des données 

 - Création d'une application Dash
    - Affichage de la table jointe sur DASH
    - Utilisateur entre une ville de destination sur Le Dash, le Dash récupère les données des activités dans le SQL et l'affiche. L'utilisateur sélectionne une activité puis le Dash va récupérer les données de vol pour cette ville puis affiche les données de Vol dans Dash.
