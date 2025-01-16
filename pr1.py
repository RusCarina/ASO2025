def numara_vocale(text):
    vocale = 'aeiouAEIOU'
    contor = 0
    for caracter in text:
        if caracter in vocale:
            contor += 1
    return contor

text_input = " Ex de prop"
numar_vocale = numara_vocale(text_input)
print(f"nr voc {numara_vocale}")
