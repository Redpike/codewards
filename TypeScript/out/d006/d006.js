"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Kata {
    static xo(str) {
        const map = counter(str.toLowerCase());
        return map['x'] === map['o'] ? true : false;
    }
}
exports.Kata = Kata;
function counter(str) {
    return str.split('').reduce((total, letter) => {
        total[letter] ? total[letter]++ : total[letter] = 1;
        return total;
    }, {});
}
console.log(Kata.xo('xoxoxoxdasdasd'));
console.log(Kata.xo('ooxx'));
//# sourceMappingURL=d006.js.map