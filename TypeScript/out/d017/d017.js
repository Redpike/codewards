"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
class G964 {
    static containAllRots(str, arr) {
        if (str.length === 0 || !str) {
            return true;
        }
        else {
            return G964.areRotations(str, arr);
        }
    }
    static areRotations(str, arr) {
        let result = true;
        const testString = str + str;
        let rotations = [];
        for (let i = 0; i < str.length; i++) {
            rotations.push(testString.substr(i, str.length));
        }
        for (let rotation of rotations) {
            if (!arr.includes(rotation)) {
                result = false;
                break;
            }
        }
        return result;
    }
}
exports.G964 = G964;
console.log(G964.containAllRots('bsjq', ['bsjq', 'qbsj', 'sjqb', 'twZNsslC', 'jqbs']));
console.log(G964.containAllRots('Ajylvpy', ['Ajylvpy', 'ylvpyAj', 'jylvpyA', 'lvpyAjy', 'pyAjylv', 'vpyAjyl', 'ipywee']));
//# sourceMappingURL=d017.js.map