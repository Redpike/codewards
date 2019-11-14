package pl.com.redpike.d004;

import java.util.Arrays;

public class AverageCalculator {

    private AverageCalculator() {
    }

    public static double findAverage(int[] array) {
        return Arrays.stream(array)
                .average()
                .orElse(0);
    }
}
