"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function compare(s1, s2) {
    if (!s1 || !/^[a-zA-Z]+$/.test(s1)) {
        s1 = '';
    }
    if (!s2 || !/^[a-zA-Z]+$/.test(s2)) {
        s2 = '';
    }
    return computeSum(s1.toUpperCase()) === computeSum(s2.toUpperCase());
}
exports.compare = compare;
function computeSum(string) {
    let sum = 0;
    for (let i = 0; i < string.length; i++) {
        sum += string.charAt(i).charCodeAt(0);
    }
    return sum;
}
//# sourceMappingURL=d013.js.map