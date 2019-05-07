const NORTH_SOUTH = ['NORTH', 'SOUTH'];
const WEST_EAST = ['WEST', 'EAST'];

export class G964 {

  public static dirReduc = (arr) => {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] !== arr[i + 1] && NORTH_SOUTH.indexOf(arr[i]) > -1 && NORTH_SOUTH.indexOf(arr[i + 1]) > -1) {
        arr.splice(i, 2);
        i -= 2;
        continue;
      }

      if (arr[i] !== arr[i + 1] && WEST_EAST.indexOf(arr[i]) > -1 && WEST_EAST.indexOf(arr[i + 1]) > -1) {
        arr.splice(i, 2);
        i -= 2;
        continue;
      }
    }

    return arr;
  }
}

console.log(G964.dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']));
console.log(G964.dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']));
