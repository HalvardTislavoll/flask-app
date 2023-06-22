import json
from flask import Flask, abort
from markupsafe import escape

# Create the Flask application
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')

def hello_world():
    return 'Hello, Halvard Tislavoll!'

'''using template:
@app.route("/about")
def about():
    return render_template("about-us.html")
'''

@app.route('/index/')
def index():
    return json.dumps({'name': 'Flask_test', 'email': 'halvard.tislavoll@haugnett.no'})

###############################
#   Routes and View Functions
###############################

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

"""
In this step, you’ll add a few routes to your application to display
different pages depending on the requested URL. You’ll also learn
about view functions and how to use them.

A route is a URL you can use to determine what the user receives
when they visit your web application on their browser.
For example, http://127.0.0.1:5000/ is the main route that might be
used to display an index page.
The URL http://127.0.0.1:5000/about may be another route used for
an about page that gives the visitor some information about
your web application. Similarly, you can create a route that allows
users to sign in to your application at http://127.0.0.1:5000/login.

Your Flask application currently has one route that serves users
who request the main URL (http://127.0.0.1:5000/).
To demonstrate how to add a new web page to your application,
you will edit your application file to add another route that provides
information on your web application at http://127.0.0.1:5000/about.
"""

###############################
#   Dynamic Routes:
###############################

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

"""
## depends on 'from markupsafe import escape'
This new route has a variable section <word>. This tells Flask to
take the value from the URL and pass it to the view function.
The URL variable <word> passes a keyword argument to
the capitalize() view function. The argument has the same name as
the URL variable (word in this case).
With this you can access the word passed through the URL and
respond with a capitalized version of it using
the capitalize() method in Python.

You use the escape() function you imported earlier to render
the word string as text. This is important to avoid
Cross Site Scripting (XSS) attacks. If the user submits
malicious JavaScript instead of a word, escape() will it render as
text and the browser will not run it,
keeping your web application safe.

To display the capitalized word inside an <h1> HTML heading,
you use the format() Python method, for more on this method,
see How To Use String Formatters in Python 3

With the development server running, open your browser and visit
the following URLs. You can replace the highlighted words with any
word of your choice.

http://127.0.0.1:5000/capitalize/hello
http://127.0.0.1:5000/capitalize/flask
http://127.0.0.1:5000/capitalize/python
"""


@app.route('/add/<int:n1>/<int:n2>/')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)

"""
In this route, you use a special converter int with the
URL variable (/add/<int:n1>/<int:n2>/)
which only accepts positive integers. By default,
URL variables are assumed to be strings and are treated as such.

With the development server running, open your browser and
visit the following URL:
http://127.0.0.1:5000/add/5/5/
"""

'''
@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])
'''
"""
In the route above, the greet_user() view function receives a
user_id argument from the user_id URL variable.
You use the int converter to accept positive integers.
Inside the function, you have a Python list called users, which
contains three strings representing usernames.
The view function returns a string that is constructed depending
on the provided user_id. If the user_id is 0, the response will be
Hi Bob in an <h2> tag because Bob is the first item in the list
(the value of users[0]).

With the development server running, open your browser and visit
the following URLs:

http://127.0.0.1:5000/users/0
http://127.0.0.1:5000/users/1
http://127.0.0.1:5000/users/2
"""


@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)
"""
## depends on 'from markupsafe import abort'
You use try above to test the return expression for errors.
If there was no error, meaning that user_id has a value that matches
an index in the users list, the application will respond with
the appropriate greeting. If the value of user_id is outside
the list’s range, an IndexError exception will be raised, and you use
except to catch the error and respond with an HTTP 404 error using
the abort() Flask helper function.

Now, with the development server running, visit the URL again:
http://127.0.0.1:5000/users/3
"""


# Run the application
if __name__ == '__main__':
    app.run()

