export class G964 {

  public static solequa(n: number) {
    let result = [];

    /*
      x^2 - 4 * y^2 = n
      x^2 - 4 * y^2 = (x - 2y)(x + 2y) = n
      i = x - 2y, j = x + 2y
    */

    for (let i = 1; i < Math.floor(Math.sqrt(n)) + 1; i++) {

      if (n % i != 0) {
        continue;
      }

      let j = n / i;
      let y = (j - i) / 4;
      let x = i + 2 * y;

      if (x >= 0 && y >= 0 && Number.isInteger(x) && Number.isInteger(y) && (j == x + 2 * y) && (i == x - 2 * y)) {
        result.push([x, y]);
      }
    }

    return result;
  }
}

console.log(G964.solequa(90005));
console.log(G964.solequa(90002));
