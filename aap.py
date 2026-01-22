from flask import Flask
from database import Database
from rotas import tarefa_db

app = Flask(__name__)

# registra o blueprint
app.register_blueprint(tarefa_db)

if __name__ == "__main__":
    database = Database()
    database.init_database()

    print("Servidor rodando na porta 5000")

    app.run(debug=True, port=5000)
