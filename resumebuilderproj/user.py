import sqlite3
from flask_restful import Resource
from flask import request
import database

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    @classmethod 
    def find_by_username(clss, username):
        conn = database.connect()
        c = conn.cursor()
        q1 = "SELECT * FROM user WHERE username=?"
        result = c.execute(q1, (username,))        
        row = result.fetchone()
        if row:
            user = clss(*row)
        else:
            user = None
        return user
    @classmethod
    def find_by_id(clss, id):
        conn = database.connect()
        c = conn.cursor()
        q1 = "SELECT * FROM user WHERE id=?"
        result = c.execute(q1, (id,))        
        row = result.fetchone()
        if row:
            user = clss(*row)
        else:
            user = None
        return user
        
        
class SignUp(Resource):
    def post(self):
        data = request.get_json()
        conn = database.connect()
        c = conn.cursor()
        q1 = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
        c.execute(q1)
        q2 = "INSERT INTO user VALUES(NULL,?,?)"
        c.execute(q2,(data['username'], data['password']))
        conn.commit()
        conn.close()
        return {'message':'user created successfully'}
    