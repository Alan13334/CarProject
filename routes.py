from flask import Flask,render_template,request, redirect
import sqlite3
app = Flask(__name__)

def get_random_data():
    with sqlite3.connect('car.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM car ORDER BY RANDOM() LIMIT 3")
        data = cursor.fetchall()
    return data

@app.route('/')
def home():
    random_data = get_random_data()
    return render_template('home.html', data=random_data)
    
@app.route("/contact")
def contacts():
    return render_template("contact.html",title="Contact")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route('/cars/<int:id>')
def car(id):
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car WHERE brand=?',(id,))
    car = cur.fetchall()
    
    return render_template("cars.html",car=car)

@app.route('/contact', methods=['POST'])
def contact_form():
    conn = sqlite3.connect('car.db')
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    conn = sqlite3.connect('car.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Contact (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    return redirect("http://127.0.0.1:5000/")




@app.route('/cars_detail/<int:id>')
def cars_detail(id):
    conn = sqlite3.connect('car.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM car WHERE id=?',(id,))
    car = cur.fetchall()
    
    
    cur.execute('SELECT name FROM category WHERE id=?',(car[0][3],))
    category = cur.fetchall()
    return render_template("cars_detail.html",car=car,category=category)


if __name__ == '__main__':
    app.run(debug = True)