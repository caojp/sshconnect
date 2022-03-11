ssh connect
========
## envirtualment
> virtualenv -p python3 env  
> source env/bin/activate
## Install
> pip install -r requirements.txt
## Help
> python main.py

## Run user name password
> python main.py -i 11.1.2.1 -d 22 -u root -p 123456

## Run user file and password file
> python main.py -i 11.1.2.1 -d 22 -U /tmp/usernames.txt -P /tmp/password.txt


