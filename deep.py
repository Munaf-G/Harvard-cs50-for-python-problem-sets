answer = input("what is the answer to the greatest question of life, the universe, and everything? ")
answer=answer.lower().strip()
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("yes")
else:
    print("no")
