"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const array = [true, true, true, false,
    true, true, true, true,
    undefined, false, null, null,
    true, false, false, true,
    true, true, true, true,
    false, false, true, true];
function countSheeps(arrayOfSheep) {
    return arrayOfSheep.filter(value => value).length;
}
exports.countSheeps = countSheeps;
console.log(countSheeps(array));
//# sourceMappingURL=d002.js.map