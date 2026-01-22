from flask import Blueprint, request, jsonify
from tarefa import Tarefa

tarefa_db = Blueprint('tarefas', __name__)


@tarefa_db.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()

    nova_tarefa = Tarefa(titulo=dados['titulo'])
    nova_tarefa.save()

    return jsonify(nova_tarefa.to_dict()), 201

    
    

