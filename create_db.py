from app import db, create_app
from app.models import User, Activity

app = create_app()
app.app_context().push()

db.create_all()

print("Banco de dados criado com sucesso!")
