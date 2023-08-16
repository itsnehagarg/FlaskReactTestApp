from flask import Flask

api= Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body={
        "name" : "neha",
        "about" : "hey, there!"
    }
    return response_body