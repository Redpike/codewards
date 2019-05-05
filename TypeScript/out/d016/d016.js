"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function sortScores(scores) {
    return new Map([...scores.entries()].sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] > b[0] ? 1 : -1;
        }
        else {
            return b[1] - a[1];
        }
    }));
}
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
            const sortedScores = sortScores(scores);
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
        let length = firstname.length;
        firstname.split('').forEach(char => {
            const value = char.charCodeAt(0) - 96;
            length += value;
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
}
exports.G964 = G964;
console.log(G964.rank('COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH', [1, 4, 4, 5, 2, 1], 4)); // PauL
console.log(G964.rank('COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH', [1, 4, 4, 5, 2, 1], 10));
console.log(G964.rank('', [1, 4, 4, 5, 2, 1], 4));
// "Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4, "Benjamin"
console.log(G964.rank('Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin', [4, 2, 1, 4, 3, 1, 2], 4));
// "Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2, "Matthew"
console.log(G964.rank('Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden', [1, 3, 5, 5, 3, 6], 2));
// "Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4, "Abigail"
console.log(G964.rank('Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth', [3, 1, 4, 4, 3, 2], 4));
// "Lagon,Lily", [1, 5], 2, "Lagon"
console.log(G964.rank('Lagon,Lily', [1, 5], 2));
//# sourceMappingURL=d016.js.map