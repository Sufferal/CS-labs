import random
from tests import *
from md6 import md6hash

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2 
d = random.randint(2, p - 2) 

def generate_public_key(p, g, d):
  pk = pow(g, d, p)
  return pk

def encrypt(message, p, g, pk):
  k = random.randint(1, p - 1) 
  r = pow(g, k, p)             
  t = (pow(pk, k, p) * message) % p

  return r, t

def decrypt(r, t, p, d):
  message = (pow(r, p - 1 - d, p) * t) % p
  return message

def elgamal_main():
  md6 = md6hash()
  hash_size = 256 # Bits

  initial_msg = get_current_message()
  initial_hash = md6.hex(initial_msg, hash_size)
  print("md6 hash initial: ", initial_hash)

  r, t = encrypt(int(initial_hash, 16), p, g, generate_public_key(p, g, d))
  plain_text = decrypt(r, t, p, d)

  # Test tampering
  # add_spaces("message.txt", 2)
  # remove_lines("message.txt", 2)
  # clear_file("message.txt")

  current_msg = get_current_message()
  current_hash = md6.hex(current_msg, hash_size)
  print("md6 hash current: ", current_hash)
  if plain_text == int(current_hash, 16):
    print("[Status] Signature is valid. Message is not tampered with.")
  else:
    print("[Status] Signature is invalid. Message is tampered with.")

if __name__ == "__main__":
  elgamal_main()