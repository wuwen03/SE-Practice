from flask import Blueprint,request,jsonify

bp_user = Blueprint("user",__name__,"/user")

@bp_user.route('/login',methods=['POST'])
def login():
    pass