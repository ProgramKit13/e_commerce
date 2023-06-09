from flask import request, url_for
from sqlalchemy import or_, and_

def paginate_advanced(model, schema, per_page, **filters):
    page = int(request.args.get('page', 1))
    if 'per_page' in filters and filters['per_page'] != 'undefined':
        per_page = int(filters.pop('per_page'))

    search_fields = ['nome', 'descricao', 'setor', 'fornecedor', 'barcode', 'fabricante']
    model_filters = []
    for field, value in filters.items():
        if field in search_fields:
            field = translate_search_field(field)
            model_filters.append(getattr(model, field).ilike(f'%{value}%'))
        elif hasattr(model, field):  # Add filter for other model fields
            model_filters.append(getattr(model, field) == value)

    query = model.query.filter(and_(*model_filters))

    page_obj = query.paginate(page=page, per_page=per_page)

    next_url = url_for(request.endpoint, page=page_obj.next_num if page_obj.has_next else page_obj.page, per_page=per_page, **filters)
    prev_url = url_for(request.endpoint, page=page_obj.prev_num if page_obj.has_prev else page_obj.page, per_page=per_page, **filters)

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
        'nome': 'prodName',
        'descricao': 'description',
        'setor': 'sector',
        'fornecedor': 'supplier',
        'barcode': 'barcode',
        'fabricante': 'manufacturer'
    }.get(field, field)



