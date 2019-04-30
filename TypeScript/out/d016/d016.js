"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class G964 {
    static rank(st, we, n) {
        if (!st || st.length === 0) {
            return 'No participants';
        }
        else if (st.split(',').length < n) {
            return 'Not enough participants';
        }
        else {
            const lengths = this.getLengthsOfFirstnames(st);
            const scores = this.computeScores(st, lengths, we);
            const sortedScores = this.sortScores(scores);
            console.log(sortedScores);
            return Array.from(sortedScores.keys())[n - 1];
        }
    }
    static getLengthsOfFirstnames(string) {
        let arrayOfLengths = [];
        string.split(',').forEach(firstname => {
            const length = this.computeLengthOfFirstname(firstname.toLowerCase());
            arrayOfLengths.push(length);
        });
        return arrayOfLengths;
    }
    static computeLengthOfFirstname(firstname) {
        let length = 0;
        firstname.split('').forEach(char => {
            length += char.charCodeAt(0) - 96;
        });
        return length;
    }
    static computeScores(string, lengths, weights) {
        let scores = new Map();
        string.split(',').forEach((firstname, index) => {
            let score = lengths[index] * weights[index];
            scores.set(firstname, score);
        });
        return scores;
    }
    static sortScores(scores) {
        return new Map([...scores.entries()].sort((a, b) => b[1] - a[1]));
    }
}
exports.G964 = G964;
const testString = 'COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH';
const weights = [1, 4, 4, 5, 2, 1];
const n = 4;
console.log(G964.rank(testString, weights, n));
console.log(G964.rank(testString, weights, 10));
console.log(G964.rank('', weights, n));
//# sourceMappingURL=d016.js.map