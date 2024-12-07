text = input("Text: ")
new_text = ""

vowels =["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(text)):
    if text[i] not in vowels:
        new_text += text[i]

print(new_text)
