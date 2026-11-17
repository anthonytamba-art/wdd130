LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            content = line.strip()

            if case_sensitive:
                if word == content:
                    return True
                else:
                    if word.lower() == content.lower():
                        return True

    return False

def word_complexity (word):
    complexity = 0

    if word_has_character(word, LOWERCASE):
        complexity += 1

    if word_has_character(word, UPPERCASE):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL_CHARACTERS):
        complexity += 1

    return complexity

def password_strength(password, min_length=10, strong_length=16):

    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure")
        return 0

    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long. Length trumps complexity. This is a good password.")
        return 5

    strength = 1 + word_complexity(password)
    return strength

def main():
    while True:
        password = input("Enter a password to test (or Q to quit): ")
        
        if password.lower() == "q": 
            print("Goodbye!")
            break
        

    strength = password_strength(password)
    print(f"Password strength: {strength} out of 5")

if __name__ == "__main__":
    main()



