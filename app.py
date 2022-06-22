from html import entities
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Softjuandius_25@localhost:5432/software2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    contraseña = db.Column(db.String(80), nullable=False)

db.create_all()

#LOGEAR USUARIOS
@app.route('/authenticate/login', methods=['POST'])
def authenticate_user():
    error = False
    response = {}
    print(request.get_json())
    try:
        print("hola")
        username = request.get_json()['username']
        print(username)
        password = request.get_json()['password']
        print(password)
        db.session.query(Usuario).filter(Usuario.nombre==username).filter(Usuario.contraseña==password).one()
    except:
        print("adios")
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "Usuario o contraseña incorrecto"
    response['error'] = error
        
    return jsonify(response)

'''
@app.route('/test',methods=['GET'])
def probar_test():
    db_session = db.getSession()
    user = entities.Usuario(
        username = "dion",
        password = "0"
    )
'''
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')