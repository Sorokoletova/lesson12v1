from flask import Blueprint, render_template, request
import logging
from exceptions import ErrorFiletypeException
from function12 import add_post_pictures, add_post_joson
logging.basicConfig(filename="info.log", level=logging.INFO, encoding="UTF-8")
add_post_blueprint = Blueprint('add_post_blueprint', __name__, template_folder='templates')


@add_post_blueprint.route('/post')
def loader_post():
    logging.info("Cтраница по добавлению записи запрошена")
    return render_template("post_form.html")


@add_post_blueprint.route('/post', methods=['POST'])
def add_post():
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, т.к не были заполнены")
        return "Данные не загружены"
    try:
        pic_url = add_post_pictures(picture)
    except ErrorFiletypeException:
        return "Неверный тип файла"
    post = {"pic": "/" + pic_url, "content": content}
    add_post_joson(post)
    logging.info("Данные записаны в json")
    return render_template("post_uploaded.html", picture_url="/" + pic_url, content=content)
