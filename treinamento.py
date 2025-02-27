from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import time
time.clock = time.time


CONVERSAS = [
    r"C:\Users\User\Desktop\rodoviaria_bot\conversas\rodoviaria.json",
    r"C:\Users\User\Desktop\rodoviaria_bot\conversas\saudacoes.json",
]

def iniciar():
    iniciado, treinador = False, None

    try:
        robo = ChatBot(
            "Robô de Atendimento da Rodoviária de Vitória da Conquista.")
        treinador = ListTrainer(robo)

        iniciado = True
    except Exception as e:
        print(f"Ocorreu um erro ao iniciar o treinamento: {str(e)}")

    return iniciado, treinador


def carregar_conversas():
    carregadas, conversas = False, []

    try:
        for caminho_arquivo in CONVERSAS:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dicionario = json.load(arquivo)
                conversas.append(dicionario["conversas"])

                arquivo.close()
        carregadas = True
    except Exception as e:
        print(f"Ocorreu um erro ao carregar as conversas: {str(e)}")
    return carregadas, conversas


def treinar(treinador, conversas):
    treinado = False

    try:
        for conversa in conversas:
            for mensagens_resposta in conversa:
                mensagens = mensagens_resposta["mensagens"]
                resposta = mensagens_resposta["resposta"]

                print(
                    f"Treinando o robô, mensagens = {mensagens}, resposta = {resposta}")

                for mensagem in mensagens:
                    treinador.train([mensagem.lower(), resposta])
        treinado = True

    except Exception as e:
        print(f"Ocorreu um erro ao treinar o robô: {str(e)}")
    return treinado


if __name__ == "__main__":
    iniciado, treinador = iniciar()
    if iniciado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinado = treinar(treinador, conversas)
            if treinado:
                print("Treinamento concluído")
            else:
                print("Ocorreu um problema no treinamento")
