class TimeConverter {
  public static parse = (time: number): string => {
    const hours = ~~(time / 3600);
    const minutes = ~~((time - (hours * 3600)) / 60);
    const seconds = ~~((time - (hours * 3600) - (minutes * 60)));

    return TimeConverter.toString(hours) + '|' + TimeConverter.toString(minutes) + '|' + TimeConverter.toString(seconds);
  }

  public static convert = (time: string): number => {
    const data = time.split('|');
    const hours = Number(data[0]);
    const minutes = Number(data[1]);
    const seconds = Number(data[2]);

    return hours * 3600 + (minutes * 60) + seconds;
  }

  private static toString(number: number): string {
    return number.toLocaleString('en-US', {
      minimumIntegerDigits: 2,
      useGrouping: false
    });
  }
}

export class G964 {

  public static stat = (strg) => {
    if (strg.length > 0) {
      let str = String(strg);
      str = str.replace(' ', '');
      const times = str.split(',');
      const converted = times.map(TimeConverter.convert);

      return G964.range(converted) + ' ' + G964.average(converted) + ' ' + G964.median(converted);
    }

    return '';
  }

  private static range = (times: number[]): string => {
    const min = Math.min(...times);
    const max = Math.max(...times);

    return 'Range: ' + TimeConverter.parse(max - min);
  }

  private static average = (times: number[]): string => {
    const sum = times.reduce(function (a, b) {
      return a + b;
    });
    const average = TimeConverter.parse(sum / times.length);

    return 'Average: ' + average;
  }

  private static median = (times: number[]): string => {
    times.sort(function (a, b) {
      return a - b;
    });

    let median = '';

    if (times.length === 0) {
      median = '00';
    } else {
      const half = Math.floor(times.length / 2);
      if (times.length % 2 === 1) {
        median = TimeConverter.parse(times[half]);
      } else {
        median = TimeConverter.parse((times[half - 1] + times[half]) / 2);
      }
    }

    return 'Median: ' + median;
  }
}

console.log(G964.stat('01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17'));
