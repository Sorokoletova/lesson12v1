import json
from json import JSONDecodeError
from exceptions import ErrorContentException, ErrorFiletypeException


def get_posts_list():
    """ Получаем список всех постов"""
    try:
        with open("posts.json", encoding='utf8') as file:
            posts_list = json.load(file)
        return posts_list
    except (FileNotFoundError, JSONDecodeError):
        raise ErrorContentException("Файл не найден или не может быть преобразован")


def get_post_content(content):
    """Получаем пост по контенту"""
    try:
        posts = get_posts_list()
        content_l = content.lower()
        post_content = []
        for post in posts:
            if content_l in post["content"].lower():
                post_content.append(post)
        return post_content
    except TypeError:
        raise ErrorContentException("Не подготовлены данные для выбора")


def add_post_pictures(picture):
    """" Записывает картинку из поста в uploads/picture/ """

    filename = picture.filename
    file_type = filename.split('.')[-1]
    if file_type not in ["jpeg", "jpg", "png"]:
        raise ErrorFiletypeException
    picture.save(f"uploads/picture/{filename}")

    return f"uploads/picture/{filename}"


def add_post_joson(post):
    """" Записывает данные поста в posts.json """

    posts = get_posts_list()
    posts.append(post)
    try:
        with open("posts.json", "w", encoding='utf-8') as file:
            json.dump(posts, file, ensure_ascii=False)
        return "Данные записаны"
    except (FileNotFoundError, JSONDecodeError):
        raise ErrorContentException("Файл для записи не найден или не может быть преобразован")
