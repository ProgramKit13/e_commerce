from flask_restful import Resource
from api import api
from ...schemas import prod_schema, sector_schema
from flask import request, make_response, jsonify, current_app
from ...entities import product
from ...services import product_service, adminPreferences_service, user_service, sector_service
import secrets
from ...decorators import admin_required
from ...schemas.validators import validator
from .consult_config import paginate
from ...models.product_model import Product
from ...models.sector_model import Sector
from flask_jwt_extended import get_jwt_identity
from .advancedfilter import paginate_advanced

##Product Register
class AdminProdRegister(Resource):
    @admin_required
    def post(self):
        errorTypes = {}
        verify = True 
        ps = prod_schema.ProdSchema()

        if 'valueResale' in request.json:
            request.json['valueResale'] = float(request.json['valueResale'])
        if 'cust' in request.json:
            request.json['cust'] = float(request.json['cust'])
        if 'tax' in request.json and request.json['tax']:
            request.json['tax'] = float(request.json['tax'])
        if 'discount' in request.json and request.json['discount']:
            request.json['discount'] = float(request.json['discount'])
        if 'weight' in request.json:
            request.json['weight'] = float(request.json['weight'])


        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            prodName = request.json['prodName']
            valueResale = request.json['valueResale']
            cust = request.json['cust']
            tax = request.json['tax']
            supplier = request.json['supplier']
            qt = request.json['qt']
            discount = request.json['discount']
            description = request.json['description']
            datePurchase = request.json['datePurchase']
            sector = request.json['sector']
            supplierCode = request.json.get('supplierCode')  
            manufacturer = request.json.get('manufacturer')
            weight = request.json.get('weight')
            dimensions = request.json.get('dimensions')
            lastUpdated = request.json.get('lastUpdated')
            reorderPoint = request.json.get('reorderPoint')
            restockTime = request.json.get('restockTime')
            warrantyInfo = request.json.get('warrantyInfo')
            batchInfo = request.json.get('batchInfo')
            expiryDate = request.json.get('expiryDate')
            materialOrIngredients = request.json.get('materialOrIngredients')
            safetyRating = request.json.get('safetyRating')
            shippingRestrictions = request.json.get('shippingRestrictions')
            barcode = request.json.get('barcode')
            weightUnit = request.json.get('weightUnit')
            dimensionsUnit = request.json.get('dimensionsUnit')
            token = secrets.token_hex(6)
        
        if lastUpdated == '':
            lastUpdated = None

        if expiryDate == '':
            expiryDate = None

        if barcode != '':
            barcodeValidate = validator.validateBarCode(barcode)
            if barcodeValidate != True:
                verify = False
                errorTypes['barcode'] = 'Invalid format.'
        
        if supplierCode != '':
            supplierCodeValidate = validator.validateSupplierCode(supplierCode)
            if supplierCodeValidate != True:
                verify = False
                errorTypes['supplierCode'] = 'Invalid format.'

        if manufacturer != '':
            manufacturerValidate = validator.validate_name(manufacturer)
            if manufacturerValidate != True:
                verify = False
                errorTypes['manufacturer'] = manufacturerValidate

        prodNameValidate = validator.validate_DiferentText(prodName)
        if prodNameValidate != True:
            verify = False
            errorTypes['prodName'] = prodNameValidate

        
        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'
        
        if type(cust) != float:
            verify = False
            errorTypes['cust'] = 'Invalid format.'


        if tax and type(tax) != float:
            verify = False
            errorTypes['tax'] = 'Invalid format.'

        if discount and type(discount) != float:
                verify = False
                errorTypes['discount'] = 'Invalid format.'

        
        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'
        
        
        sectorValidate = validator.validate_name(sector)
        if sectorValidate != True:
            verify = False
            errorTypes['sector'] = sectorValidate
        else:
            sectorName = sector_service.sector_getBy_name(sector)
            if not sectorName:
                tokenSector = secrets.token_hex(6)
                new_sector = Sector(name=sector, token=tokenSector)
                sector_service.sector_register(new_sector)
                sectorName = sector_service.sector_getBy_name(sector)
                sector = sectorName.name
            else:
                sectorName = sector_service.sector_getBy_name(sector)
                sector = sectorName.name

        if description in request.json:
            description = request.json['description']
            validateDescription = validator.validate_description(description)
            if validateDescription != True:
                verify = False
                errorTypes['description'] = validateDescription



        if weight and type(weight) != float:
            verify = False
            errorTypes['weight'] = 'Invalid format.'


        datePurchaseValidate = validator.date_validate(datePurchase)
        if datePurchaseValidate != True:
            verify = False
            errorTypes['datePurchase'] = datePurchaseValidate


        if reorderPoint and type(reorderPoint) != int:
            verify = False
            errorTypes['reorderPoint'] = 'Invalid format.'
        print(reorderPoint)
            

        if restockTime and type(restockTime) != int:
            verify = False
            errorTypes['restockTime'] = 'Invalid format.'


        supplierValidate = validator.validate_name(supplier) if supplier else True
        if supplierValidate != True:
            verify = False
            errorTypes['supplier'] = supplierValidate


        if verify:
            new_prod = product.Product(
                prodName=prodName,
                description=description,
                sector=sector,
                supplier=supplier,
                supplierCode=supplierCode,
                manufacturer=manufacturer,
                valueResale=valueResale,
                cust=cust,
                tax=tax,
                qt=qt,
                discount=discount,
                weight=weight,
                dimensions=dimensions,
                datePurchase=datePurchase,
                lastUpdated=lastUpdated,
                reorderPoint=reorderPoint,
                restockTime=restockTime,
                warrantyInfo=warrantyInfo,
                batchInfo=batchInfo,
                expiryDate=expiryDate,
                materialOrIngredients=materialOrIngredients,
                safetyRating=safetyRating,
                shippingRestrictions=shippingRestrictions,
                token=token,
                barcode=barcode,
                weightUnit=weightUnit,
                dimensionsUnit=dimensionsUnit
            )
            result = product_service.prod_register(new_prod)
            print(result)
            ref = ps.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)

###############################################

##List
class AdminShowProducts(Resource):
    @admin_required
    def get(self):
        current_user =  get_jwt_identity()
        user = user_service.get_user(current_user)  
        ps = prod_schema.ProdSchema(many=True)
        preferecesPerPageProd = adminPreferences_service.get_adminPreferencesPerpage_by_token(user)
        infoPaginate = paginate(Product, ps, preferecesPerPageProd.productsPerPage.value)
        listEnum = adminPreferences_service.listPerpageProductsEnum()
        listSectors = sector_service.sector_list()
        return make_response(jsonify({'products': infoPaginate, 'enum': listEnum, 'sectors': listSectors}), 200)


##Search       
class AdminProdSearchId(Resource):
    @admin_required
    def get(self, id):
        product = product_service.product_list_id(id)
        if product is None:
            return make_response(jsonify("Product not found"), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)
    

class AdminProdSearchFilter(Resource):
    @admin_required
    def get(self, infoSearch, typeSearch):
        try:
            current_user =  get_jwt_identity()
            user = user_service.get_user(current_user)  
            preferecesPerPageProd = adminPreferences_service.get_adminPreferencesPerpage_by_token(user)
            ps = prod_schema.ProdSchema(many=True)
            if typeSearch != 'setor' and typeSearch != 'nome' and typeSearch != 'fornecedor' and typeSearch != 'descricao' and typeSearch != 'barcode' != typeSearch != 'fabricante':
                return make_response(jsonify('Invalid search type'), 400)
            infoPaginate = paginate(Product, ps, preferecesPerPageProd.productsPerPage.value, infoSearch=infoSearch, typeSearch=typeSearch)
        except Exception as e:
            current_app.logger.error(f"Error while searching for product: {e}")
            return make_response(jsonify('Error while searching for product'), 500)

        if not infoPaginate['list']:
            return make_response(jsonify('Product not found'), 404)

        return make_response(jsonify(infoPaginate), 200)
 


###################################################
from flask import request, url_for
from sqlalchemy import or_, and_

class AdvancedSearchFilter(Resource):
    @admin_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = user_service.get_user(current_user)
            preferencesPerPageProd = adminPreferences_service.get_adminPreferencesPerpage_by_token(user)
            ps = prod_schema.ProdSchema(many=True)
            filters = request.args.to_dict()  # Get all filters from the request
            infoPaginate = paginate_advanced(Product, ps, preferencesPerPageProd.productsPerPage.value, **filters)
        except Exception as e:
            current_app.logger.error(f"Error while searching for product: {e}")
            return make_response(jsonify('Error while searching for product'), 500)

        if not infoPaginate['list']:
            return make_response(jsonify('Product not found'), 404)

        return make_response(jsonify(infoPaginate), 200)






##Update
class AdminUpdateProd(Resource):
    @admin_required
    def put(self, id):
        product_db = product_service.product_list_id(id)
        verify = True
        errorTypes = {}
        if product_db is None:
            return make_response(jsonify("Product not fount."), 404)
        ps = prod_schema.ProdSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            prodName = request.json['prodName']
            valueResale = request.json['valueResale']
            cust = request.json['cust']
            tax = request.json['tax']
            supplier = request.json['supplier']
            qt = request.json['qt']
            alterResale = request.json['alterResale']
            discount = request.json['discount']
            description = request.json['description']
            datePurchase = request.json['datePurchase']
            token = product_db.token

        
        prodNameValidate = validator.validate_name(prodName)
        if prodNameValidate != True:
            verify = False
            errorTypes['prodName'] = prodNameValidate

        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'
        
        if type(cust) != float:
            verify = False
            errorTypes['cust'] = 'Invalid format.'
        
        if tax:
            if type(tax) != float:
                verify = False
                errorTypes['tax'] = 'Invalid format.'
        
        if alterResale:
            if type(alterResale) != float:
                verify = False
                errorTypes['alterResale'] = 'Invalid format.'

        if discount:
            if type(discount) != float:
                verify = False
                errorTypes['discount'] = 'Invalid format.'
        
        if description in request.json:
            description = request.json['description']
            validateDescription = validator.validate_description(description)
            if validateDescription != True:
                verify = False
                errorTypes['description'] = validateDescription
        else:
            description = None


        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'

        
        if verify:
            upgrade_product = product.Product(prodName=prodName, valueResale=valueResale, cust=cust, tax=tax, supplier=supplier, qt=qt, alterResale=alterResale, discount=discount, description=description, datePurchase=datePurchase, token=token)
            product_service.product_update(product_db, upgrade_product)
            response = product_service.product_list_id(id)
            return make_response(ps.jsonify(response), 200)
        else:
            return make_response(jsonify(errorTypes), 404)


##Delete
class AdminDeleteProd(Resource):
    @admin_required
    def delete(self, id):
        product_db = product_service.product_list_id(id)
        if product_db is None:
            return make_response(jsonify("Product not found"), 404)
        product_service.product_delete(product_db)
        return make_response(jsonify("Product deleted successfully."), 204)



class SectorList(Resource):
    @admin_required
    def get(self):
        sectors = sector_service.sector_list()
        if not sectors:
            return make_response(jsonify("Sectors not found"), 404)
        return make_response(jsonify(sectors), 200)
    

api.add_resource(AdminShowProducts, '/axiosadmin/gestao/produtos')

api.add_resource(AdminProdRegister, '/admin_dashboard/product_register')

api.add_resource(AdminProdSearchId, '/admin_dashboard/product_search/<int:id>')

api.add_resource(AdminProdSearchFilter, '/axiosadmin/gestao/produtos/busca/<string:typeSearch>/<string:infoSearch>')

api.add_resource(AdvancedSearchFilter, '/axiosadmin/gestao/produtos/busca_avancada')

api.add_resource(AdminUpdateProd, '/admin_dashboard/product_update/<int:id>')

api.add_resource(AdminDeleteProd, '/admin_dashboard/product_delete/<int:id>')

api.add_resource(SectorList, '/axiosadmin/list_sectors')