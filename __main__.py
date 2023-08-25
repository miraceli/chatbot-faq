import chatbot as chat

textos = chat.ds.textos

while True:
    try:
        pergunta = input(
            "Faça uma pergunta ou digite 'sair' para encerrar: ").strip()

        if pergunta.lower() == "sair":
            print("Encerrando...")
            break

        if not pergunta:
            print("Por favor, faça uma pergunta válida.")
            continue

        resposta = chat.chatbot(pergunta, textos)
        print("Resposta:", resposta)

    except Exception as e:
        print("Ocorreu um erro inesperado:", str(e))
