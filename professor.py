import random

def main():
    l = get_level()
    score = generate_integer(l)
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1", "2", "3"]:
            continue
        return level

def generate_integer(level):
    score = 0
    for i in range(10):
        if level == "1":
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == "2":
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == "3":
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        attempts = 0
        while attempts < 3:
            print(f"{x} + {y} = ", end="")
            answer = input()
            if answer == str(x + y):
                score += 1
                break
            else:
                print("EEE")
                attempts += 1
        if attempts == 3:
            print(f"{x} + {y} = {x + y}")
    return score

if __name__ == "__main__":
    main()
