def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    """
    Interactive temperature converter.
    """
    print("Temperature Converter")
    print("-" * 30)

    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        if unit == "C":
            converted = celsius_to_fahrenheit(temp)
            print(f"{temp:.2f}°C = {converted:.2f}°F")
        elif unit == "F":
            converted = fahrenheit_to_celsius(temp)
            print(f"{temp:.2f}°F = {converted:.2f}°C")
        else:
            print("Invalid unit! Please enter C or F.")
    except ValueError:
        print("Invalid temperature! Please enter a number.")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()