from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Activity
from app.forms import RegistrationForm, LoginForm, ActivityForm
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Início')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabéns, você está registrado!')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Registrar', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Nome de usuário ou senha inválidos')
            return redirect(url_for('main.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('login.html', title='Entrar', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    days_in_month = 31  # Use appropriate logic to get the number of days in the current month
    calendar = []
    today = datetime.today().day
    for day in range(1, days_in_month + 1):
        activity = Activity.query.filter_by(user_id=current_user.id, day=day).first()
        calendar.append({
            'day': day,
            'today': day == today,
            'activity': activity.description if activity else None
        })
    return render_template('dashboard.html', title='Painel de Controle', calendar=calendar)

@bp.route('/add_activity', methods=['POST'])
@login_required
def add_activity():
    day = int(request.form['day'])
    description = request.form['activity']
    activity = Activity(user_id=current_user.id, day=day, description=description)
    db.session.add(activity)
    db.session.commit()
    return redirect(url_for('main.dashboard'))
