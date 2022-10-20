# Simple project for data visualization using Django framework

First, clone the repo
```bash 
git clone git@github.com:Adawy0/google_trends.git
cd google_trends
```
## Install project requirements

Create the virtualenv
```bash
python3.7 -m venv venv
```

Activate it
```bash
source venv/bin/activate
```

And finally install the requirements
```bash
pip install -r requirements.dev.txt
```

## suppose you installed Postgresql in your device if not can use this
Please refer to this [link](https://www.tecmint.com/install-postgresql-and-pgadmin-in-ubuntu/) to Install postgresql and pgAdmin

## Create database for project
database name google_trends

## Source Env variables
Run this command before each run project
```bash
echo "source project.env
```
## Summary 
Project that get data from google trends apis then draw this data using amchars
Project contains three apis
1- for get historical interest data 
``` http://127.0.0.1:8000/apis/historical-interest/?kw=egypt```
2- for get interest by region data
``` http://127.0.0.1:8000/apis/interest-by-region/?kw=food&kw=eat```
3- for get data
```http://127.0.0.1:8000/apis/read-data```
