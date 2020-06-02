"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

# configure Jinja2 setting to make it throw errors for undef. vars 
from jinja2 import StrictUndefined

app = Flask(__name__)
# Flask instance (ie, app) needs a secret key 
# else flash and session won't work
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/')
def homepage(): 
    """View homepage."""

    return render_template('homepage.html')

####################### Routes: Movie-related ######################

# This code from lab manual works! 
@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

###################### Routes: User-related ####################

@app.route('/users')
def users(): 
    """Show a list of all users."""
    users = crud.get_users()
    
    return render_template('all_users.html', users=users)



# Check that dynamic template placeholder variable 
# matches the arguments passed into the functions, methods below!
@app.route('/users/<email>')  
def get_user_by_id(email):
    """Get user info for user ID given."""

    # User info returned by get_user_by_id consists of
    # user_id, email, and password
    user_info = crud.get_user_by_id(email)

    # Assign local var "user_info" to template placeholder var "user"
    # located in user_details.html file 
    return render_template('user_details.html', user=user_info)



######################################################################
# Connect to database before calling app.run or Flask can't access db!
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

