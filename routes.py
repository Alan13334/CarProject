from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car')
    results = cur.fetchall()

    return render_template("home.html",results=results)
    
@app.route("/contact")
def contacts():
    return render_template("contact.html",title="Contact")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route('/all_cars')
def cars():
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car')
    car = cur.fetchall()
    return render_template('all_cars.html', car=car)

@app.route('/cars/<int:id>')
def car(id):
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT name FROM car WHERE id=?',(id,))
    name = cur.fetchone()
    cur.execute('SELECT brand FROM car WHERE id=?',(id,))
    brand = cur.fetchone()
    cur.execute('SELECT catergory FROM car WHERE id=?',(id,))
    catergory = cur.fetchall()
    cur.execute('SELECT name FROM car WHERE id=?',(id,))
    return render_template("cars.html",name=name, brand=brand,catergory=catergory)


if __name__ == '__main__':
    app.run(debug = True)