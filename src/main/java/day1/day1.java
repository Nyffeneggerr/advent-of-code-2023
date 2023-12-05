package day1;

import java.util.Arrays;
import java.util.List;

public class day1 {

    public static void main(String[] args) {
        var inputData = loadInputData();

        var resultValue = inputData.stream().mapToInt(day1::extractValueFromString).peek(System.out::println).sum();
        System.out.println(resultValue);
    }

    private static int extractValueFromString(String input) {
        System.out.println("Input: " + input);
        var transformedWordString = replaceDigitsToWords(input);
        System.out.println("Transformed 1: " + transformedWordString);
        var transformedNumberString = replaceWordsToDigits(transformedWordString);
        System.out.println("Transformed 2: " + transformedNumberString);
        var numberString = transformedNumberString.replaceAll("[^0-9]", "");

        if (numberString.length() == 0) {
            return 0;
        }

        if (numberString.length() == 1) {
            return Integer.valueOf( "" + numberString + numberString);
        }

        return Integer.valueOf("" + numberString.substring(0, 1) + numberString.substring(numberString.length()-1));
    }

    private static String replaceWordsToDigits(String input) {
        var result = findFromBeginning(input);
        result = findFromEnd(result);
        return result;
    }

    private static String findFromBeginning(String input) {
        var currentIndex = 0;

        while(currentIndex <= input.length()) {
            var stringPart = input.substring(0, currentIndex);
            var currentValue = replaceWordsToDigitsSimple(stringPart);

            if(!currentValue.equals(stringPart)) {
                var result = currentValue + input.substring(currentIndex);
                System.out.println("Find from beginning result: " + result);
                return result;
            }
            currentIndex++;
        }

        return input;
    }

    private static String findFromEnd(String input) {
        var currentIndex = input.length() - 1;

        while(currentIndex > 0) {
            var stringPart = input.substring(currentIndex);
            var currentValue = replaceWordsToDigitsSimple(stringPart);

            if(!currentValue.equals(stringPart)) {
                var result = input.substring(0, currentIndex) + currentValue;
                System.out.println("Find from end result: " + result);
                return result;
            }
            currentIndex--;
        }

        return input;
    }

    private static String replaceDigitsToWords(String input) {
        return input
                .replaceAll("1","one")
                .replaceAll("2","two")
                .replaceAll("3","three")
                .replaceAll("4","four")
                .replaceAll("5","five")
                .replaceAll("6","six")
                .replaceAll("7","seven")
                .replaceAll("8","eight")
                .replaceAll("9","nine");

    }

    private static String replaceWordsToDigitsSimple(String input) {
        return input
                .replaceAll("one", "1")
                .replaceAll("two", "2")
                .replaceAll("three", "3")
                .replaceAll("four", "4")
                .replaceAll("five", "5")
                .replaceAll("six", "6")
                .replaceAll("seven", "7")
                .replaceAll("eight", "8")
                .replaceAll("nine", "9");
    }

    private static List<String> loadInputData() {
        var stringMap = """
                """;
        return Arrays.asList(stringMap.split("\n"));
    }
}
