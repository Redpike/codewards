"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class Challenge {
    static getMiddle(s) {
        const middleMod = s.length % 2;
        if (middleMod === 0) {
            return s.charAt((s.length / 2) - 1) + s.charAt(s.length / 2);
        }
        else {
            return s.charAt(Math.ceil(s.length / 2) - 1);
        }
    }
}
exports.Challenge = Challenge;
console.log(Challenge.getMiddle('test'));
console.log(Challenge.getMiddle('testing'));
console.log(Challenge.getMiddle('middle'));
console.log(Challenge.getMiddle('A'));
//# sourceMappingURL=d007.js.map