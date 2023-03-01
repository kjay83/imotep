# app.py

from flask import render_template # Remove: import Flask
import connexion

# app = connexion.App(__name__, specification_dir="./")
# app.add_api("swagger.yml")

#def create_app(config):
def create_app():
    app1 = connexion.App(__name__, specification_dir="./")
    #app1.app.config.from_object(config)
    app1.add_api("swagger.yml")

    @app1.route("/index")
    def index():
        return render_template("index.html")

    @app1.route("/")
    def home():
        return render_template("home.html")
    
    return app1

# @app.route("/")
# def home():
#     return render_template("home.html")
app = create_app()


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True)
    #create_app({"TESTING": False}).run(host="0.0.0.0", port=8000, debug=True)
    app.run(host="0.0.0.0", port=8000, debug=True)
