const keyNumElem  = document.querySelector('#key-num');
const keyWordElem = document.querySelector('#key-word');
const valueElem   = document.querySelector('#value');
const encryptBtn  = document.querySelector('#encrypt');
const decryptBtn  = document.querySelector('#decrypt');
const outputElem  = document.querySelector('#output');

// Error Messages
const keyWordErrorElem = document.querySelector("#key-word-message");

// Enter Key
window.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    encryptBtn.click();
  }
  if (e.key === 'Enter') {
    if (e.shiftKey) {
      e.preventDefault();
      decryptBtn.click();
    }
  }
});

// Modulo Function
const mod = (a, b) => ((a % b) + b) % b;

const validateInput = (value) => {
  if(value.length < 7) {
    keyWordErrorElem.textContent = "Please enter at least 7 letters";
    return false;
  } 

  return true;
};

const CaesarCipher = (e, sign) => {
  e.preventDefault();
  outputElem.textContent = 'Result: ';
  keyWordErrorElem.textContent = "";

  // Remove Spaces and Uppercase
  const userValue = valueElem.value.toUpperCase().replace(/\s/g, "");
  const keyWordValue = keyWordElem.value;
  const userKey = keyNumElem.value;

  let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'; 

  if (keyWordValue !== "" && validateInput(keyWordValue)) {
    // Remove Duplicates
    const letters = [...new Set([...keyWordElem.value.toUpperCase()])]
    
    // Adjust Alphabet
    for (const char of letters) {
      alphabet = alphabet.replace(new RegExp(char, 'g'), '');
    }

    // Add KeyWord to the front of the modified alphabet
    alphabet = letters.join('') + alphabet;
  }

  let result = "";
  for (const char of userValue) {
    let modifier = (sign === "+") ? 1 : -1;
    result += alphabet[mod((alphabet.indexOf(char) + modifier * parseInt(userKey)), 26)];
  }

  outputElem.textContent += result;
};

encryptBtn.addEventListener('click', (e) => CaesarCipher(e, "+"));
decryptBtn.addEventListener('click', (e) => CaesarCipher(e, "-"));
