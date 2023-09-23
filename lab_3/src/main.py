def vigenere_cipher(action, key, text):
  alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
  result = ""

  for i in range(len(text)):
    if action == "encrypt":
      text_char_index = alphabet.index(text[i])
      key_char_index = alphabet.index(key[i % len(key)])
      new_char_index = (text_char_index + key_char_index) % len(alphabet)
      result += alphabet[new_char_index]
    elif action == "decrypt":
      text_char_index = alphabet.index(text[i])
      key_char_index = alphabet.index(key[i % len(key)])
      new_char_index = (text_char_index - key_char_index) % len(alphabet)
      result += alphabet[new_char_index]
    else:
      print("Invalid action")
      break

  return result

def get_valid_text(prompt):
  while True:
    text = input(prompt)
    text = text.replace(" ", "").upper()
    if text.isalpha():
      return text
    else:
      print("[Invalid input]: Please enter a valid message/cryptogram. (Only Romanian alphabetic characters are allowed)")

def get_valid_key():
  while True:
    key = input("Enter the key: ")
    key = key.upper()
    if len(key) < 7:
      print("Key should have at least 7 letters.")
    elif key.isalpha():
      return key
    else:
      print("[Invalid key]: Please enter a valid key. (Only Romanian alphabetic characters are allowed)")
    
def interactive_menu():
  while True:
    print("\n===== Choose an option =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      key = get_valid_key()
      message = get_valid_text("Enter the message: ")
      encrypted_message = vigenere_cipher("encrypt", key, message)
      print("Encrypted message:", encrypted_message)
    elif choice == "2":
      key = get_valid_key()
      cryptogram = get_valid_text("Enter the cryptogram: ")
      decrypted_message = vigenere_cipher("decrypt", key, cryptogram)
      print("Decrypted message:", decrypted_message)
    elif choice == "3":
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  interactive_menu()
