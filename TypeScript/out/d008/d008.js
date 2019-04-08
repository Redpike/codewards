"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function isSortedAndHow(array) {
    const ascArray = array.slice().sort((a, b) => a > b ? 1 : -1);
    const descArray = array.slice().sort((a, b) => a > b ? -1 : 1);
    if (JSON.stringify(array) === JSON.stringify(ascArray)) {
        return 'yes, ascending';
    }
    else if (JSON.stringify(array) === JSON.stringify(descArray)) {
        return 'yes, descending';
    }
    else {
        return 'no';
    }
}
exports.isSortedAndHow = isSortedAndHow;
console.log(isSortedAndHow([2, 3, 5, 1]));
console.log(isSortedAndHow([1, 3, 5, 6]));
console.log(isSortedAndHow([8, 6, 5, 5]));
//# sourceMappingURL=d008.js.map