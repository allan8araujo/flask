from flask import render_template, url_for, redirect, flash
from aplicativo import app,db,bcrypt
from aplicativo.forms import RegistrationForm, LoginForm
from .models import User,Post
from flask_login import login_user, current_user, logout_user
sell_accs = [
    {'nick': 'Abacato',
     'level': '300',
     'elo': 'Plat III'
     },
    {'nick': 'paradoxo de zeno',
     'level': '214',
     'elo': 'diamond II'
     }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        flash(f'You account has been created!', 'success!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(' please check unsername and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/elojobref')
def elojobrefs():
    return render_template('elojobrefs.html')

@app.route('/accs_sellings')
def selling_accs():
    return render_template('selling_accs.html', sell_accs=sell_accs)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
