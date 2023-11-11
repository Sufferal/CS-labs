import sys

# Set the maximum number of digits for integers
sys.set_int_max_str_digits(0)

# 2 large prime numbers
p = (2 ** 3539 + 1) // 3     # https://t5k.org/primes/page.php?id=54344
q = 4713 * (2 ** 4713) + 1   # https://t5k.org/primes/page.php?id=40087

# n is the modulus for the public key and the private keys
n = p * q

# Phi is the totient of n
phi = (p - 1) * (q - 1)

# Choose an integer e such that e and phi(n) are coprime
# Commonly used value for e is 65537
e = 65537

# Private key d is the multiplicative inverse of e modulo phi(n)
d = pow(e, -1, phi)

def encrypt(message, e, n):
  return pow(message, e, n)

def decrypt(cipher_text, d, n):
  return pow(cipher_text, d, n)

def rsa_main():
  user_input = input("Enter a message to encrypt: ")
  message = int(user_input.encode().hex(), 16)
  print("Message (hex): ", hex(message))
  print("Message (decimal): ", message)
  cipher_text = encrypt(message, e, n)
  print("Cipher Text: ", cipher_text)

  decrypted_message = decrypt(cipher_text, d, n)
  result = bytes.fromhex(hex(decrypted_message)[2:]).decode("ASCII")
  print("Decrypted cipher: ", result)

if __name__ == "__main__":
  rsa_main()