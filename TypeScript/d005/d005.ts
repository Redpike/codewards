export const centuryFromYear = (year: number): number => {
  return year % 100 === 0 ? Math.floor(year / 100) : Math.floor((year / 100) + 1);
};

console.log(centuryFromYear(2019));
