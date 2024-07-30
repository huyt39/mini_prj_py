def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "auoei":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation 
phrase = input("Enter your phrase: ")
print (translator(phrase))
