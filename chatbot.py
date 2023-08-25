import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import dataset as ds

LIMIT_SIMILARITY = 0.05

nltk.download('stopwords')
nltk.download('punkt')

nltk.data.path.append(nltk.data.find('corpora'))


def preprocess_text(text):
    """
    Pré-processa um texto removendo stopwords, fazendo stemming e retornando o texto limpo.

    Args:
        text (str): O texto a ser pré-processado.

    Returns:
        str: O texto pré-processado.
    """
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words("portuguese"))
    words = [word for word in words if word not in stop_words]

    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return " ".join(words)


def chatbot(pergunta, textos):
    """
    Responde a uma pergunta com base em uma lista de textos pré-definidos.

    Args:
        pergunta (str): A pergunta feita pelo usuário.
        textos (dict): Um dicionário de textos pré-definidos.

    Returns:
        str: A melhor resposta encontrada.
    """
    preprocessed_question = preprocess_text(pergunta)

    best_similarity = -1
    best_response = "Nenhum resultado encontrado."

    for chave, texto in textos.items():
        preprocessed_text = preprocess_text(texto)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(
            [preprocessed_text, preprocessed_question])

        similarity_scores = cosine_similarity(tfidf_matrix)

        similarity_score = similarity_scores[0][1]

        if similarity_score >= LIMIT_SIMILARITY and similarity_score > best_similarity:
            best_similarity = similarity_score
            best_response = texto

    return best_response
