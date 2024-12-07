def convert(text: str) -> str:
    # Replace emoticons with corresponding emoji
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    user_input = input("Enter your text: ")
    result = convert(user_input)
    print(result)

if __name__ == "__main__":
    main()
