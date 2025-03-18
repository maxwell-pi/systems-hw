# NLP Systems Assignment 2
## Maxwell Pickering

## How to Run

Create a virtual environment from `requirements.py`, and then execute `run.py`.

## Code Notes

This project uses Flask and Flask-SQLAlchemy to provide a database backend to the notebook web app from Assignment 1. The app is packaged as `notebook`. When the `notebook` package is initialized, a Flask app is created, a SQLAlchemy database connection is opened, and the routes contained in `notebook.routes` are registered. The app can then be launched, but the the database tables must first be initialized in the app context. This is all handled in the `run.py` script.

## Database Model

The `notes.py` file from Assignment 1 is replaced by `model.py`, which defines the notebook database ORM. The notebook is implemented with two tables: notes and comments. The notes table has schema: id, title, body, time, comments. The comments table has schema: id, body, time, parent_node_id. Both `Note` and `Table` also implement a number of class methods which encapsulate database logic in the ORM object classes, allowing other modules to know nothing about the database itself and just interact with `Note` and `Comment` objects.

The notes and comments tables are linked, as there exists a one-to-many mapping from a note to comments. Each comment stores the primary key id of the note to which it maps. Additionally, a relationship is declared between notes and comments in the `Note` object, specifying a backreference from comments to notes: 'author'. A consequence of this is that when a note is deleted, all comments which map to it must also be deleted.

`Note` implements a `search()` class, which must now not only search titles and bodies but also comments. To enable this, we perform a table join with the comments table on note_ids, then filter by the search term string, and then report all the distinct discovered notes.

## Flask Routes

Nothing complicated is done here; information is passed in to route functions via: (1) HTML request forms, and (2) URL values. For each route, when appropriate, this information is collected, processed using calls to class methods defined in `model.py`, and realized to the user with the rendering of a Jinja template. The database logic encapsulation in the `model` module allows for especially clean code here.

## Jinja

Nothing major has changed here from Assignment 1; I rely on forms to handle all the notebook actions. I did clean up/rewrite a reasonable amount. I eliminated all the div markings, as I found I could get the visuals I wanted without them.

I do reformat the database times to nice strings. It might be more appropriate to do this elsewhere, but I think it's not too bad to do it here, since the role of the Jinja template is to realize information for consumption by the user.

Most notably, I use a togglable add comment field, which is implemented with a Javascript script. The toggle button and the add comment field are both declared in the HTML, and the script is loaded in the HTML with a script tag. The Javascript simply adds a click listener to the button (identified by element id), and whenever click, toggles the display style of the add comment field (also identified by element id) between invisible and visible.

A simple CSS stylesheet is shared between the two Jinja templates.