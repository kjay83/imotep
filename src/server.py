# server.py

from flask import render_template # Remove: import Flask
import connexion


def create_app():
    app1 = connexion.FlaskApp(__name__, specification_dir="./")   
    app1.add_api("swagger.yml")

    @app1.route("/index")
    def index():
        return render_template("index.html")

    @app1.route("/")
    def home():
        return render_template("home.html")
    
    return app1

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
