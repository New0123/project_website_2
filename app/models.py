# Один из главных файлов ищущий и выбирающий файлы из бд
from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class SumMntSale(db.Model):
    types_shops_name = db.Column(db.String(256), primary_key=True)
    sale_date = db.Column(db.String(10), primary_key=True)
    sum_mnt_weight_sale = db.Column(db.String(256))
    sum_mnt_piece_sale = db.Column(db.String(256))

class DiffMntSale(db.Model):
    types_shops_name = db.Column(db.String(256), primary_key=True)
    sum_mnt_weight_sale = db.Column(db.Integer)
    sum_mnt_piece_sale = db.Column(db.Integer)
    sum_current_weight_sales = db.Column(db.Integer)
    sum_current_piece_sales = db.Column(db.Integer)

class MaxOverShopsCapacity(db.Model):
    types_shops_name = db.Column(db.String(256), primary_key=True)
    types_goods_name = db.Column(db.String(256), primary_key=True)
    max_over_weight_capacity = db.Column(db.Integer)
    max_over_piece_capacity = db.Column(db.Integer)

class CrntOverShopsCapacity(db.Model):
    types_shops_name = db.Column(db.String(256), primary_key=True)
    types_goods_name = db.Column(db.String(256), primary_key=True)
    max_over_weight_capacity = db.Column(db.Integer)
    max_over_piece_capacity = db.Column(db.Integer)
    current_over_weight_capacity = db.Column(db.Integer)
    current_over_piece_capacity = db.Column(db.Integer)

class MntSaleShopNearHome(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.String(256))
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer, primary_key=True)

class MntSaleSupershop(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.String(256))
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer, primary_key=True)

class MntSaleGipershop(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.String(256))
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer, primary_key=True)

class MntSaleFruit(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    good_name = db.Column(db.String(256), primary_key=True)
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256))
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntSaleVegetables(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    good_name = db.Column(db.String(256), primary_key=True)
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256))
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntSaleGreens(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256))
    good_name = db.Column(db.String(256), primary_key=True)
    sum_sales = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256))
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntOverShopNearHome(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntOverSupershop(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntOverGipershop(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    shop_name = db.Column(db.String(256), primary_key=True)
    shop_loc = db.Column(db.String(256))
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer)
    unit_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, primary_key=True)
    type_goods_id = db.Column(db.Integer)

class MntOverFruit(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    good_name = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    type_goods_id = db.Column(db.Integer)

class MntOverVegetables(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    good_name = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    type_goods_id = db.Column(db.Integer)

class MntOverGreens(db.Model):
    sale_dt_crt = db.Column(db.String(256), primary_key=True)
    types_good_name = db.Column(db.String(256))
    types_good_name_ru = db.Column(db.String(256), primary_key=True)
    good_name = db.Column(db.String(256), primary_key=True)
    over_balance = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String(256), primary_key=True)
    types_shops_name = db.Column(db.String(256), primary_key=True)
    type_shops_id = db.Column(db.Integer)
    unit_id = db.Column(db.Integer)
    type_goods_id = db.Column(db.Integer)
    





