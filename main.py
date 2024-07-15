from con import Database
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

db = None  # Remova o uso de variáveis globais desnecessárias

@app.route('/conectar', methods=['POST'])
def conectar():
    try:
        global db
        if db is None:
            user = request.form.get('user', 'pi')
            passwd = request.form.get('passwd', 'raspberry')
            database = request.form.get('database', 'random')
            db = Database(user=user, passwd=passwd, database=database)
            teste = db.conectar()

            if teste is True:
                return Response(json.dumps({'message': "Conectado"}), status=200)
            else:
                return Response(json.dumps(teste), status=500)
        else:
            return Response(json.dumps({"message": "Já conectado ao banco de dados."}), status=400)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

@app.route('/ler', methods=['GET'])
def ler_todos_os_estudantes():
    try:
        global db
        if db:
            students = db.read_students()
            if isinstance(students, dict) and "error" in students:
                return Response(json.dumps(students), status=500)
            return jsonify({"estudantes": students})
        else:
            return Response(json.dumps({"message": "Cliente não conectado."}), status=503)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

@app.route('/ler_por_pagina', methods=['GET'])
def ler_por_pagina():
    try:
        global db
        if db:
            page = request.args.get('page', 1)
            per_page = request.args.get('per_page', 10)
            students, total_records = db.read_students_paginate(page=int(page), per_page=int(per_page))
            if isinstance(students, dict) and "error" in students:
                return Response(json.dumps(students), status=500)
            response_data = {
                "estudantes": students,
                "total_records": total_records
            }
            return jsonify(response_data)
        else:
            return Response(json.dumps({"message": "Cliente não conectado."}), status=503)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

@app.route('/atualizar_estudante/<int:student_id>', methods=['PUT'])
def atualizar_estudante(student_id):
    try:
        global db
        if db:
            data = request.get_json()
            resultado_atualizacao = db.atualizar_estudante_no_banco(student_id, data)

            if resultado_atualizacao is True:
                return Response(json.dumps({'message': "Estudante atualizado com sucesso."}), status=200)
            else:
                return Response(json.dumps({"error": resultado_atualizacao}), status=500)
        else:
            return Response(json.dumps({"message": "Cliente não conectado ao banco de dados."}), status=503)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

@app.route('/deletar-por-id/<int:id>', methods=['DELETE'])
def deletar_estudante(id):
    try:
        global db
        if db:
            resultado_delecao = db.deletar_estudante(id)
            if resultado_delecao is True:
                return Response(json.dumps({"message": "aluno deletado com sucesso"}), status=200)
            else:
                return Response(json.dumps({"error": resultado_delecao}), status=500)
        else:
            return Response(json.dumps({"message": "Cliente não conectado ao banco de dados."}), status=503)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

@app.route('/inserir-estudante', methods=['POST'])
def inserir_estudante():
    try:
        global db
        if db:
            data = request.get_json()
            resultado_da_insercao = db.inserir_estudante(data)

            if resultado_da_insercao is True:
                return Response(json.dumps({"message": "aluno inserido com sucesso"}), status=200)
            else:
                return Response(json.dumps({"error": resultado_da_insercao}), status=500)
        else:
            return Response(json.dumps({"message": "Cliente não conectado ao banco de dados."}), status=503)
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
