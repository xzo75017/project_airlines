from os import access
import requests

url = "https://api.lufthansa.com/v1/oauth/token"
header_auth = {'client_id':'fuf4333jnbsfp63vdc248rxq', 'client_secret':'bfQKjgnQMQBTxtXMGtpq', 'grant_type':'client_credentials'}
token = requests.post(url, data=header_auth)
#token = requests.post(url, auth=("fuf4333jnbsfp63vdc248rxq","bfQKjgnQMQBTxtXMGtpq"))
j = token.json()

myrequest = "https://api.lufthansa.com/v1/flight-schedules/flightschedules/passenger?airlines=LH&flightNumberRanges=400-405&startDate=05AUG22&endDate=10AUG22&daysOfOperation=1234567&timeMode=UTC"

pw = j['access_token']
header = {'Authorization':'Bearer ' + str(pw), 'Accept': 'application/json'}
print(header)
req = requests.get(myrequest, headers=header)
print(req.json())