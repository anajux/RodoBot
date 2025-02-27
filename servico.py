from flask import Flask, jsonify
from robo import *

servico = Flask("RodoVCABot")
iniciado, robo = iniciar()


@servico.get("/")
def get_info():
    info = {
        "descricao": "Robô de Atendimento da Rodoviária de Vitória da Conquista.",
        "versao": "0.0.1"
    }
    return jsonify(info)


@servico.get("/responder/<mensagem>")
def responder(mensagem):
    resposta = robo.get_response(mensagem.lower())

    return jsonify({
        "resposta": resposta.text,
        "confianca": resposta.confidence
    })


if __name__ == "__main__":
    if iniciado:
        servico.run(debug=True)
