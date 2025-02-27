from chatterbot import ChatBot
import time
time.clock = time.time

CONFIANCA_MINIMA = 0.65


def iniciar():
    iniciado, robo = False, None
    try:
        robo = ChatBot(
            "Robô de Atendimento da Rodoviária de Vitória da Conquista.", read_only=True)

        iniciado = True
    except Exception as e:
        print(f"Ocorreu um erro ao iniciar o robô{str(e)}.")

    return iniciado, robo


def atender(robo):
    while True:
        mensagem = input("\nPara iniciar escreva uma mensagem:\n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(
                f"RodôBot: {resposta.text} \nCONFIANÇA = {resposta.confidence}\n")
        else:
            print("Rodoviária de Vitória da Conquista: Ops! Ainda não sei como responder isso, posso te ajudar em outra coisa?")


if __name__ == "__main__":
    iniciado, robo = iniciar()
    if iniciado:
        atender(robo)
