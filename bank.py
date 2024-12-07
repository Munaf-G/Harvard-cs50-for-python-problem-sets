def main():
    greeting = input("Enter a greeting: ").strip()

    if greeting.lower().startswith("hello"):
        print("$0")
    elif greeting.lower().startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
