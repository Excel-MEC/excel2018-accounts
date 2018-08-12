# excel2018-accounts
A platform for event managers and participants for EXCEL 2018

### Create python virtual environment and install python dependencies
```
virtualenv -p python3 env
source env/bin/activate  # run this command everytime before working on project
pip install -r requirements.txt
```

### Set up PostgreSQL
```
sudo su - postgres
CREATE DATABASE excel2018_accounts;
CREATE USER admin WITH PASSWORD 'pass';
ALTER ROLE admin SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE excel2018_accounts TO admin;
```
