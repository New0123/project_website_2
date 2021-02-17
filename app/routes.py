# -*- coding: utf-8 -*- 
# Один из главных файлов связывающий бд и сайт
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User, Post, SumMntSale, DiffMntSale, MaxOverShopsCapacity, CrntOverShopsCapacity, MntSaleShopNearHome, MntSaleSupershop, MntSaleGipershop, MntSaleFruit, MntSaleVegetables, MntSaleGreens, MntOverShopNearHome, MntOverSupershop, MntOverGipershop, MntOverFruit, MntOverVegetables, MntOverGreens
from datetime import datetime

@login_required
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]
    top_sales = get_top_sales()
    diff_mnt_sale = get_diff_mnt_sale()
    crnt_over_shops_capacity = get_crnt_over_shops_capacity()
    max_over_shops_capacity = get_max_over_shops_capacity()
    mnt_sale_shop_near_home = get_mnt_sale_shop_near_home()
    mnt_sale_supershop = get_mnt_sale_supershop()
    mnt_sale_gipershop = get_mnt_sale_gipershop()
    mnt_sale_fruit = get_mnt_sale_fruit()
    mnt_sale_vegetables = get_mnt_sale_vegetables()
    mnt_sale_greens = get_mnt_sale_greens()
    mnt_over_shop_near_home = get_mnt_over_shop_near_home()
    mnt_over_supershop = get_mnt_over_supershop()
    mnt_over_gipershop = get_mnt_over_gipershop()
    mnt_over_fruit = get_mnt_over_fruit()
    mnt_over_vegetables = get_mnt_over_vegetables()
    mnt_over_greens = get_mnt_over_greens()
    print (diff_mnt_sale)
    return render_template('index.html', title='Home', posts=posts, top_sales = top_sales, diff_mnt_sale = diff_mnt_sale, max_over_shops_capacity = max_over_shops_capacity, crnt_over_shops_capacity = crnt_over_shops_capacity, mnt_sale_shop_near_home = mnt_sale_shop_near_home, mnt_sale_supershop = mnt_sale_supershop, mnt_sale_gipershop = mnt_sale_gipershop, mnt_sale_fruit = mnt_sale_fruit, mnt_sale_vegetables = mnt_sale_vegetables, mnt_sale_greens = mnt_sale_greens, mnt_over_shop_near_home = mnt_over_shop_near_home, mnt_over_supershop = mnt_over_supershop, mnt_over_gipershop = mnt_over_gipershop, mnt_over_fruit = mnt_over_fruit, mnt_over_vegetables = mnt_over_vegetables, mnt_over_greens = mnt_over_greens)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Поздравляем, теперь вы зарегистрированный пользователь!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user, posts=user.posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Ваши изменения были сохранены.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.username.data = current_user.about_me
    return render_template('edit_profile.html', title='Изменить профиль', form=form)


@app.route('/user/<int:uid>')
def get_userinfo(uid):
    user = User.query.get(uid)
    print ('render with user_id = ', uid)
    return render_template('my_template.html', user=user)


@app.route('/pie')
def pie():
    labels = ['Большая часть', 'что-то незначительное', 'меньшая часть']
    values = [100, 15, 39]
    colors = [ "#F7464A", "#46BFBD", "#ABCDEF" ]
    return render_template('pie.html', title='Bitcoin Monthly Price in USD', max=17000, set=zip(values, labels, colors))

@app.route('/bar')
def bar():
    labels = ['Большая часть', 'что-то незначительное']
    values = [10000, 140000]
    return render_template('bar.html', title='Bitcoin Monthly Price in USD', max=150000, labels=labels, values=values)


@app.route('/top_sales')
@login_required
def top_sales():
    top_sales = get_top_sales()
    return render_template('top_sales.html', title='Топ продаж по типам магазинов', top_sales = top_sales)

def get_top_sales():
    return SumMntSale.query.all()

@app.route('/diff_mnt_sale')
@login_required
def diff_mnt_sale():
    diff_mnt_sale = get_diff_mnt_sale()
    return render_template('bar.html', title='Выполнение продаж', diff_mnt_sale = diff_mnt_sale)

def get_diff_mnt_sale():
    return DiffMntSale.query.all()

@app.route('/crnt_over_shops_capacity')
@login_required
def crnt_over_shops_capacity():
    crnt_over_shops_capacity = get_crnt_over_shops_capacity()
    return render_template('bar.html', title='Выполнение продаж', crnt_over_shops_capacity = crnt_over_shops_capacity)

def get_crnt_over_shops_capacity():
    return CrntOverShopsCapacity.query.all()    

@app.route('/max_over_shops_capacity')
@login_required
def max_over_shops_capacity():
    max_over_shops_capacity = get_max_over_shops_capacity()
    return render_template('max_over_shops_capacity.html', title='Выполнение продаж', max_over_shops_capacity = max_over_shops_capacity)

def get_max_over_shops_capacity():
    return MaxOverShopsCapacity.query.all()

@app.route('/sale_shop')
@login_required
def mnt_sale_shop_near_home():
    mnt_sale_shop_near_home = get_mnt_sale_shop_near_home()
    return render_template('sale_shop.html', title='Продажи по месяцам в магазинах у дома', mnt_sale_shop_near_home = mnt_sale_shop_near_home)

def get_mnt_sale_shop_near_home():
    return MntSaleShopNearHome.query.all()

@app.route('/sale_supershop')
@login_required
def mnt_sale_supershop():
    mnt_sale_supershop = get_mnt_sale_supershop()
    return render_template('sale_supershop.html', title='Продажи по месяцам в супермаркетах', mnt_sale_supershop = mnt_sale_supershop)

def get_mnt_sale_supershop():
    return MntSaleSupershop.query.all()

@app.route('/sale_gipershop')
@login_required
def mnt_sale_gipershop():
    mnt_sale_gipershop = get_mnt_sale_gipershop()
    return render_template('sale_gipershop.html', title='Продажи по месяцам в гипермаркетах', mnt_sale_gipershop = mnt_sale_gipershop)

def get_mnt_sale_gipershop():
    return MntSaleGipershop.query.all()

@app.route('/sale_fruit')
@login_required
def mnt_sale_fruit():
    mnt_sale_fruit = get_mnt_sale_fruit()
    return render_template('sale_fruit.html', title='Продажа фруктов по типам магазинов', mnt_sale_fruit = mnt_sale_fruit)

def get_mnt_sale_fruit():
    return MntSaleFruit.query.all()

@app.route('/sale_vegetables')
@login_required
def mnt_sale_vegetables():
    mnt_sale_vegetables = get_mnt_sale_vegetables()
    return render_template('sale_vegetables.html', title='Продажа овощей по типам магазинов', mnt_sale_vegetables = mnt_sale_vegetables)

def get_mnt_sale_vegetables():
    return MntSaleVegetables.query.all()

@app.route('/sale_greens')
@login_required
def mnt_sale_greens():
    mnt_sale_greens = get_mnt_sale_greens()
    return render_template('sale_greens.html', title='Продажа зелени по типам магазинов', mnt_sale_greens = mnt_sale_greens)

def get_mnt_sale_greens():
    return MntSaleGreens.query.all()

@app.route('/shop_near_home')
@login_required
def mnt_over_shop_near_home():
    mnt_over_shop_near_home = get_mnt_over_shop_near_home()
    return render_template('shop_near_home.html', title='Остатки товаров в магазинах у дома', mnt_over_shop_near_home = mnt_over_shop_near_home)

def get_mnt_over_shop_near_home():
    return MntOverShopNearHome.query.all()

@app.route('/supershop')
@login_required
def mnt_over_supershop():
    mnt_over_supershop = get_mnt_over_supershop()
    return render_template('supershop.html', title='Остатки товаров в супермаркетах', mnt_over_supershop = mnt_over_supershop)

def get_mnt_over_supershop():
    return MntOverSupershop.query.all()

@app.route('/gipershop')
@login_required
def mnt_over_gipershop():
    mnt_over_gipershop = get_mnt_over_gipershop()
    return render_template('gipershop.html', title='Остатки товар в гипермаркетах', mnt_over_gipershop = mnt_over_gipershop)

def get_mnt_over_gipershop():
    return MntOverGipershop.query.all()

@app.route('/fruit')
@login_required
def mnt_over_fruit():
    mnt_over_fruit = get_mnt_over_fruit()
    return render_template('fruit.html', title='Остатки фруктов по типам магазинов', mnt_over_fruit = mnt_over_fruit)

def get_mnt_over_fruit():
    return MntOverFruit.query.all()

@app.route('/vegetables')
@login_required
def mnt_over_vegetables():
    mnt_over_vegetables = get_mnt_over_vegetables()
    return render_template('vegetables.html', title='Остатки овощей по типам магазинов', mnt_over_vegetables = mnt_over_vegetables)

def get_mnt_over_vegetables():
    return MntOverVegetables.query.all()

@app.route('/greens')
@login_required
def mnt_over_greens():
    mnt_over_greens = get_mnt_over_greens()
    return render_template('greens.html', title='Остатки зелени по типам магазинов', mnt_over_greens = mnt_over_greens)

def get_mnt_over_greens():
    return MntOverGreens.query.all()

