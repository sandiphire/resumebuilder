try:
    from flask import Flask, request, jsonify
    from flask_restful import Resource, Api
    # from security import auth, identity
    # from flask_jwt import JWT, jwt_required
    from flask_restful import reqparse
    from user import SignUp
    import database
    from resumebuilderproj import api1
except Exception as e:
    print("Some modules are missing {}".format(e))

app = Flask(__name__)
app.register_blueprint(api1, url_prefix="/")
app.config['SECRET_KEY'] = 'Hard to guess'
api = Api(app)

pagination = reqparse.RequestParser()
pagination.add_argument('id',type=int, required = False, default = 1, help = "Please enter id")
pagination.add_argument('role', type=str, required = False, help = "Please enter role")

class Role(Resource):
    def __init__(self):
        self.id = pagination.parse_args().get('id', None)
        self.role = pagination.parse_args().get('role', None)
        
    def get(self):
        role_id = self.id
        conn = database.connect()
        role_desc = database.get_role_by_id(conn, role_id)
        conn.close()
        return jsonify({'role_desc':role_desc[1]})
    
    def post(self):
        role_desc = self.role
        conn = database.connect()
        database.insert_role(conn, role_desc)
        conn.close()
        return {'you sent': role_desc}, 201

class Multi(Resource):
    def get(self, num):
        return {'result': num *10}
    

class Resume(Resource):
    def __init__(self):
        pass
    
    
    def get(self):
        role_id = request.get_json()
        conn = database.connect() 
        id = role_id['role_id']
        resume = database.get_resume_by_i('id')
        
     
        return resume.jsonify()
    
    def post(self ,name):
        Tem = {'Data':name}
        Data.append(Tem)
        return Tem
    
    def delete(self,name):
        for ind, x in enumerate(Data):
            if x['Data'] == name:
                Tem = Data.pop(ind)
                return {'Note':'Deleted'}


# api.add_resource(People,'/Name/<string:name>')
api.add_resource(Multi, '/multi/<int:num>')
api.add_resource(SignUp, '/signup')
api.add_resource(Role,'/role')
# api.add_resource(Role,'/roledesc/<string:role>')



# Post API- add employee details http://localhost:9090/emp/add
# c.execute("""CREATE TABLE resume (
#         resume_id integer,
#         user_id text,
#         resume_type_id integer,
#         role_id blob
#     )""")

if __name__ =='__main__':
    app.run(debug=True)
    
