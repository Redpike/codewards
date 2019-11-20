package pl.com.redpike.d006;

import java.util.AbstractMap;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class AlphabetWar {

    private static final String LEFT_SIDE_WON_RESULT = "Left side wins!";
    private static final String RIGHT_SIDE_WON_RESULT = "Right side wins!";
    private static final String DRAW_RESULT = "Let's fight again!";

    private static Map<Character, Integer> leftSideArmy;
    private static Map<Character, Integer> rightSideArmy;

    static {
        leftSideArmy = Stream.of(
                new AbstractMap.SimpleEntry<>('w', 4),
                new AbstractMap.SimpleEntry<>('p', 3),
                new AbstractMap.SimpleEntry<>('b', 2),
                new AbstractMap.SimpleEntry<>('s', 1)
        ).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

        rightSideArmy = Stream.of(
                new AbstractMap.SimpleEntry<>('m', 4),
                new AbstractMap.SimpleEntry<>('q', 3),
                new AbstractMap.SimpleEntry<>('d', 2),
                new AbstractMap.SimpleEntry<>('z', 1)
        ).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    private AlphabetWar() {
    }

    public static String alphabetWar(String fight) {
        String lowerFight = fight.toLowerCase();

        int leftScore = getScore(lowerFight, leftSideArmy);
        int rightScore = getScore(lowerFight, rightSideArmy);

        if (leftScore == rightScore)
            return DRAW_RESULT;
        else if (leftScore > rightScore)
            return LEFT_SIDE_WON_RESULT;
        else
            return RIGHT_SIDE_WON_RESULT;
    }

    private static int getScore(String fight, Map<Character, Integer> armyMap) {
        return fight.chars()
                .mapToObj(c -> (char) c)
                .filter(armyMap::containsKey)
                .mapToInt(c -> armyMap.getOrDefault(c, 0))
                .sum();
    }
}
