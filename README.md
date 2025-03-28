### English version

```bash
Chatbot
This is a simple Python chatbot that responds to questions based on a predefined list of texts. It uses natural language processing (NLP) to find the most relevant response to the user's question. The objective is to exemplify how an LLM works and the main NLP concepts.

Features
Text processing to remove stopwords and perform stemming.
Calculation of similarity between the user's question and predefined texts.
Response with the most similar found text.

Setup
Make sure you have Python installed on your system. Additionally, you'll need the libraries listed in the requirements.txt file. To install them, run:

pip install -r requirements.txt

Usage
To use this Python chatbot, follow the steps below:

Clone this repository to your local machine:

git clone https://github.com/miraceli/chatbot-faq.git

Navigate to the project directory:

cd chatbot-faq

Activate your virtual environment (if you're using one with .env):

source .env/bin/activate

Run the chatbot:

python3 __main__.py

Enter a question when prompted. The chatbot will respond with the best match found in the predefined texts.

Predefined Texts
The chatbot uses a list of predefined texts stored in the dataset.py file. These texts serve as a basis for responding to user questions.

Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request.
```

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
   git clone https://github.com/miraceli/chatbot-faq.git
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
