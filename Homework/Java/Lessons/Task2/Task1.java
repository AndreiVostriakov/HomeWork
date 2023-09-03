package Homework.Java.Lessons.Task2;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        LinkedList<String> ll = new LinkedList<>();
        Collections.addAll(ll, "apple", "orange", "banana");
        while (true) {
            System.out.println("Введите параметры");
            String input = sc.next();
            String[] arrString = input.split("~");

            Integer index = Integer.parseInt(arrString[1]);
            if (arrString[0].equals("print")) {
                System.out.println(ll.get(index - 1));
            }
            if (arrString.length != 2 || index < 0) {
                System.out.println("Некоректный ввод");
                continue;
            }

            for (int i = ll.size(); i < index - 1; i++) {
                ll.add(null);
            }

            ll.add(index - 1, arrString[0]);
            System.out.println(ll);
        }

    }
}
