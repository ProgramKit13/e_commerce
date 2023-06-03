from flask import request, url_for
from sqlalchemy import or_

def paginate(model, schema, perpage, prodName=None):
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', perpage)
    if per_page != 'undefined':
        per_page = int(per_page)
    else:
        per_page = int(perpage)  # use default perpage value

    if prodName:  # If a product name is provided, filter the query
        search = f'%{prodName}%'
        query = model.query.filter(or_(model.prodName.ilike(search), model.description.ilike(search)))
    else:  # Otherwise, do not filter the query
        query = model.query

    page_obj = query.paginate(page=page, per_page=per_page)

    view_args = request.view_args.copy()
    if prodName:
        view_args['prodName'] = prodName

    next = url_for(request.endpoint, page=page_obj.next_num if page_obj.has_next else page_obj.page, per_page=per_page, **view_args)
    prev = url_for(request.endpoint, page=page_obj.prev_num if page_obj.has_prev else page_obj.page, per_page=per_page, **view_args)

    return {
        'list': schema.dump(page_obj.items),
        'next': next,
        'prev': prev,
        'total': page_obj.total,
        'pages': page_obj.pages,
        'page': page_obj.page,
        'per_page': page_obj.per_page
    }