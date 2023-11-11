def caesar_cipher(action, key, text, permutation = None):
  original_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabet = original_alphabet
  result = ""
  
  if permutation:
    # Remove duplicate letters from permutation
    permutation = "".join(dict.fromkeys(permutation))

    # Remove letters from alphabet that are in permutation
    for letter in permutation:
      if letter in alphabet:
        alphabet = alphabet.replace(letter, "")

    # Add permutation to the beginning of alphabet
    alphabet = permutation + alphabet
    print("Original Alphabet:", original_alphabet)
    print("Altered Alphabet:", alphabet)


  for letter in text:
    if letter.isalpha():
      index = alphabet.find(letter.upper())
      if action == "encrypt":
        result += alphabet[(index + key) % 26]
      elif action == "decrypt":
        result += alphabet[(index - key) % 26]

  return result

def get_valid_key():
  while True:
    key = input("Enter the key (1st key, an integer between 1-25): ")
    if key.isdigit() and 0 < int(key) < 26:
        return int(key)
    else:
        print("Invalid key. Please enter a valid key (1-25).")

def get_valid_text(prompt):
  while True:
    text = input(prompt)
    text = text.replace(" ", "").upper()
    if text.isalpha():
      return text
    else:
      print("Invalid input. Please enter a valid message/cryptogram. (Only alphabetic characters are allowed)")

def get_valid_permutation():
  while True:
    permutation = input("Enter the permutation (2nd key, an alphabetic sequence): ")
    permutation = permutation.upper()
    if len(permutation) < 7:
      print("Permutation should have at least 7 letters.")
    elif permutation.isalpha():
      return permutation
    else:
      print("Invalid permutation. Please enter a valid permutation. (Only alphabetic characters are allowed)")
    
def prompt_for_permutation():
  use_permutation = input("Do you want to use a second key (permutation)? (Y/N): ").strip().upper()
  permutation = None

  if use_permutation == "Y":
    permutation = get_valid_permutation()

  return permutation

def interactive_menu():
  while True:
    print("\n===== Choose an option =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      key = get_valid_key()
      permutation = prompt_for_permutation()
      message = get_valid_text("Enter the message: ")
      encrypted_message = caesar_cipher("encrypt", key, message, permutation)
      print("Encrypted message:", encrypted_message)
    elif choice == "2":
      key = get_valid_key()
      permutation = prompt_for_permutation()
      cryptogram = get_valid_text("Enter the cryptogram: ")
      decrypted_message = caesar_cipher("decrypt", key, cryptogram, permutation)
      print("Decrypted message:", decrypted_message)
    elif choice == "3":
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  interactive_menu()
