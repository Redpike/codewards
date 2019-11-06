package pl.com.redpike.d002;

import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class NumberConverter {

    private NumberConverter() {
    }

    public static int[] digitize(long number) {
        List<String> list = String.valueOf(number).chars()
                .mapToObj(c -> Character.toString((char) c))
                .collect(Collectors.toList());
        Collections.reverse(list);
        return list.stream()
                .mapToInt(Integer::valueOf)
                .toArray();
    }
}
