from flask import Flask
from os import walk

hst = '0.0.0.0'
pt = '30000'

app = Flask(__name__)


# set to function Flask  => telling all u need is here (current dir)

#
@app.route("/content")
def ret_content():
    filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
    for file in filenames:
        if file.endswith('txt'):
            content = open(file, 'r', encoding='utf-8')
            result = content.read()
            content.close()
            return result, 200,
        #     return "there is no txt files here"


@app.route("/register")
def register():
    filenames = next(walk('./'), (None, None, []))[2]  # [] if no file
    for file in filenames:
        if file.endswith('txt'):

            content = open(file, 'w+')
            content.truncate(0)
            content.write("hello")
            return "success"
            # write hello and return success and 201


def runit():
    app.run(host=hst, port=pt)
