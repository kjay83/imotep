# server.py

from flask import render_template # Remove: import Flask
#import connexion
import config
from models import People


def create_app():
    app1 = config.connex_app
    app1.add_api(config.basedir / "swagger.yml")

    @app1.route("/")
    def home():
        people = People.query.all()
        return render_template("home.html", people=people)

    # app1 = connexion.FlaskApp(__name__, specification_dir="./")   
    # app1.add_api("swagger.yml")

    @app1.route("/index")
    def index():
        return render_template("index.html")
    
    return app1

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
