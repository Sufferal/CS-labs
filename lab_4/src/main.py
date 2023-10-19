import random

e_boxes = [
  32, 1, 2, 3, 4, 5,
  4, 5, 6, 7, 8, 9,
  8, 9, 10, 11, 12, 13,
  12, 13, 14, 15, 16, 17,
  16, 17, 18, 19, 20, 21,
  20, 21, 22, 23, 24, 25,
  24, 25, 26, 27, 28, 29,
  28, 29, 30, 31, 32, 1
]

def block_exp(r_block): 
  block_arr = []

  for i in e_boxes:
    block_arr.append(r_block[i - 1])

  return block_arr

def xor_exp(r_block, key):
  xor_arr = []

  for i in range(len(r_block)):
    xor_arr.append(r_block[i] ^ key[i])

  return xor_arr

def generate_random_key():
  return [random.randint(0, 1) for _ in range(48)]

def generate_random_r_block():
  return [random.randint(0, 1) for _ in range(32)]

def is_binary_string(input_string):
  return all(bit in ('0', '1') for bit in input_string)

def print_list(a_list, n):
  count = 0
  
  for i in (''.join(str(num) for num in a_list)):
    if count % n == 0:
      print(" ", end='')
    print(i, end='')
    count += 1

def print_results(key, r_block):
  # Key and r_block
  print("Key:")
  print_list(key, 6)
  print("\nr_block:")
  print_list(r_block, 4)

  # Expansion
  e_block = block_exp(r_block)
  print("\ne_block:")
  print_list(e_block, 6)
  
  # XOR
  xor_block = xor_exp(e_block, key)
  print("\nxor_block:")
  print_list(xor_block, 6)
  print("\n")

def menu():
  while True:
    print("\n===== Choose an input method: =====")
    print("1. Manual Input")
    print("2. Random Input")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == '1':
      key = input("Enter the key (48 bits): ")
      r_block = input("Enter r_block (32 bits): ")
      if len(key) != 48 or len(r_block) != 32 or not is_binary_string(key) or not is_binary_string(r_block):
            print("Key must be 48 bits and r_block must be 32 bits, containing only '0' and '1'.")
            continue
      key = [int(bit) for bit in key]
      r_block = [int(bit) for bit in r_block]
      print_results(key, r_block)
    elif choice == '2':
      key = generate_random_key()
      r_block = generate_random_r_block()
      print_results(key, r_block)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please enter 1, 2 or 3.")
      continue

if __name__ == "__main__":
  menu()
  


