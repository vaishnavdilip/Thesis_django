# Thesis_django

Django web app for thesis. To start with make sure that you have python installed on your system.

## Instructions

### Virtual environment

Create a virtual environment for this project. I created one using the virtualenv module installed by default in python.

```{python}
virtualenv venv
```
Once the virtualenv is created, activate it using

```{python}
venv\Scripts\Activate
```

on Windows. Activate using source command if on Linux.

### Dependencies

Now we can install the packages required for this project using the requirements.txt


```{python}
pip install -r requirements.txt
```
This might take some time. 

### Server

Once installation is done, make sure the neo4j database is running. Now run the server using


```{python}
python manage.py runserver
```

Access the webapp on http://localhost:8000

## Sites

 - Homepage 
 - Dashboard
 - Recommendation
 - Link Prediction

