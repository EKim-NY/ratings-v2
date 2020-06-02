"""CRUD operations."""

################ Utility Functions ######################
# from model.py in the same working directory, import: 
# db - an instance of SQLAlchemy() 
# User, Movie, Rating - classes 
# connect_to_db - a function

from model import db, User, Movie, Rating, connect_to_db

# Functions start here! 

def create_user(email, password):
    """Create and return a new user."""

    user = User(email = email, password = password)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all() 

def get_user_by_id(user_id): 
    """Return user by ID."""

    return User.query.get(user_id)

########################################################
############### Functions related to movies ############
########################################################

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title,
                  overview = overview,
                  release_date = release_date, 
                  poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Return all movies."""

    return Movie.query.all()

def new_rating(user, movie, score):
    """Create and return a new rating."""
    # This function should not work directly w/ primary keys.
    # Use class attributes from class Rating in model.py

    rating = Rating(user = user, 
                    movie = movie, 
                    score = score)

    db.session.add(rating)
    db.session.commit()

    return rating


def get_movie_by_id(movie_id): 
    """Return movie with the given ID."""

    return Movie.query.get(movie_id)


# connects you to the database when you run crud.py interactively 
if __name__ == '__main__': 
    from server import app 
    connect_to_db(app) 


