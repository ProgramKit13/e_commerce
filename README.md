# ##E-commerce de pratileira

Um e-commerce pronto com backend api restfull e Machine Learning em Python, frontend React Js + Bootstrap. O projeto visa fornecer uma api robusta para que possa ser reutilizado com diversos modelos de frontend para e-commerce e com sistema de gestão de crédito prático.

# Libs

- `set FLASK_APP=app.py`
- `flask db init`
- `flask db migrate`
- `flask db upgrade`

# #Arquitetura
## --- Root <br>
## -- Api<br>
- Entities (captura do get e set de todas as entidades)
- Models (modelo base das estruturas)
- Views (lógica de negócio)
- Services (CRUD ORM)
- Schemas (Validação de dados)
- ..Validators(Validação de dados por REGEX)




# #Bibliotecas
- `pip install Flask`
- `pip install Flask-Migrate`
- `pip install flask-restful`
- `pip install Flask-SQLAlchemy`
- `pip install marshmallow-sqlalchemy`
- `pip install flask-marshmallow`
- `pip install mysqlclient`
- `pip install bcrypt`
- `pip install validate-docbr`