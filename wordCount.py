
def wordCount(text):
    words = text.split()
    print(words)

    return len(words)

def getStrippedText(filename):
    with open(filename, "r") as f:
        txt = f.read()

    stripped_txt = ""
    for letter in txt:
        if letter.isalnum() or letter in [" ", "\t", "\n"]:
            stripped_txt += letter

    return stripped_txt


def main():
    filename = "experiments/outputs/trial3.txt"

    text = getStrippedText(filename)
    print(wordCount(text))

if __name__ == "__main__":
    main()







