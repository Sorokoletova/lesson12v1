from flask import Blueprint, render_template, request
import logging
from function12 import get_post_content

logging.basicConfig(filename="info.log", level=logging.INFO, encoding="UTF-8")
find_post_blueprint = Blueprint('find_post_blueprint', __name__, template_folder='templates')


@find_post_blueprint.route('/')
def find_post():
    logging.info("Cтраница по поиску запрошена")
    return render_template("index.html")


@find_post_blueprint.route('/search')
def search_list():
    logging.info("Cтраница с результатами поиска запрошена")
    s = request.args.get("s", "")
    postes = get_post_content(s)
    return render_template("post_list.html", postes=postes, s=s)
