import re
import random
import requests
from bs4 import BeautifulSoup


# Functie care foloseste cautarea Google pentru a gasi un raspuns la o intrebare
def answer_question(question):
    # Codul de mai jos creeaza URL-ul pentru a face o cautare pe yahoo
    google_search_url = "https://ro.search.yahoo.com/search?p="
    # Inlocuieste spatiile din intrebare cu + pentru a putea face o cautare valida pe Google
    search_query = question.replace(" ", "+")
    # Creeaza URL-ul final de cautare
    search_url = google_search_url + search_query
    # Foloseste requests pentru a face o cerere HTTP catre URL-ul de cautare
    response = requests.Session().get(search_url)
    # Verifica daca raspunsul este valid
    if response.status_code == 200:
        # Daca raspunsul este valid, foloseste BeautifulSoup pentru a parse HTML-ul
        soup = BeautifulSoup(response.text, "html.parser")
        # Cauta primul element <div> din pagina care are clasa "fc-falcon"
        # Acesta reprezinta raspunsul
        answer_div = soup.find("span", class_="fc-falcon")
        # Daca s-a gasit un raspuns, il returneaza
        # Daca nu, returneaza mesajul "Nu am gasit un raspuns la aceasta intrebare."
        if answer_div:
            return answer_div.text
        else:
            return "I did not find an answer to this question."
    # Daca raspunsul nu este valid, returneaza mesajul "A aparut o eroare in timpul cautarii pe Google."
    else:
        return "An error occurred during the search."


# Functia de mai jos poate fi folosita pentru a verifica daca o propozitie este o intrebare
def is_question(sentence):
    # Foloseste o expresie regulata pentru a verifica daca propozitia se termina cu semnele de intrebare
    return bool(re.search(r'\?$', sentence))


# Functia de mai jos poate fi folosita pentru a raspunde la o propozitie neintrebatoare
def handle_statement(statement):
    # A
    # Creeaza o lista de raspunsuri posibile pentru propozitii neintrebatoare
    non_questions_answers = [
        "I understand. Tell me more.",
        "Oh, okay. What else do you want to know??",
        "Hmm, interesant. Ce altceva vrei sa discutam?",
        "I didn't quite understand what you meant. More clearly, please.",
        "Yes, that's right. What else do you want to discuss?"
    ]

    # Alege un raspuns aleator din lista de mai sus
    answer = random.choice(non_questions_answers)

    # Returneaza raspunsul ales
    return answer


# Functia de mai jos poate fi folosita pentru a determina daca un cuvant este un sinonim pentru "salut"
def is_greeting(word):
    # Creeaza o lista de cuvinte care sunt sinonime pentru "salut"
    greetings = ["hello", "salut", "hei", "hi"]
    # Verifica daca cuvantul dat ca argument se afla in lista de mai sus
    return word.lower() in greetings


# Functia de mai jos poate fi folosita pentru a raspunde la un salut
def handle_greeting(greeting):
    # Creeaza o lista de raspunsuri posibile la salut
    greetings_answers = [
        "Hello! What is your name?",
        "Hi! What is your name?",
        "Hei! What is your name?",
        "Hello! What is your name?",
    ]
    # Alege un raspuns aleator din lista de mai sus
    answer = random.choice(greetings_answers)
    # Returneaza raspunsul ales
    return answer


# Functia de mai jos poate fi folosita pentru a raspunde la orice alta propozitie
def handle_other(other):
    # Creeaza o lista de raspunsuri posibile pentru propozitii care nu sunt intrebari sau saluturi
    other_answers = [
        "I don't quite understand what you mean.",
        "I'm sorry, I didn't understand what you meant.",
        "Can you say this more clearly?",
        "I didn't understand very well. Can you help me?",
    ]
    # Alege un raspuns aleator din lista de mai sus
    answer = random.choice(other_answers)
    # Returneaza raspunsul ales
    return answer


# Functia de mai jos poate fi folosita pentru a raspunde la orice propozitie
def get_response(sentence):
    #
    # Verifica daca propozitia este o intrebare
    if is_question(sentence):
        # Daca este o intrebare, foloseste functia answer_question pentru a raspunde
        return answer_question(sentence)

    # Verifica daca primul cuvant din propozitie este un sinonim pentru "salut"
    if is_greeting(sentence.split()[0]):
        # Daca este un salut, foloseste functia handle_greeting pentru a raspunde
        return handle_greeting(sentence)

    # Daca propozitia nu este nici o intrebare nici un salut, foloseste functia handle_other pentru a raspunde
    return handle_other(sentence)


# Functia de mai jos poate fi folosita pentru a porni chatbot-ul
def start_chatbot():
    # Afiseaza mesajul de bun venit
    print("Welcome to my chatbot! What is your name?")
    # Citeste numele utilizatorului de la tastatura
    user_name = input("> ")
    # Afiseaza un mesaj de bun venit
    print(f"Hello, {user_name}! What do you want to know today?")
    # Seteaza variabila running la True pentru a indica ca chatbot-ul ruleaza
    running = True
    # Cat timp chatbot-ul ruleaza:
    while running:
        # Citeste o linie de la tastatura
        user_input = input("> ")
        # Verifica daca utilizatorul a scris cuvantul "close"
        if user_input.lower() == "close":
            # Daca da, seteaza variabila running la False pentru a opri chatbot-ul
            running = False
            # Afiseaza un mesaj de inchidere
            print("Goodbye! I hope to see you soon.")
        # Daca utilizatorul nu a scris cuvantul "close":
        else:
            # Foloseste functia get_response pentru a gasi un raspuns la propozitia utilizatorului
            response = get_response(user_input)
            # Afiseaza raspunsul
            print(response)


# Porneste chatbot-ul folosind functia start_chatbot
start_chatbot()