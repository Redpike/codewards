package pl.com.redpike.d002;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class NumberConverterTest {

    @Test
    void shouldReturnArray() {
        assertArrayEquals(new int[] {1, 3, 2, 5, 3}, NumberConverter.digitize(35231));
    }
}