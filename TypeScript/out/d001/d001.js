"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.summation = (num) => {
    let sum = 0;
    for (let i = 1; i <= num; i++) {
        sum += i;
    }
    return sum;
};
console.log(exports.summation(8));
//# sourceMappingURL=d001.js.map