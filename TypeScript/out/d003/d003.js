"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const array = [34, -345, -1, 100];
function findSmallestInt(args) {
    return args.sort((a, b) => a > b ? 1 : -1).shift();
}
exports.findSmallestInt = findSmallestInt;
console.log(findSmallestInt(array));
//# sourceMappingURL=d003.js.map