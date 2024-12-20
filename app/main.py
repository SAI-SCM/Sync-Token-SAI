from app.utils.string_utils import reverse_string

def display_info():
    print("SAI-SCM este pregătit pentru testare și extindere!")

def calculate_sum(a, b):
    """Calculează suma a două numere."""
    return a + b

def main():
    print("Bun venit în SAI-SCM!")
    display_info()
    # Exemplu de utilizare a funcției calculate_sum
    result = calculate_sum(5, 7)
    print(f"Rezultatul sumei este: {result}")

    # Exemplu de utilizare a funcției reverse_string
    reversed_text = reverse_string("SAI-SCM")
    print(f"Text inversat: {reversed_text}")

if __name__ == "__main__":
    main()
