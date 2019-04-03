const array = [true, true, true, false,
  true, true, true, true,
  undefined, false, null, null,
  true, false, false, true,
  true, true, true, true,
  false, false, true, true];

export function countSheeps(arrayOfSheep) {
  return arrayOfSheep.filter(value => value).length;
}

console.log(countSheeps(array));
