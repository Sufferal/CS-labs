import sys
import random

# Set the maximum number of digits for integers
sys.set_int_max_str_digits(0)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2
d = random.randint(2, p - 2)

def beta_generator(p, g, d):
  beta = pow(g, d, p)
  return beta

def encrypt(message, p, g, beta):
  k = random.randint(2, p - 2)
  r = pow(g, k, p)
  t = (pow(beta, k, p) * message) % p

  return r, t

def decrypt(r, t, p, d):
  message = (pow(r, p - 1 - d, p) * t) % p
  return message

def elgamal_main():
  user_input = input("Enter a message to encrypt: ")
  message = int(user_input.encode().hex(), 16)
  print("Message (hex): ", hex(message))
  print("Message (decimal): ", message)
  r, t = encrypt(message, p, g, beta_generator(p, g, d))
  print("Cipher Text: ", t)

  decrypted_message = decrypt(r, t, p, d)
  result = bytes.fromhex(hex(decrypted_message)[2:]).decode("ASCII")
  print("Decrypted cipher: ", result)

if __name__ == "__main__":
  elgamal_main()