
def wordCount(text:str):
    """
    Returns the number of words and average length of words in a text
    """
    words = text.split()
    print(words)
    avg = 0

    wc = len(words)
    #find avg
    totalChars = sum(len(count) for count in words) 
    print(totalChars)
    try:
        avg = totalChars / wc
    # Prevents errors if there's an empty file with wc == 0
    except ZeroDivisionError:
        avg = None

    return len(words), avg 



    

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







