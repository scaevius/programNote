from flask_nav import Nav
from flask_nav.elements import Navbar, View
from program_note import app, views

nav = Nav(app)

nav.register_element('navbar', Navbar(
    'thenav',
    View('Home Page', 'index'),
    View('About', 'about'),
    View('Create Account', 'signup'),
    View('Log In', 'login')
))

nav.register_element('backendNav', Navbar(
    'backendNav',
    View('Add Note', 'dashboard'),
    View('All Notes', 'allNotes'),
    View('Categories', 'categories'),
    View('Account Settings', 'accountSettings')
))