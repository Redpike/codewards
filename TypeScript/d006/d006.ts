export class Kata {
  static xo(str: string) {
    const map = counter(str.toLowerCase())
    return map['x'] === map['o'] ? true : false;
  }
}

function counter(str: string) {
  return str.split('').reduce((total, letter) => {
    total[letter] ? total[letter]++ : total[letter] = 1;
    return total;
  }, {});
}

console.log(Kata.xo('xoxoxoxdasdasd'));
console.log(Kata.xo('ooxx'));
