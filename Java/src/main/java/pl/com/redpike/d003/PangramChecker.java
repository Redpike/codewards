package pl.com.redpike.d003;

import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

public class PangramChecker {

    private static final Integer ALPHABET_COUNT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".length();

    public boolean check(String sentence) {
        if (Objects.isNull(sentence) || sentence.trim().isEmpty())
            return false;
        else {
            String sentenceUpper = sentence.toUpperCase();
            Set<Character> characterSet = sentenceUpper.chars()
                    .filter(Character::isAlphabetic)
                    .mapToObj(c -> (char) c)
                    .collect(Collectors.toSet());

            return characterSet.size() == ALPHABET_COUNT;
        }
    }
}
