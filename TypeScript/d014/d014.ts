export function encode(str: String, n: number): number[] {
  const lettes = 'abcdefghijklmnopqrstuvwxyz';
  const number = String(n);
  const digits = convertToDigits(lettes);

  return cipher(str, number, digits);
}

function convertToDigits(letters: String): {} {
  let digits = {};

  for (let i = 0; i < letters.length; i++) {
    digits[letters.charAt(i)] = letters.charCodeAt(i) - 96;
  }

  return digits
}

function cipher(stringToCipher: String, salt: String, digits: {}): number[] {
  let result = [];

  stringToCipher.split('').forEach((char, index) => {
    result.push(Number(digits[char]) + Number((salt.charAt(index % salt.length))));
  });

  return result;
}

console.log(encode('scout', 1939));
