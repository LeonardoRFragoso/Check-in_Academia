# Treinos_AB

Treinos_AB é uma aplicação web para registro de atividades de treino em academias. Permite que os usuários registrem sua presença diária, bem como a descrição das atividades realizadas em dias específicos. A aplicação inclui funcionalidades de login e registro de usuários, um painel de controle com calendário para o registro diário de atividades e visualização do histórico de presença.

## Funcionalidades

- Registro e login de usuários.
- Painel de controle com calendário mensal.
- Registro de presença diária e descrição das atividades realizadas.
- Visualização do histórico de atividades.

## Tecnologias Utilizadas

- **Backend:**
  - Flask
  - SQLAlchemy
  - Flask-Login

- **Frontend:**
  - HTML5
  - CSS3
  - UIkit
  - JavaScript

## Instalação

### Pré-requisitos

- Python 3.6 ou superior
- Virtualenv

### Passos para instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu_usuario/Treinos_AB.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd Treinos_AB
    ```
3. Crie um ambiente virtual:
    ```sh
    python3 -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```sh
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
6. Crie o banco de dados:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
7. Execute a aplicação:
    ```sh
    flask run
    ```

## Como Usar

1. Acesse `http://127.0.0.1:5000/` no seu navegador.
2. Registre-se ou faça login.
3. No painel de controle, clique no dia atual para registrar sua atividade.
4. Adicione a descrição da atividade realizada e clique em "Registrar".

## Estrutura do Projeto

```markdown
Treinos_AB/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   └── register.html
│   └── static/
│       ├── css/
│       │   └── styles.css
│       └── js/
│           └── main.js
├── migrations/
├── venv/
├── .flaskenv
├── config.py
├── requirements.txt
└── run.py

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch:
    ```sh
    git checkout -b feature/sua-feature
    ```
3. Faça suas alterações e commit:
    ```sh
    git commit -m 'Adicionei uma nova feature'
    ```
4. Envie para o repositório original:
    ```sh
    git push origin feature/sua-feature
    ```
5. Crie uma pull request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Leonardo Fragoso - leonardo.fragoso@example.com

Link do Projeto: [https://github.com/seu_usuario/Treinos_AB](https://github.com/seu_usuario/Treinos_AB)
