from app import create_app, db
from app.models import User

app = create_app()
app.app_context().push()

# Criação do usuário Leonardo
user = User(username='Leonardo', email='leonardo@example.com')
user.set_password('123456')
db.session.add(user)
db.session.commit()

print("Usuário Leonardo criado com sucesso!")
