const array = ["I", "wish", "I", "hadn't", "come"];

export class G964 {
  public static partlist(arr: string[]): string[] {
    let result = [];
    arr.forEach((_element, index) => {
      let firstPart = arr.slice(0, index);
      let secondPart = arr.slice(index);
      if (firstPart.length > 0 && secondPart.length > 0) {
        result.push([firstPart.join(' '), secondPart.join(' ')]);
      }
    });

    return result;
  }
}

console.log(G964.partlist(array));
