import s2t

speech = ""

while True:
    response = input("Type \"s2t\" to start speech to text: ")
    if response == "s2t":
        speech = s2t.s2t()
        print(speech)
    elif response == "quit":
        break