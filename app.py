from flask import Flask, jsonify, request
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password ='',
    database = 'usuarios',
    port =3306   
)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'



@app.post('/usuarios')
def crearUsuario():
    #request  => envia el cliente
    #response => lo que le voy a responder
    datos = request.json
    
    print(datos)

    cursor = db.cursor()

    cursor.execute('''INSERT INTO usuario(nombres, email, contrasena)
        VALUE(%s, %s, %s)''', (
        datos['nombres'],
        datos['email'],
        datos['contrasena'],
    ))

    db.commit()
    
    return jsonify({

        "mensaje": "usuario alamcenado correctamente"
    })


@app.get('/usuarios')
def listaUsuarios():
    cursor = db.cursor(dictionary=True)

    cursor.execute('select * from usuario')

    usuarios = cursor.fetchall()

    return jsonify(usuarios)




@app.put('/usuarios/<id>')
def actualizarUsuario(id):

    datos=request.json

    cursor = db.cursor()


    cursor.execute('''UPDATE usuario set nombres=%s, 
        email=%s, contrasena=%s where id=%s''',(
            datos['nombres'],
            datos['email'],
            datos['contrasena'],
            id
        ))
    
    db.commit()

    return jsonify({

        "mensaje": "usuario almacenado correctamente"
    })


@app.delete('/usuarios/<id>')
def eliminarUsuario(id):


    cursor = db.cursor()
    cursor.execute('DELETE FROM usuario where id=%s',(id,))


    db.commit()

    return jsonify({

        "mensaje": "usuario eliminado correctamente"
    })




app.run(debug=True)