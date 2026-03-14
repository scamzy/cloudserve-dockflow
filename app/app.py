from flask import Flask
import os

#create flask app
app = Flask(__name__)

#homepage route
@app.route("/")
def home():
    return """
    <h1>CloudServe + DockFlow Project</h1>
    <p>This Flask app is running inside a Podman container.</p>
    """

#run application
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
