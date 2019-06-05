"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function countRedBeads(n) {
    if (n < 2) {
        return 0;
    }
    else {
        return (n - 1) * 2;
    }
}
exports.countRedBeads = countRedBeads;
console.log(countRedBeads(0));
console.log(countRedBeads(1));
console.log(countRedBeads(3));
console.log(countRedBeads(5));
//# sourceMappingURL=d018.js.map