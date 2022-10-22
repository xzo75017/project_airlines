FROM python:3.10
RUN apt-get update && apt-get install python3-pip -y && pip3 install datetime && pip3 install dash && pip3 install sqlalchemy && pip3 install pandas && pip3 install requests && pip3 install pymongo && pip3 install bs4 && pip3 install dash && pip3 install dash_bootstrap_components 
ADD App_dash.py home/ubuntu/project_airlines/app/App_dash.py
ADD Dash_utils.py home/ubuntu/project_airlines/app/Dash_utils.py
ADD Data home/ubuntu/project_airlines/app/Data
ADD API_flightapi home/ubuntu/project_airlines/app/API_flightapi
ADD Dash home/ubuntu/project_airlines/app/Dash
ADD allevents home/ubuntu/project_airlines/app/allevents
WORKDIR /app/
EXPOSE 5000
RUN python3 /home/ubuntu/project_airlines/app/App_dash.py