import sys
import random

# Set the maximum number of digits for integers
sys.set_int_max_str_digits(0)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

# Private keys
private_1 = random.randint(2, p - 2)
private_2 = random.randint(2, p - 2)

# Public keys
public_1 = pow(g, private_1, p)
public_2 = pow(g, private_2, p)

# Shared secret
shared_1 = pow(public_2, private_1, p)
shared_2 = pow(public_1, private_2, p)

def trunc_256_bits(key):
  res = key.to_bytes((key.bit_length() + 7) // 8, byteorder='big')
  
  # Ensure the shared secret is 256 bits (32 bytes)
  if len(res) < 32:
    res = b'\x00' * (32 - len(res)) + res
  elif len(res) > 32:
    res = res[-32:]
  
  return res

def diffie_hellman_main():
  print("Prime: ", p)
  print("Generator: ", g)

  print("\nPrivate key 1: ", private_1)
  print("Private key 2: ", private_2)

  print("\nPublic key 1: ", public_1)
  print("Public key 2: ", public_2)

  print("\nShared secret 1: ", shared_1)
  print("Shared secret 2: ", shared_2)

  if shared_1 == shared_2:
    print("\nShared secrets match!")
    trunc_256_bits(shared_1)
    print("Shared secret (256 bits): ", trunc_256_bits(shared_1))
    print("Shared secret hex: ", trunc_256_bits(shared_1).hex())
    print("Shared secret decimal: ", int(trunc_256_bits(shared_1).hex(), 16))
    print("Shared secret length: ", 
            len(trunc_256_bits(shared_1)), "bytes,", 
            len(trunc_256_bits(shared_1)) * 8, "bits,",
            len(str(int(trunc_256_bits(shared_1).hex(), 16))), "digits.")
  else:
    print("\nShared secrets do not match!")

if __name__ == "__main__":
  diffie_hellman_main()