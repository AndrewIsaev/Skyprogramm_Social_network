from flask import Blueprint


handler_blueprint = Blueprint('handler_blueprint', __name__, template_folder='templates')


@handler_blueprint.errorhandler(404)
def error404():
    return "статус-код 404"


@handler_blueprint.errorhandler(500)
def error500():
    return "статус-код 500"