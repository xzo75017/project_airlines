

# I Objectif du projet Airline

Permettre à un utilisateur souhaitant partir en voyage d'avoir accès aux événements du pays en lui proposant un billet d'avion à destination de ce pays  


# II Architecture du projet 

Le projet va s'articuler de la manière suivante comme l'indique le diagramme ci-dessous : 


![Diagram_DST drawio (1)](https://user-images.githubusercontent.com/63191063/196041099-d75d486c-932e-4600-838e-e5af91849923.png)



# III Etapes du projet 

## 1. Extraction des données 


- Prise en main de FlightAPI et Allevents (création de compte, requêtage des différentes routes et comparaison des données retournées).
- Requêtage des données sur 3 end points :
 ```bash
     /onewaytrip/YOURAPIKEY/LHR/LAX/2019-10-11/2/0/1/Economy/USD
     /iata/api-key?name=american&type=airline
     /roundtrip/YOURAPIKEY/LHR/LAX/2019-10-11/2019-10-15/2/0/1/Economy/USD
```
- Résultats des requêtes 
Allevents : 
Requete-du-26-09-2022.json
Requete-du-30-09-2022.json

FlightAPI : 

flightapi_schedule_2.json

PriceFlightAPI :
price.json

AirportCodeAPI : 
airport.json 

## 2. Organisation de la base de donnée 

 - Création d'un cluster MongoDB en effectuant un pré-traitement des données dans les fichiers JSON (non nécessité de définir soigneusement leur structure à l'avance d'où l'utilisation de MongoDB)
   - changement id de legs ex :```   LHR-LAX:BA5951~11:BA6123~11:0" ``` et de price ex : ```a6fca0f2a8a3e4f3msr:BA5951~11-BA6123~11``` en ```BA5951~11-BA6123~11 ```
 - Utilisation de MongoDB pour avoir une clarté dans le code + allégement des temps de calcul comparé à SQL 


- Connexion au MongoDB :  ```client = MongoClient("mongodb+srv://DST-PROJECT:DST@cluster0.7wo11db.mongodb.net/?retryWrites=true&w=majority```

- Création des collections (récupération des données utilisées pour le projet).
   -  ```Vol ```
   -   ```Price ```
   - ```Airline```
   - ```Airport```

Sélections de 9 variables sur les 30 présentes dans la collection ```Vol``` :
  - ```departureTime ```
  - ```arrivalTime```
  - ```duration```
  - ```departureAirportCode```
  - ```arrivalAirportCode```
  - ```airlineCodes```
  - ```departureDate```
  -  ```arrivalDate```

 Sélection des variables suivantes pour la collection ```Price```:
  - ```totalAmount```
  - ```amountPerAdult```
  - ```amountPerChild```
  - ```amountPerInfant``` 

 Sélection des variables suivantes pour la collection ```Airline```:
  - code de la compagnie aérienne ex : ```AF```
  - nom de la compagnie aérienne ex : ```Air France```


Sélection des variables suivantes pour la collection ```Airport```:
  - code de la compagnie aérienne ex : ```CDG```
  - nom de la compagnie aérienne ex : ```Charles de Gaulle```


- Connexion + création d'une base de données sqlite :``` create_engine('sqlite:///travel.db', echo = True)```
  - Création d'une base de donnée SQL pour garantir un schéma fixe des données. 
  - Insertion des données SQL dans SQLite (table laissées disjointe (avec création d'une table de jointure en plus))
  - Jointure des données dans la base de donnée SQL obtenir une table résultante contenant les informations sur les vols, la période, la destination et les activités. 



    

## 3. Consommation des données 

 - Création d'une application Dash
    - Affichage de la table jointe sur DASH
    - Utilisateur entre une ville de destination sur Le Dash, le Dash récupère les données des activités dans le SQL et l'affiche. L'utilisateur sélectionne une activité puis le Dash va récupérer les données de vol pour cette ville puis affiche les données de Vol dans Dash.
