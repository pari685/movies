# A Simple Movie Database
##  by Parikshit Juluri

This is a Simple Movie Database Project using the Python Django Framework.

Views
-----

* Add New Movie: Add a new movie and its related information: Movie Title, Director, Genre, and Language
* List all Movies: List the movies in the Database in the form of a table
* Search Movie: Search the database based on one or more of the fields from: Movie Title, Director, Genre, and Language

Usage
----
require: Python-Django
 ```
 # Create the database file and the move table
  python manage.py syncdb
 
 # Run the server on a localhost
 python manage.py runserver
 
 # to run the server on a specific IP 0.0.0.0 on port 8000
 python manage.py runserver 0.0.0.0:8000
 ```


