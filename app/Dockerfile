FROM python:3.10
RUN apt-get update && apt-get install python3-pip -y && pip3 install datetime && pip3 install dash && pip3 install sqlalchemy && pip3 install pandas && pip3 install requests && pip3 install pymongo && pip3 install bs4 && pip3 install dash && pip3 install dash_bootstrap_components 

WORKDIR /app/

ADD App_dash.py App_dash.py
ADD Dash_utils.py Dash_utils.py
ADD sql_database.py sql_database.py
ADD Data Data
ADD cities.txt cities.txt
ADD API_flightapi API_flightapi
ADD Dash Dash
ADD allevents allevents
EXPOSE 5000

CMD python3 App_dash.py