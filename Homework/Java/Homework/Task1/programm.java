package Homework.Java.Homework.Task1;


public class programm {
    public static void main(String[] args) {
        String str = "aaaabbbcddfg";
        System.out.print(compressString(str));
    }

    // Напишите метод, который сжимает строку.
    //Пример: вход aaaabbbcdd.
    //
    //10:43
    //a4b3cd2
    public static String compressString(String str) {
        int counter = 1;
        StringBuilder compressed = new StringBuilder();
        char current = str.charAt(0);
        char prev = current;

        for (int i = 1; i < str.length(); i++) {
            prev = str.charAt(i-1);
            current = str.charAt(i);

            if (prev != current) {
                compressed.append(prev);
                if (counter != 1) {
                    compressed.append(counter);
                }
                counter = 0;
            }
            counter = counter + 1;

        }

        compressed.append(current);
        if (counter >1) {
            compressed.append(counter);
        }

        return compressed.toString();
    }
}