import requests

url = "https://api.lufthansa.com/v1/oauth/token"       #url pour post une demande de token
header_auth = {'client_id':'fuf4333jnbsfp63vdc248rxq', 'client_secret':'bfQKjgnQMQBTxtXMGtpq', 'grant_type':'client_credentials'}  #header avec l'id, le mdp (secret) et grant_type
token = requests.post(url, data=header_auth)    #demande de token
j = token.json()  #on transforme le token en json pour lire et récuperer les infos plus facilement

#url pour lancer une requete dans l'API : ici on demande des informations sur les vols des avions de LH, ayant un numéro entre 400 et 405 et entre le 5 et 10 aout , tout les jours
myrequest = "https://api.lufthansa.com/v1/flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate=05AUG22&endDate=10AUG22&daysOfOperation=1234567&timeMode=UTC"

pw = j['access_token']  #on récupère le token pour s'authentifier
header = {'Authorization':'Bearer ' + str(pw), 'Accept': 'application/json'}  #header permettant de s'authentifier
print(header)   #test pour voir si on l'a bien récupéré
req = requests.get(myrequest, headers=header)   #requete lancée
print(req.json())  #on affiche le résultat