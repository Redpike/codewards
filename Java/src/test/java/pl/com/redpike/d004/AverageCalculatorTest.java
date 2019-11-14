package pl.com.redpike.d004;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AverageCalculatorTest {

    private static final double DELTA = 1e-15;

    @Test
    void shouldReturnAverage() {
        assertEquals(1, AverageCalculator.findAverage(new int[]{1, 1, 1}), DELTA);
        assertEquals(2, AverageCalculator.findAverage(new int[]{1, 2, 3}), DELTA);
    }
}