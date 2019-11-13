package pl.com.redpike.d003;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PangramCheckerTest {

    @Test
    void test() {
        // Declare
        String pangram1 = "The quick brown fox jumps over the lazy dog.";
        String pangram2 = "You shall not pass!";

        // When
        PangramChecker pc = new PangramChecker();

        // Then
        assertTrue(pc.check(pangram1));
        assertFalse(pc.check(pangram2));
    }
}