from flask import Blueprint
from controllers.user_controller import UserController

class UserBlueprint:
    user_bp = Blueprint('user',__name__,url_prefix='/api/v1/users')

    user_bp.route('/',methods=['GET'])(UserController.get_users)
    user_bp.route('/<int:id>',methods=['GET'])(UserController.get_user)
    user_bp.route('/',methods=['POST'])(UserController.create_user)
    user_bp.route('/<int:id>',methods=['PUT'])(UserController.update_user)
    user_bp.route('/<int:id>',methods=['DELETE'])(UserController.delete_user)
