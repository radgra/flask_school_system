from flask_restful import Resource
from models.user import UserModel
from flask import request
from schemas.user import UserSchema
from marshmallow import ValidationError 
from db import db
from sqlalchemy import exc
from flask_jwt_extended import create_access_token, create_refresh_token

class UserList(Resource):
    user_schema = UserSchema()
    
    def get(self):
        users = UserModel.query.all()

        return self.user_schema.dump(users, many=True)

    def post(self):
        data = request.get_json()

        try:
            data_parsed = self.user_schema.load(data)
            new_user = UserModel(**data_parsed)
            db.session.add(new_user)
            db.session.commit()

        except ValidationError as err:
            return err.messages, 400
        
        # w dluzeszej perpektywie moge integerityerror skasowac
        except exc.IntegrityError as e:
            return {"message": e.args[0]}, 500
        except:
            return {"message": "Something went wrong"}, 500


        return data_parsed


class UserLogin(Resource):
    user_schema = UserSchema(only=("password","username"))
    
    def post(self):
        data = request.get_json()
        user_data = self.user_schema.load(data)

        user = UserModel.query.filter_by(username=user_data["username"]).first()

        # tu tzeba hashowac password
        if user and user_data['password'] == user.password:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)

            return {
                "access_token":access_token,
                "refresh_token":refresh_token
            }
        
        return {"message": "Invalid credentials"}