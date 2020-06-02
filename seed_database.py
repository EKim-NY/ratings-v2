"""Automatically populate database with fake data."""

# import os, json, crud, model, server modules from Python
# files after the first one in the line above won't be imported 
import os 
import json 
import crud
import model
import server 

# invalid syntax below 
# import (os, json, crud, model, server)

# QUESTION: 
# OK to use (function1, function2) after 'import' statement 
# but each file must be imported separately (?)

# import functions from random and datetime modules in Python 
from random import (choice, randint)
from datetime import datetime



# Automate: Get Python to delete and create "ratings" database.
os.system('dropdb ratngs')
os.system('createdb ratings')

# Automatically connect to the databse call create_all(). 
# We have to go through model to access create_all() 
#  because we imported model.py and not db from model.py; 
#  We can't access db directly. 
model.connect_to_db(server.app)
model.db.create_all()


###############################################################
#################### POPULATE FAKE MOVIES TABLE ################
###############################################################
"""
movie_data is a list of dictionaries that look like this: 

[{'overview': 'The search of the unknown.',
  'poster_path': 'https://image.tmdb.jpg',
  'release_date': '2019-09-20',
  'title': 'Ad Astra'}
  ...
  ]
"""

# Load data from data/movies.json and save as f. 
with open('data/movies.json') as f: 
    movie_data = json.loads(f.read())
    # movie_data is a dictionary of dictionaries

# Create movies, store them in list so we can use them 
# to create fake ratings
movies_in_db = []

for movie in movie_data: 
  # Extract and unpack dictionary values. 
  title, overview, poster_path = (movie['title'], 
                                  movie['overview'],
                                  movie['poster_path']
                                  ) 

  # Convert datetime object into a formatted string. 
  release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

  # Create a record for each movie. 
  db_movie = crud.create_movie(title,
                               overview, 
                               release_date,
                               poster_path)

  # Append movie to the list. 
  movies_in_db.append(db_movie)


###############################################################
#################### POPULATE FAKE USERS TABLE ################
###############################################################

# Load the JSON file as f and convert/save as a string. 
with open('data/users.json') as f: 
    user_data = json.loads(f.read())
    # user_data is a list of dictionaries of type string. 

users_in_db = []

for user in user_data: 
  email, password = (user['email'], user['password'])
  
  # For debugging: 
  # print("For user in user_data")                      
  # print(user, email, password)

  # Create a new user record and add it to the database
  new_user = crud.create_user(email, password)

  # For debugging: 
  # print("Create user", new_user)

  users_in_db.append(new_user)


  


