export class G964 {

  public static containAllRots(str, arr) {
    if (str.length === 0 || !str) {
      return true;
    } else {
      return G964.areRotations(str, arr);
    }
  }

  private static areRotations(str, arr): boolean {
    let result: boolean = true;
    const testString: string = str + str;
    let rotations = [];
    for (let i = 0; i < str.length; i++) {
      rotations.push(testString.substr(i, str.length));
    }

    for (let rotation of rotations) {
      if (!arr.includes(rotation)) {
        result = false;
        break;
      }
    }

    return result;
  }
}

console.log(G964.containAllRots('bsjq', ['bsjq', 'qbsj', 'sjqb', 'twZNsslC', 'jqbs']));
console.log(G964.containAllRots('Ajylvpy', ['Ajylvpy', 'ylvpyAj', 'jylvpyA', 'lvpyAjy', 'pyAjylv', 'vpyAjyl', 'ipywee']));
