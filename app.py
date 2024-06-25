from flask import Flask, render_template, request, redirect, url_for, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.String(15), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/user/<int:id>')
def user_detail(id):
    user = User.query.get_or_404(id)
    return render_template('user_detail.html', user=user)

@app.route('/create', methods=('GET', 'POST'))
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        telephone = request.form['telephone']
        new_user = User(name=name, surname=surname, email=email, telephone=telephone)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_user.html')

@app.route('/update/<int:id>', methods=('GET', 'POST'))
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.telephone = request.form['telephone']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_user.html', user=user)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
