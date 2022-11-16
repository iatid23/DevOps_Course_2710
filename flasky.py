from flask import Flask
from os import walk


# app = Flask(__name__)
#
#
# @app.route("/content")
def ret_content():
    filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
    for file in filenames:
        if file.lower().endswith('txt'):
            print(file)
            content = open(file, 'r')
            return content.read()
        #to do  status code 200


def register():
    filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
    for file in filenames:
        if file.lower().endswith('txt'):
            print(file)
            content = open(file, 'w+')
            # write hello and return success and 201

