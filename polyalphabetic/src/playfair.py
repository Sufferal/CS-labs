# alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def playfair_cipher(action, key, text):
  # Helper function to find the position of a letter in the matrix
  def find_position(matrix, letter):
    for row in range(5):
      if letter in matrix[row]:
        return row, matrix[row].index(letter)

  result = ""

  if action == "encrypt":
    # Replace J with I
    text = text.replace("J", "I")
    updated_alphabet = alphabet.replace("J", "")

    # Split the text into 2-letter pairs
    pairs = []
    for i in range(0, len(text), 2):
      pairs.append(text[i:i + 2])

    # Add X and Z to double letters
    for i in range(len(pairs)):
      if pairs[i][0] == pairs[i][1] == pairs[i + 1][0]:
        pairs[i] = pairs[i][0] + "X" 
        pairs.insert(i + 1, pairs[i][0] + "Z")
      elif pairs[i][0] == pairs[i][1]:
        pairs[i] = pairs[i][0] + "X" 
      elif pairs[i][1] == "":
        pairs[i] = pairs[i][0] + "Z"
  
    matrix = []
    
    # Remove key letters from the alphabet
    for char in key:
      updated_alphabet = updated_alphabet.replace(char, "")

    # Add key letters to the beginning of the updated alphabet
    updated_alphabet = key + updated_alphabet

    # Split the updated alphabet into 5-letter groups
    for i in range(0, len(updated_alphabet), 5):
      matrix.append(updated_alphabet[i:i + 5])

    for pair in pairs:
      a, b = pair[0], pair[1]
      a_row, a_col = find_position(matrix, a)
      b_row, b_col = find_position(matrix, b)

      if a_row == b_row:
        result += matrix[a_row][(a_col + 1) % 5] + matrix[b_row][(b_col + 1) % 5]
      elif a_col == b_col:
        result += matrix[(a_row + 1) % 5][a_col] + matrix[(b_row + 1) % 5][b_col]
      else:
        result += matrix[a_row][b_col] + matrix[b_row][a_col]

  elif action == "decrypt":
    # Split the text into 2-letter pairs
    pairs = []
    for i in range(0, len(text), 2):
      pairs.append(text[i:i + 2])

    # Create a 5x5 matrix
    matrix = []

    updated_alphabet = alphabet.replace("J", "")

    # Remove key letters from the alphabet
    for char in key:
      updated_alphabet = updated_alphabet.replace(char, "")

    # Add key letters to the beginning of the updated alphabet
    updated_alphabet = key + updated_alphabet

    # Split the updated alphabet into 5-letter groups
    for i in range(0, len(updated_alphabet), 5):
      matrix.append(updated_alphabet[i:i + 5])

    for pair in pairs:
      a, b = pair[0], pair[1]
      a_row, a_col = find_position(matrix, a)
      b_row, b_col = find_position(matrix, b)

      if a_row == b_row:
        result += matrix[a_row][(a_col - 1) % 5] + matrix[b_row][(b_col - 1) % 5]
      elif a_col == b_col:
        result += matrix[(a_row - 1) % 5][a_col] + matrix[(b_row - 1) % 5][b_col]
      else:
        result += matrix[a_row][b_col] + matrix[b_row][a_col]

    # Remove X and Z
    result = result.replace("X", "").replace("Z", "")      
  
  return result

def get_valid_text(prompt):
  punctuation = ".,;:?!-()\"\'"

  def remove_punctuation(text):
    for char in punctuation:
      text = text.replace(char, "")
    return text

  while True:
    text = input(prompt)
    text = text.replace(" ", "").upper()
    text = remove_punctuation(text)
    if text.isalpha():
      return text
    else:
      print('''[Invalid input]: Please enter a valid message/cryptogram. (Only Romanian alphabetic 
            characters and punctations are allowed)''')

def get_valid_key():
  while True:
    key = input("Enter the key: ")
    key = key.upper().replace(" ", "")
    if len(key) < 7:
      print("Key should have at least 7 letters.")
    elif key.isalpha():
      # Remove duplicate letters
      key = "".join(dict.fromkeys(key))
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
      encrypted_message = playfair_cipher("encrypt", key, message)
      print("Encrypted message:", encrypted_message)  
    elif choice == "2":
      key = get_valid_key()
      cryptogram = get_valid_text("Enter the cryptogram: ")
      decrypted_message = playfair_cipher("decrypt", key, cryptogram)
      print("Decrypted message:", decrypted_message)
    elif choice == "3":
      break
    else:
      print("Invalid choice")

if __name__ == "__main__":
  interactive_menu()
