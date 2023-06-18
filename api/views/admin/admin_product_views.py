from flask_restful import Resource
from api import api
from ...schemas import prod_schema
from flask import request, make_response, jsonify, current_app
from ...entities import product
from ...services import product_service, adminPreferences_service, user_service, sector_service
import secrets
from ...decorators import admin_required
from ...schemas.validators import validator
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
        
        prodNameValidate = validator.validateGlobalText(prodName, True, False, 3, 100)
        if prodNameValidate != True:
            verify = False
            errorTypes['prodName'] = prodNameValidate

        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'

        
        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'

        if manufacturer != '':
            manufacturerValidate = validator.validateGlobalText(manufacturer, False, False, 3, 100)
            if manufacturerValidate != True:
                verify = False
                errorTypes['manufacturer'] = manufacturerValidate

        
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

        
        if cust != '':
            if type(cust) != float:
                verify = False
                errorTypes['cust'] = 'Invalid format.'


        if tax != '':
            if tax and type(tax) != float:
                verify = False
                errorTypes['tax'] = 'Invalid format.'

        if discount != '':
            if discount and type(discount) != float:
                    verify = False
                    errorTypes['discount'] = 'Invalid format.'
        
        
        if sector != '':
            sectorValidate = validator.validateGlobalText(sector, False, False, 3, 100)
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
            validateDescription = validator.validateGlobalText(description, False, False, 3, 2048)
            if validateDescription != True:
                verify = False
                errorTypes['description'] = validateDescription



        if weight and type(weight) != float:
            verify = False
            errorTypes['weight'] = 'Invalid format.'

        if datePurchase == '':
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


        if supplier != '':
            supplierValidate = validator.validateGlobalText(supplier, False, False, 3, 100)
            if supplierValidate != True:
                verify = False
                errorTypes['supplier'] = supplierValidate

        if warrantyInfo != '':
            warrantyInfoValidate = validator.validateGlobalText(warrantyInfo, False, False, 3, 100)
            if warrantyInfoValidate != True:
                verify = False
                errorTypes['warrantyInfo'] = warrantyInfoValidate
        
        if batchInfo != '':
            batchInfoValidate = validator.validateGlobalText(batchInfo, False, False, 3, 100)
            if batchInfoValidate != True:
                verify = False
                errorTypes['batchInfo'] = batchInfoValidate

        if materialOrIngredients != '':
            materialOrIngredientsValidate = validator.validateGlobalText(materialOrIngredients, False, False, 3, 100)
            if materialOrIngredientsValidate != True:
                verify = False
                errorTypes['materialOrIngredients'] = materialOrIngredientsValidate

        if safetyRating != '':
            safetyRatingValidate = validator.validateGlobalText(safetyRating, False, False, 3, 100)
            if safetyRatingValidate != True:
                verify = False
                errorTypes['safetyRating'] = safetyRatingValidate

        if shippingRestrictions != '':
            shippingRestrictionsValidate = validator.validateGlobalText(shippingRestrictions, False, False, 3, 100)
            if shippingRestrictionsValidate != True:
                verify = False
                errorTypes['shippingRestrictions'] = shippingRestrictionsValidate


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
            ref = ps.jsonify(result)
            return make_response(ref, 201)
        else:
            return make_response(jsonify(errorTypes), 404)

###############################################


##Search       
class AdminGetProdToken(Resource):
    @admin_required
    def get(self, token):
        product = product_service.product_list_token(token)
        if product is None:
            return make_response(jsonify("Product not found"), 404)
        ps = prod_schema.ProdSchema()
        return make_response(ps.jsonify(product), 200)
    

####List and search
class GetAllandSearch(Resource):
    @admin_required
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = user_service.get_user(current_user)
            preferencesPerPageProd = adminPreferences_service.get_adminPreferencesPerpage_by_token(user)
            ps = prod_schema.ProdSchema(many=True)
            filters = request.args.to_dict() 
            if 'per_page' in filters and filters['per_page'] != 'undefined':
                per_page = int(filters.pop('per_page'))
            else:
                per_page = preferencesPerPageProd.productsPerPage.value
            infoPaginate = paginate_advanced(Product, ps, per_page, **filters)
        except Exception as e:
            current_app.logger.error(f"Error while searching for product: {type(e).__name__} {e}")

            return make_response(jsonify('Error while searching for product'), 500)

        if not infoPaginate['list']:
            return make_response(jsonify('Not product registred'), 202)

        return make_response(jsonify(infoPaginate), 200)



##Update
class AdminUpdateProd(Resource):
    @admin_required
    def put(self, token):
        product_db = product_service.product_list_token(token)
        verify = True
        errorTypes = {}
        if product_db is None:
            return make_response(jsonify("Product not fount."), 404)
        ps = prod_schema.ProdSchema()
        validate = ps.validate(request.json)
        print(validate)
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



        if validate:
            return make_response(jsonify(validate), 404)
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
            token_db = product_db.token

        prodNameValidate = validator.validateGlobalText(prodName, True, False, 3, 100)
        if prodNameValidate != True:
            verify = False
            errorTypes['prodName'] = prodNameValidate

        if type(valueResale) != float:
            verify = False
            errorTypes['valueResale'] = 'Invalid format.'

        
        if type(qt) != int:
            verify = False
            errorTypes['qt'] = 'Invalid format.'

        if manufacturer != '':
            manufacturerValidate = validator.validateGlobalText(manufacturer, False, False, 3, 100)
            if manufacturerValidate != True:
                verify = False
                errorTypes['manufacturer'] = manufacturerValidate

        
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

        
        if cust != '':
            if type(cust) != float:
                verify = False
                errorTypes['cust'] = 'Invalid format.'


        if tax != '':
            if tax and type(tax) != float:
                verify = False
                errorTypes['tax'] = 'Invalid format.'

        if discount != '':
            if discount and type(discount) != float:
                    verify = False
                    errorTypes['discount'] = 'Invalid format.'
        
        
        if sector != '':
            sectorValidate = validator.validateGlobalText(sector, False, False, 3, 100)
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
            validateDescription = validator.validateGlobalText(description, False, False, 3, 2048)
            if validateDescription != True:
                verify = False
                errorTypes['description'] = validateDescription



        if weight and type(weight) != float:
            verify = False
            errorTypes['weight'] = 'Invalid format.'

        if datePurchase == '':
            datePurchaseValidate = validator.date_validate(datePurchase)
            if datePurchaseValidate != True:
                verify = False
                errorTypes['datePurchase'] = datePurchaseValidate


        if reorderPoint and type(reorderPoint) != int:
            verify = False
            errorTypes['reorderPoint'] = 'Invalid format.'

            

        if restockTime and type(restockTime) != int:
            verify = False
            errorTypes['restockTime'] = 'Invalid format.'


        if supplier != '':
            supplierValidate = validator.validateGlobalText(supplier, False, False, 3, 100)
            if supplierValidate != True:
                verify = False
                errorTypes['supplier'] = supplierValidate

        if warrantyInfo != '':
            warrantyInfoValidate = validator.validateGlobalText(warrantyInfo, False, False, 3, 100)
            if warrantyInfoValidate != True:
                verify = False
                errorTypes['warrantyInfo'] = warrantyInfoValidate
        
        if batchInfo != '':
            batchInfoValidate = validator.validateGlobalText(batchInfo, False, False, 3, 100)
            if batchInfoValidate != True:
                verify = False
                errorTypes['batchInfo'] = batchInfoValidate

        if materialOrIngredients != '':
            materialOrIngredientsValidate = validator.validateGlobalText(materialOrIngredients, False, False, 3, 100)
            if materialOrIngredientsValidate != True:
                verify = False
                errorTypes['materialOrIngredients'] = materialOrIngredientsValidate

        if safetyRating != '':
            safetyRatingValidate = validator.validateGlobalText(safetyRating, False, False, 3, 100)
            if safetyRatingValidate != True:
                verify = False
                errorTypes['safetyRating'] = safetyRatingValidate

        if shippingRestrictions != '':
            shippingRestrictionsValidate = validator.validateGlobalText(shippingRestrictions, False, False, 3, 100)
            if shippingRestrictionsValidate != True:
                verify = False
                errorTypes['shippingRestrictions'] = shippingRestrictionsValidate
        

        if verify:
            new_product = product.Product(prodName=prodName, valueResale=valueResale, qt=qt, manufacturer=manufacturer, lastUpdated=lastUpdated, expiryDate=expiryDate, barcode=barcode, supplierCode=supplierCode, cust=cust, tax=tax, discount=discount, sector=sector, description=description, weight=weight, datePurchase=datePurchase, reorderPoint=reorderPoint, restockTime=restockTime, supplier=supplier, warrantyInfo=warrantyInfo, batchInfo=batchInfo, materialOrIngredients=materialOrIngredients, safetyRating=safetyRating, shippingRestrictions=shippingRestrictions, token=token_db, weightUnit=weightUnit, dimensions=dimensions, dimensionsUnit=dimensionsUnit)
            result = product_service.product_update(product_db, new_product)
            return make_response(jsonify(result), 200)
        else:
            return make_response(jsonify(errorTypes), 400)        


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
            return make_response(jsonify("Sectors not found"), 202)
        return make_response(jsonify(sectors), 200)
    

api.add_resource(AdminProdRegister, '/admin_dashboard/product_register')

api.add_resource(AdminGetProdToken, '/axiosadmin/products/getByToken/<string:token>')

api.add_resource(GetAllandSearch, '/axiosadmin/gestao/produtos')

api.add_resource(AdminUpdateProd, '/axiosadmin/products/products_update/<string:token>')

api.add_resource(AdminDeleteProd, '/admin_dashboard/product_delete/<int:id>')

api.add_resource(SectorList, '/axiosadmin/list_sectors')