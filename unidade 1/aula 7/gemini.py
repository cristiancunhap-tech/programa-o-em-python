from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JDav_M_5Pr87goRrCWU_0fqR29a3rGLY3zUt5SuzbZwg")

def atendimento_python():
    interaction_id = None

    print("Digite sua dúvida. Em breve um especialista irá atendê-lo(a):")
    while True:
        pergunta_usuario = input()

        if pergunta_usuario == "sair":
            break

        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            input=pergunta_usuario,
            system_instruction="Voce é um atendente de python. tire a duvida do usuario e peca informacoes como nome, usuario e numero de telefone",
            previous_interaction_id=interaction_id
        )

        interaction_id = interaction.id

        print(interaction.output_text)