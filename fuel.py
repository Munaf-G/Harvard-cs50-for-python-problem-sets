def main():
    while True:
        fraction = input("Fraction: ")

        try:
            x, y = map(int, fraction.split('/'))

            if y == 0:
                print("Invalid input. Please enter a valid fraction.")
                continue
            if x > y:
                print("Invalid input. Please enter a valid fraction.")
                continue

            percentage = (x / y) * 100

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            break

        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
