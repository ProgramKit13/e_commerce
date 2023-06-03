from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_mercadopago import Mercadopago
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)
mercadopago = Mercadopago(app)
CORS(app)
from .views import user_views, product_view, address_views, login_views, refresh_token_views, cart_views, payment_view
from .views.admin import admin_user_views, admin_address_views, admin_product_views, admin_supplier_views, adminPreferences_views
from .models import user_model, address_model, supplier_model, userPayments_model, cart_model, product_model
