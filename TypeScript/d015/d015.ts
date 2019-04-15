export function SeriesSum(n: number): string {
  if (n === 0) {
    return '0.00';
  } else {
    let sum = 0;
    let denominator = -2;

    for (let i = 0; i < n; i++) {
      denominator += 3
      sum += 1 / denominator;
    }

    return String(roundToTwo(sum).toFixed(2));
  }
}

function roundToTwo(value: number) {
  return (Math.round(value * 100) / 100);
}

console.log(SeriesSum(1));
console.log(SeriesSum(2));
console.log(SeriesSum(5));
