from cs50 import get_string


def contar_palavras(string):
    # numero de palavras
    return(len(string.strip().split(" ")))
# ==========================================================================================================


def contar_letras(string):
    letras = 0
    for char in string:
        if char.isalpha():
            letras += 1
    return letras
# ==========================================================================================================


def contar_frases(string):
    frases = 0
    for char in string:
        if char == '.' or char == '?' or char == '!':
            frases += 1
    return frases
# ==========================================================================================================


text = get_string("Text: ")
palavras = contar_palavras(text)
letras = contar_letras(text)
frases = contar_frases(text)
# índice Coleman-Liau: 0.0588 * L - 0.296 * S - 15.8 ,
# L é o número médio de letras por 100 palavras no texto e
# S é o número médio de sentenças por 100 palavras no texto.

index = 0.0588 * ((letras / palavras) * 100) - 0.296 * ((frases / palavras) * 100) - 15.8
index = round(index)  # Coleman-Liau


if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade " + str(index))