export class G964 {

  public static rank(st, we, n) {
    if (!st || st.length === 0) {
      return 'No participants';
    } else if (st.split(',').length < n) {
      return 'Not enough participants';
    } else {
      const lengths = this.getLengthsOfFirstnames(st);
      const scores = this.computeScores(st, lengths, we);
      const sortedScores = this.sortScores(scores);
      console.log(sortedScores);

      return Array.from(sortedScores.keys())[n - 1];
    }
  }

  private static getLengthsOfFirstnames(string: string): number[] {
    let arrayOfLengths = [];

    string.split(',').forEach(firstname => {
      const length = this.computeLengthOfFirstname(firstname.toLowerCase());
      arrayOfLengths.push(length);
    });

    return arrayOfLengths;
  }

  private static computeLengthOfFirstname(firstname: string): number {
    let length = 0;

    firstname.split('').forEach(char => {
      length += char.charCodeAt(0) - 96;
    });

    return length;
  }

  private static computeScores(string: string, lengths: number[], weights: number[]) {
    let scores = new Map<string, number>();

    string.split(',').forEach((firstname, index) => {
      let score = lengths[index] * weights[index];
      scores.set(firstname, score);
    })

    return scores;
  }

  private static sortScores(scores: Map<string, number>) {
    return new Map([...scores.entries()].sort((a, b) => b[1] - a[1]));
  }
}

const testString = 'COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH';
const weights = [1, 4, 4, 5, 2, 1];
const n = 4;

console.log(G964.rank(testString, weights, n));
console.log(G964.rank(testString, weights, 10));
console.log(G964.rank('', weights, n));
