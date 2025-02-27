from unittest import TestCase, main
from robo import *
import json

class TesteConversas(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.iniciado, cls.robo = iniciar()

    def criar_teste_para_mensagem(self, mensagem, resposta_esperada):
        resposta = self.robo.get_response(mensagem.lower())

        self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA, f"Confiança insuficiente para: {mensagem}")

        # Validação da resposta
        self.assertIn(resposta_esperada, resposta.text, f"Resposta incorreta para: {mensagem}")
        try:
            self.assertIn(resposta_esperada, resposta.text)
            print(f"✅ [SUCESSO] Mensagem: '{mensagem}' -> Resposta correta!\n")
        except AssertionError:
            print(f"❌ [FALHA] Mensagem: '{mensagem}'")
            print(f"   - Esperado: {resposta_esperada}")
            print(f"   - Obtido: {resposta.text}\n")
         
    def testar_saudacoes(self):
        saudacoes = {
            "olá": "Olá! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "oi": "Olá! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "oi, tudo bem?": "Olá! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "tudo bem?": "Olá! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "oi, como vai?": "Olá! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Bom dia": "Bom dia! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Olá, bom dia": "Bom dia! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Boa tarde": "Boa tarde! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Olá, boa tarde": "Boa tarde! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Boa noite": "Boa noite! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
            "Olá, boa noite": "Boa noite! Sou o robô de atendimento da Rodoviária de Vitória da Conquista. Como posso te ajudar?",
        }

        for mensagem, resposta_esperada in saudacoes.items():
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)

    def testar_rodoviaria_localizacao(self):
        mensagens = [
            "Onde a rodoviária está localizada?",
            "Onde fica a rodoviária da cidade?",
            "Qual o endereço da rodoviária?"
        ]
        resposta_esperada = "O endereço da estação de Vitória da Conquista é: Av. Dep. Ulisses, 405 - Lot. Cristo Rei, Vitória da Conquista - BA."
        
        for mensagem in mensagens:
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)

    def testar_empresas_onibus(self):
        mensagens = [
            "Quais empresas de ônibus operam na rodoviária?",
            "Quais são as principais viações?",
            "Quais companhias de ônibus atuam na cidade?"
        ]
        resposta_esperada = "Na Rodoviária de Vitória da Conquista operam várias empresas de ônibus. Entre as empresas que oferecem serviços na estação estão: Rota Transportes, Águia Branca, Cidade Sol, Guanabara, Catarinense, Edson Turismo, Expresso do Sul, Kaissara, Ouro e Prata, Penha, Planalto, Pluma, Progresso."

        for mensagem in mensagens:
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)

    def testar_destinos_interestaduais(self):
        mensagens = [
            "Quais destinos interestaduais estão disponíveis?",
            "É possível ir para outro estado por essa rodoviária?",
            "Para quais estados tem viações disponíveis?"
        ]
        resposta_esperada = "A rodoviária ofere opções para diversos estados do Brasil, como: São Paulo, Rio de Janeiro, Espirito Santo, Minas Gerais, Alagoas e também é possível ir até o Distrito Federal."

        for mensagem in mensagens:
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)

    def testar_estacionamento_disponivel(self):
        mensagens = [
            "Existe estacionamento disponível na rodoviária?",
            "Tem como estacionar lá?",
            "Posso usar o estacionamento?"
        ]
        resposta_esperada = "A estação possui estacionamento. O estacionamento é pago e fica localizado em frente a rodoviária, onde também há um local destinado ao embarque e desembarque e ponto de táxi 24 horas."

        for mensagem in mensagens:
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)

    def testar_tempo_viagem_conquista_ilheus(self):
        mensagens = [
            "Quanto tempo demora de Vitória da Conquista até Ilhéus?",
            "Quantas horas gasta de Vitória da Conquista a Ilhéus?",
            "Vitória da Conquista para Ilhéus demora muito?"
        ]
        resposta_esperada = "A média de tempo entre as duas cidades é de 5h."

        for mensagem in mensagens:
            with self.subTest(mensagem=mensagem):
                self.criar_teste_para_mensagem(mensagem, resposta_esperada)


if __name__ == "__main__":
    main()
