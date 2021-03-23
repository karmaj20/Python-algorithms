import random

def readFile():
    filepath = "dane.txt"

    try:
        with open(filepath, "r") as f:
            return f.read()
    finally:
        f.close()


def split():
    text = textToBinary()
    n = 64

    text8bytes = [text[i:i+n] for i in range(0, len(text), n)]
    return text8bytes


def generateKey(n):
    x = [random.randint(0, 1) for _ in range(n)]
    key = ''.join([str(elem) for elem in x])

    return key


def textToBinary():
    text = readFile()
    textAsBytes = ''.join(format(x, 'b') for x in bytearray(text, 'utf-8'))

    while(len(textAsBytes) % 64 != 0):
        textAsBytes = textAsBytes + '0'

    return textAsBytes

def code():
    textToCode = split()
    for i in range(len(textToCode)):
        key = generateKey(len(textToCode[i]))

    codedText = ""
    for i in range(len(textToCode)):
        for j in range (len(key)):
            aux = int(textToCode[i][j]) ^ int(key[j])
            codedText += str(aux)

    return codedText

def saveToFile(text):
    filepath = "codedFile.txt"

    try:
        with open(filepath, "w") as f:
            f.write(str(text))
    finally:
        f.close()

def main():
    text = code()
    saveToFile(text)

if __name__ == "__main__":
    main()
