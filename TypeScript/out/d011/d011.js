"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const array = ["I", "wish", "I", "hadn't", "come"];
class G964 {
    static partlist(arr) {
        let result = [];
        arr.forEach((_element, index) => {
            let firstPart = arr.slice(0, index);
            let secondPart = arr.slice(index);
            if (firstPart.length > 0 && secondPart.length > 0) {
                result.push([firstPart.join(' '), secondPart.join(' ')]);
            }
        });
        return result;
    }
}
exports.G964 = G964;
console.log(G964.partlist(array));
//# sourceMappingURL=d011.js.map