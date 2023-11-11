from rsa import *
from elgamal import *
from diffie_hellman import *

def main():
  while True:
    print("\n===== ★★★★★ =====")
    print("1. RSA")
    print("2. ElGamal")
    print("3. Diffie-Hellman")
    print("4. Exit")
    print("===== ★★★★★ =====\n")
    choice = input("Enter your algo choice: ")

    try:
      choice = int(choice)
    except ValueError:
      print("Invalid choice. Please try again.")
      continue

    if choice == 1:
      rsa_main()
    elif choice == 2:
      elgamal_main()
    elif choice == 3:
      diffie_hellman_main()
    elif choice == 4:
      print("Exiting...")
      exit()
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()