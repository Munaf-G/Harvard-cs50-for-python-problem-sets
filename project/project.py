def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    return miles / 0.621371

def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    return kilograms / 0.453592

def main():
    while True:
        print("Unit Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kilometers to Miles")
        print("4. Miles to Kilometers")
        print("5. Pounds to Kilograms")
        print("6. Kilograms to Pounds")
        print("7. Quit")

        choice = input("Choose an option: ").strip()

        if choice == '7':
            print("Goodbye!")
            break

        value = float(input("Enter the value to convert: "))
        if choice == '1':
            result = celsius_to_fahrenheit(value)
            print(f"{value} °C is {result:.2f} °F")
        elif choice == '2':
            result = fahrenheit_to_celsius(value)
            print(f"{value} °F is {result:.2f} °C")
        elif choice == '3':
            result = kilometers_to_miles(value)
            print(f"{value} km is {result:.2f} miles")
        elif choice == '4':
            result = miles_to_kilometers(value)
            print(f"{value} miles is {result:.2f} km")
        elif choice == '5':
            result = pounds_to_kilograms(value)
            print(f"{value} lbs is {result:.2f} kg")
        elif choice == '6':
            result = kilograms_to_pounds(value)
            print(f"{value} kg is {result:.2f} lbs")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
