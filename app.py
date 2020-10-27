from flask import Flask, render_template,request
from flask_mysql_connector import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secretsecret'
app.config['MYSQL_DATABASE'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        userDetails = request.form
        name = userDetails["name"]
        email = userDetails["email"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return "success"
    return render_template('index.html')

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute('SELECT * FROM users')
    if resultValue is None:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)