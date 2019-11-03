package pl.com.redpike.d001;

import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;

public class Isogram {

    private Isogram() {
    }

    public static boolean isIsogram(String string) {
        string = Optional.ofNullable(string).orElse("").toLowerCase();
        Set<Character> charsSet = mapStringToCharSet(string);
        return string.length() == charsSet.size();
    }

    private static Set<Character> mapStringToCharSet(String string) {
        return string.chars()
                .mapToObj(character -> (char) character)
                .collect(Collectors.toSet());
    }
}
