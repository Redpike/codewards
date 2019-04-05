"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.centuryFromYear = (year) => {
    return year % 100 === 0 ? Math.floor(year / 100) : Math.floor((year / 100) + 1);
};
console.log(exports.centuryFromYear(2019));
//# sourceMappingURL=d005.js.map