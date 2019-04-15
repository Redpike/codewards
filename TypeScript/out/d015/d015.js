"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function SeriesSum(n) {
    if (n === 0) {
        return '0.00';
    }
    else {
        let sum = 0;
        let denominator = -2;
        for (let i = 0; i < n; i++) {
            denominator += 3;
            sum += 1 / denominator;
        }
        return String(roundToTwo(sum).toFixed(2));
    }
}
exports.SeriesSum = SeriesSum;
function roundToTwo(value) {
    return (Math.round(value * 100) / 100);
}
console.log(SeriesSum(1));
console.log(SeriesSum(2));
console.log(SeriesSum(5));
//# sourceMappingURL=d015.js.map