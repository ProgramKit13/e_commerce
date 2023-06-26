from flask import request, url_for
from sqlalchemy import or_, and_

def paginate_advanced(model, schema, per_page, **filters):
    page = int(request.args.get('page', 1))
    search_fields = ['produto_nome', 'produto_descricao', 'produto_setor', 'produto_fornecedor', 'produto_barcode', 'produto_fabricante', 'fornecedor_nome', 'fornecedor_cnpj']
    model_filters = []
    translated_filters = {}
    for field, value in filters.items():
        if field in search_fields:
            translated_field = translate_search_field(field)
            model_filters.append(getattr(model, translated_field).ilike(f'%{value}%'))
            translated_filters[translated_field] = value
        elif hasattr(model, field):  # Add filter for other model fields
            model_filters.append(getattr(model, field) == value)
            translated_filters[field] = value

    query = model.query.filter(and_(*model_filters))
    page_obj = query.paginate(page=page, per_page=per_page)
    next_url = url_for(request.endpoint, page=page_obj.next_num if page_obj.has_next else page_obj.page, per_page=per_page, **translated_filters)
    prev_url = url_for(request.endpoint, page=page_obj.prev_num if page_obj.has_prev else page_obj.page, per_page=per_page, **translated_filters)

    return {
        'list': schema.dump(page_obj.items),
        'next': next_url,
        'prev': prev_url,
        'total': page_obj.total,
        'pages': page_obj.pages,
        'page': page_obj.page,
        'per_page': page_obj.per_page
    }


def translate_search_field(field):
    return {
        'produto_nome': 'prodName',
        'produto_descricao': 'description',
        'produto_setor': 'sector',
        'produto_fornecedor': 'supplier',
        'produto_barcode': 'barcode',
        'produto_fabricante': 'manufacturer',
        'fornecedor_nome': 'supplierName',
        'fornecedor_cnpj': 'supplierCnpj'
    }.get(field, field)



