package pl.com.redpike.d005;

public class StringChecker {

    private StringChecker() {
    }

    public static boolean isStringEndWith(String string, String ending) {
        return string.length() >= ending.length() && string.endsWith(ending);
    }
}
