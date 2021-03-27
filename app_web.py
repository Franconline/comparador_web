from flask import Flask, render_template, request, send_file
from flask_mysqldb import MySQL
import prueba as main

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'carreras'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')
@app.route('/comparar', methods=["POST"])
def comparar():
    plan1 = request.form['plan1']
    plan2 = request.form['plan2']
    main.hacerTablas('primeraTabla.csv',plan1)
    main.hacerTablas('segundaTabla.csv',plan2)
    carrera1 = main.nombreDeLaCarrera(plan1)
    carrera2 = main.nombreDeLaCarrera(plan2)
#        cur = mysql.connection.cursor()
    main.diferencia('primeraTabla.csv','segundaTabla.csv',carrera1,carrera2)
    return send_file('diferencias.csv',mimetype='text/csv',attachment_filename='diferencias.csv', as_attachment=True)




if __name__  == '__main__':
   app.run(port= 3000, debug = True)