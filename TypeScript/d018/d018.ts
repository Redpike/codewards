export function countRedBeads(n: number): number {
  if (n < 2) {
    return 0;
  } else {
    return (n * 2) - 2;
  }
}

console.log(countRedBeads(0));
console.log(countRedBeads(1));
console.log(countRedBeads(3));
console.log(countRedBeads(5));
