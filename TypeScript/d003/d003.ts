const array = [34, -345, -1, 100];

export function findSmallestInt(args: number[]): number {
  return args.sort((a, b) => a > b ? 1 : -1).shift();
}

console.log(findSmallestInt(array));
