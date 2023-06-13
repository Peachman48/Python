phrase = input("Ingrese una frase: ")
vowels = ""
for vowels in phrase:
    if (
        phrase == "a"
        or phrase == "e"
        or phrase == "i"
        or phrase == "o"
        or phrase == "u"
    ):
        print(vowels)
