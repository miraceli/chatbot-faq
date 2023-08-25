# Chatbot

Este é um simples chatbot em Python que responde a perguntas com base em uma lista de textos pré-definidos. Ele utiliza processamento de linguagem natural (NLP) para encontrar a resposta mais relevante para a pergunta feita pelo usuário.

## Funcionalidades

- Processamento de texto para remover stopwords e realizar stemming.
- Cálculo da similaridade entre a pergunta do usuário e os textos pré-definidos.
- Resposta com o texto mais similar encontrado.

## Configuração

Certifique-se de ter o Python instalado em seu sistema. Além disso, você precisará das bibliotecas listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar este chatbot em Python, siga as etapas abaixo:

1. Clone este repositório em sua máquina local:

   ```bash
   git clone [https://github.com/seu-usuario/seu-projeto.git](https://github.com/miraceli/chatbot-faq.git)
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd chatbot-faq
   ```

3. Ative seu ambiente virtual (caso você esteja usando um ambiente virtual com a .env):

   ```bash
   source .env/bin/activate
   ```

4. Execute o chatbot:

   ```bash
   python3 __main__.py
   ```

5. Digite uma pergunta quando solicitado. O chatbot responderá com a melhor correspondência encontrada nos textos pré-definidos.

## Textos Pré-definidos

O chatbot utiliza uma lista de textos pré-definidos armazenados no arquivo `dataset.py`. Estes textos são usados como base para responder às perguntas dos usuários.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
