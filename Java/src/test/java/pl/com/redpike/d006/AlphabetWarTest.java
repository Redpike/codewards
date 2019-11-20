package pl.com.redpike.d006;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AlphabetWarTest {

    @Test
    void BasicTest() {
        assertEquals("Right side wins!", AlphabetWar.alphabetWar("z"));
        assertEquals("Let's fight again!", AlphabetWar.alphabetWar("zdqmwpbs"));
        assertEquals("Right side wins!", AlphabetWar.alphabetWar("zzzzs"));
        assertEquals("Left side wins!", AlphabetWar.alphabetWar("wwwwwwz"));
    }
}