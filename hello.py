from flask import Flask
from flask import request
from flask import current_app
from flask import make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    app_name = current_app.name
    html = """
            <h1>Hello World!</h1>
            <h2>The User-Agent is {}</h2>
            <h2>The current_app name is {}</h2>
           """.format(user_agent,app_name)
    response = make_response(html)
    response.set_cookie("answer","42")
    return response

if __name__=="__main__":
    manager.run()
