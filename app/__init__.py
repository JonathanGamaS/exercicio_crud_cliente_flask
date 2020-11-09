from flask import Flask, request
import json
import mysql.connector
import hmac
import hashlib
import base64

app = Flask(__name__)

secret_key = '52d3f853c19f8b63c0918c126422aa2d99b1aef33ec63d41dea4fadf19406e54'


def conexao_db():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'clientes'
    }
    connection = mysql.connector.connect(**config)
    return connection


def get_clientes():
    connection = conexao_db()
    try:
        cursor = connection.cursor()
        cursor.execute('select id, nome, email from registro_cliente')
        results = [{id: f'{nome}- {email}'} for (id, nome, email) in cursor]
        cursor.close()
        encoded_results = encode_response(results)
        return encoded_results
    except Exception as e:
        raise e
    finally:
        connection.close()


def post_cliente(nome, email, senha):
    connection = conexao_db()
    try:
        cursor = connection.cursor()
        senha_enc = codificando_senha(senha)
        cursor.execute(f"INSERT INTO registro_cliente (nome, email, senha) VALUES ('{nome}', '{email}', '{senha_enc}')")
        connection.commit()
        cursor.close()
        return 'Cadastro realizado com sucesso'
    except Exception as e:
        raise e
    finally:
        connection.close()


def put_cliente(id, nome, email):
    connection = conexao_db()
    try:
        cursor = connection.cursor()
        cursor.execute(f"update registro_cliente set nome = '{nome}', email = '{email}' where id = {id}")
        connection.commit()
        cursor.close()
        return 'Modificacao realizada com sucesso'
    except Exception as e:
        raise e
    finally:
        connection.close()


def delete_cliente(id):
    connection = conexao_db()
    try:
        cursor = connection.cursor()
        cursor.execute(f"delete from registro_cliente where id = {id}")
        connection.commit()
        cursor.close()
        return 'Exclusao realizada com sucesso'
    except Exception as e:
        raise e
    finally:
        connection.close()


def update_password(id, senha):
    connection = conexao_db()
    try:
        cursor = connection.cursor()
        senha_enc = codificando_senha(senha)
        data = (senha_enc, id)
        query = """ UPDATE registro_cliente
                    SET senha = %s
                    WHERE id = %s """
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        return 'Senha atualizada com sucesso'
    except Exception as e:
        raise e
    finally:
        connection.close()


def encode_response(response):
    header = json.dumps({
        'typ': 'JWT',
        'alg': 'HS256'
    }).encode()

    payload = json.dumps(response).encode()

    b64_header = base64.urlsafe_b64encode(header).decode()
    b64_payload = base64.urlsafe_b64encode(payload).decode()

    signature = hmac.new(
        key=secret_key.encode(),
        msg=f'{b64_header}.{b64_payload}'.encode(),
        digestmod=hashlib.sha256
    ).digest()

    JWT = f'{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}'
    return JWT


def codificando_senha(senha):
    senha_codificada = ''
    for letra in senha:
        senha_codificada=senha_codificada+chr(ord(letra)+2)
    return senha_codificada


@app.route('/clientes', methods=['GET'])
def index():
    return get_clientes(), 200


@app.route('/cadastro', methods=['POST'])
def adicionar_cadastro():
    if request.method == 'POST':
        try:
            content = request.get_json()
            nome = content["nome"]
            email = content["email"]
            senha = content["senha"]
            response = post_cliente(nome, email, senha)
            return json.dumps(response), 200
        except Exception as e:
            raise e
    else:
        return json.dumps("Metodo invalido"), 400


@app.route('/cliente/<id>', methods=['PUT', 'DELETE'])
def modificar_cadastro(id):
    try:
        if request.method == 'PUT':
            content = request.get_json()
            nome = content["nome"]
            email = content["email"]
            response = put_cliente(id, nome, email)
            return json.dumps(response), 200
        if request.method == 'DELETE':
            response = delete_cliente(id)
            return json.dumps(response), 200
        else:
            return json.dumps("Metodo invalido"), 400
    except Exception as e:
        raise e


@app.route('/modificar_senha/<id>', methods=['PUT'])
def modificar_senha(id):
    try:
        if request.method == 'PUT':
            content = request.get_json()
            senha = content["senha"]
            response = update_password(id, senha)
            return json.dumps(response), 200
        else:
            return json.dumps("Metodo invalido"), 400
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(host='0.0.0.0')



if __name__ == "__main__":
    app.run()