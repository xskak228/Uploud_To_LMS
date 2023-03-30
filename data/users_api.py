import flask
from flask import jsonify, request

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users', methods=["GET"])
def get_users():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    return jsonify(
        {
            'user':
                [item.to_dict(only=('id', "surname", "name", "email"))
                 for item in user]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'user': user.to_dict(only=('id', "surname", "name", "age", "position",
                                       "speciality", "address", "email", "modified_date"
                                       ))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', "surname", "name", "age",
                  "position", "speciality", "address",
                  "email", "hashed_passw    ord"]):
        return jsonify({'error': 'Bad request'})
    if db_sess.query(User).filter(User.id == request.json["id"]).first():
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json["id"],
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality = request.json['speciality'],
        address = request.json['address'],
        email=request.json['email'],
        hashed_password=request.json['hashed_password']
    )
    db_sess.add(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def change_job(user_id):
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    user = db_sess.query(User).filter(User.id == user_id).first()
    if user:
        user.surname = request.json['surname']
        user.name = request.json['name']
        user.age = request.json['age']
        user.position = request.json['position']
        user.speciality = request.json['speciality']
        user.address = request.json['address']
        user.email = request.json['email']
        user.hashed_password = request.json['hashed_password']
        db_sess.commit()
    else:
        return jsonify({'error': 'Not found'})
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_job(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return jsonify({'success': 'OK'})