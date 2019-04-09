"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Kata {
    static getCount(str) {
        return (str.match(/[aeiou]/g) || []).length;
    }
}
exports.Kata = Kata;
//# sourceMappingURL=d010.js.map