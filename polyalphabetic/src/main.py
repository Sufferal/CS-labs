from prettytable import PrettyTable

alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"


def vigenere_cipher(action, key, text):
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


def create_alphabet_table():
  numbers = list(range(len(alphabet)))

  table = PrettyTable()
  table.field_names = [alphabet[i] for i in range(len(alphabet))]
  table.add_row(numbers)

  return table


def create_vigenere_table(text, key, action):
  table = PrettyTable()
  table.field_names = ["Field"] + [str(i) for i in range(len(text))]
  key_indexes = [alphabet.index(key[i % len(key)]) for i in range(len(text))]
  key_repeated = [key[i % len(key)] for i in range(len(text))]

  if action == "encrypt":
    text_indexes = [alphabet.index(char) for char in text]
    sum_indexes = [(ti + ki) % len(alphabet) for ti, ki in zip(text_indexes, key_indexes)]
    cryptogram = [alphabet[i] for i in sum_indexes]

    table.add_row(["Text"] + list(text))
    table.add_row(["Key"] + key_repeated)
    table.add_row(["Text Index"] + text_indexes)
    table.add_row(["Key Index"] + key_indexes)
    table.add_row(["Sum Index"] + sum_indexes)
    table.add_row(["Cryptogram"] + cryptogram)
  elif action == "decrypt":
    cryptogram_indexes = [alphabet.index(char) for char in text]
    diff_indexes = [(ti - ki) % len(alphabet) for ti, ki in zip(cryptogram_indexes, key_indexes)]

    table.add_row(["Cryptogram"] + list(text))
    table.add_row(["Key"] + key_repeated)
    table.add_row(["Cryptogram Index"] + cryptogram_indexes)
    table.add_row(["Key Index"] + key_indexes)
    table.add_row(["Diff Index"] + diff_indexes)
    
    text = [alphabet[i] for i in diff_indexes]
    table.add_row(["Text"] + text)

  return table


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

      alphabet_table = create_alphabet_table()
      print("Alphabet Table:")
      print(alphabet_table)

      vigenere_table = create_vigenere_table(message, key, "encrypt")
      print("Vigenere Table:")
      print(vigenere_table)

    elif choice == "2":
      key = get_valid_key()
      cryptogram = get_valid_text("Enter the cryptogram: ")
      decrypted_message = vigenere_cipher("decrypt", key, cryptogram)
      print("Decrypted message:", decrypted_message)

      alphabet_table = create_alphabet_table()
      print("Alphabet Table:")
      print(alphabet_table)

      vigenere_table = create_vigenere_table(cryptogram, key, "decrypt")
      print("Vigenere Table:")
      print(vigenere_table)

    elif choice == "3":
      break
    else:
      print("Invalid choice")


if __name__ == "__main__":
  interactive_menu()
