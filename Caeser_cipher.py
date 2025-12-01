#Caeser Cipher.

def caesar_shift_char(ch: str, shift: int) -> str:
    """Shift a single character by 'shift' positions if it is a letter not number."""
    if 'a' <= ch <= 'z':
        base = ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)

    elif 'A' <= ch <= 'Z':
        base = ord('A')
        return chr((ord(ch) - base + shift) % 26 + base)

    else:
        # Non-alphabetic characters stay unchanged
        return ch


def encrypt(message: str, shift: int) -> str:
    """Encrypt the message by shifting letters forward."""
    return "".join(caesar_shift_char(ch, shift) for ch in message)


def decrypt(message: str, shift: int) -> str:
    """Decrypt the message by shifting letters backward."""
    return "".join(caesar_shift_char(ch,  -shift) for ch in  message)


def main():
    print("$$$ Caesar Cipher Tool By Gokul $$$")
    print("Encrypt and decrypt Your text.\n")

    while True:
        print("Choose option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "3":
            print("Exiting...!")
            break

        if choice not in ("1", "2"):
            print("Invalid choice. Try again.\n")
            continue

        message = input("\nEnter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Shift must be a number. Try again.\n")
            continue

        if choice == "1":
            encrypted = encrypt(message, shift)
            print(f"\nEncrypted message: {encrypted}\n")
        else:
            decrypted = decrypt(message, shift)
            print(f"\nDecrypted message: {decrypted}\n")


if __name__ == "__main__":
    main()
