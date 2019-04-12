export function compare(s1: string, s2: string): boolean {
  if (!s1 || !/^[a-zA-Z]+$/.test(s1)) {
    s1 = '';
  }

  if (!s2 || !/^[a-zA-Z]+$/.test(s2)) {
    s2 = '';
  }

  return computeSum(s1.toUpperCase()) === computeSum(s2.toUpperCase());
}

function computeSum(string: string): number {
  let sum = 0;

  for (let i = 0; i < string.length; i++) {
    sum += string.charAt(i).charCodeAt(0);
  }

  return sum;
}