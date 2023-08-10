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
    cur.execute('SELECT * FROM car WHERE brand=?',(id,))
    car = cur.fetchall()
    
    return render_template("cars.html",car=car)


@app.route('/cars_detail/<int:id>')
def cars_detail(id):
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car WHERE id=?',(id,))
    car = cur.fetchall()
    return render_template("cars_detail.html",car=car)


if __name__ == '__main__':
    app.run(debug = True)