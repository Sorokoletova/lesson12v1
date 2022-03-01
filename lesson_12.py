from flask import Flask, send_from_directory
from main.main import find_post_blueprint
from loader.loader import add_post_blueprint

app = Flask(__name__)

app.register_blueprint(find_post_blueprint)
app.register_blueprint(add_post_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
