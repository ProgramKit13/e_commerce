from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from .views import user_views, product_view, address_views, login_views, refresh_token_views
from .views.admin import admin_user_views, admin_address_views, admin_product_views
from .models import user_model, address_model, phone_model, supplier_model, supPhone_model, userPayments_model, cart_models, product_model
