# Cryptography Labs
This repository contains the laboratory works for the Cryptography course at FCIM, UTM.

## Caesar Cipher (#1)
It is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.

## Mono-alphabetic Cipher (#2)
A mono-alphabetic cipher is a type of substitution cipher in cryptography where each letter in the plaintext is replaced with a single, fixed letter in the ciphertext.
In a mono-alphabetic cipher, the substitution remains consistent throughout the entire message, making it relatively easy to decipher through frequency analysis and other cryptanalysis techniques.

While mono-alphabetic ciphers are straightforward to implement, they are not secure for protecting sensitive information because they are vulnerable to simple cryptanalysis methods.

## Polyalphabetic Cipher (#3)
A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets . The Vigenère cipher is probably the best-known example of a polyalphabetic cipher, though it is a simplified special case. The Enigma machine is more complex but is still fundamentally a polyalphabetic substitution cipher.

## Playfair Cipher (#4)
The Playfair cipher or Playfair square or Wheatstone-Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher. The scheme was invented in 1854 by Charles Wheatstone, but bears the name of Lord Playfair for promoting its use. 

The technique encrypts pairs of letters (bigrams or digrams), instead of single letters as in the simple substitution cipher and rather more complex Vigenère cipher systems then in use. The Playfair is thus significantly harder to break since the frequency analysis used for simple substitution ciphers does not work with it. The frequency analysis of bigrams is possible, but considerably more difficult. With 600 possible bigrams rather than the 26 possible monograms (single symbols, usually letters in this context), a considerably larger cipher text is required in order to be useful.
