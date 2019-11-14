package pl.com.redpike.d005;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class StringCheckerTest {

    @Test
    void shouldEndWith() {
        assertAll(
                () -> assertTrue(StringChecker.isStringEndWith("abc", "bc")),
                () -> assertTrue(StringChecker.isStringEndWith("asdasdasd", "dasd")),
                () -> assertTrue(StringChecker.isStringEndWith("AdasdCXXass", "Xass")),
                () -> assertTrue(StringChecker.isStringEndWith("ddddddddddddddd", "ddddd"))
        );
    }

    @Test
    void shouldntEndWith() {
        assertAll(
                () -> assertFalse(StringChecker.isStringEndWith("abc", "as")),
                () -> assertFalse(StringChecker.isStringEndWith("asdasdasd", "dASDd")),
                () -> assertFalse(StringChecker.isStringEndWith("AdasdCXXass", "xass")),
                () -> assertFalse(StringChecker.isStringEndWith("ddddddddddddddd", "dx"))
        );
    }
}