package Homework.Java.Homework.Task3;

import java.util.Arrays;
import java.lang.Integer;

public class Tasks3 {
    public static void main(String[] args) {
        Integer[] arr = new Integer[] { 4, 2, 7, 5, 1, 3, 8, 6, 9 };
        analyzeNumbers(arr);

    }

    public static void analyzeNumbers(Integer[] mas) {
        int max = mas[0];
        int min = mas[0];
        int avg = 0;

        for (int i = 0; i < mas.length; i++) {
            boolean flag = true;
            for (int j = 0; j < mas.length - (i + 1); j++) {
                if(mas[j] > mas[j + 1]) {
                    flag = false;
                    int temp = mas[j];
                    mas[j] = mas[j + 1];
                    mas[j + 1] = temp;
                }
            }
        }

        for (Integer i : mas) {
            if (i < min) min = i;
            if (i > max) max = i;
            avg += i;
        }

        avg /= mas.length;
        System.out.println(Arrays.toString(mas));
        System.out.println("Minimum is " + min);
        System.out.println("Maximum is " + max);
        System.out.println("Average is = " + avg);
    }    
}




// import java.util.Arrays;
// import java.util.ArrayList;

// class Answer {
//     public static void analyzeNumbers(Integer[] arr) {
//         ArrayList<Integer> ints = new ArrayList<>(Arrays.asList(arr));
//         ints.sort(Integer::compareTo); // сортировка списка по возрастанию
//         System.out.println(ints); // вывод списка на экран
//         System.out.println("Minimum is " + ints.get(0)); // нахождение минимального значения в списке и вывод на экран
//         System.out.println("Maximum is " + ints.get(ints.size()-1)); // нахождение максимального значения в списке и вывод на экран

//         int sum = 0;
//         for(int i : ints){ // вычисление суммы всех элементов списка
//             sum += i;
//         }
//         System.out.println("Average is = " + sum / ints.size()); // вычисление среднего арифметического значений списка и вывод на экран
//     }
// }

// public class Printer{ 
//     public static void main(String[] args) { 
//       Integer[] arr = {};

//       if (args.length == 0) {
//         arr = new Integer[]{4, 2, 7, 5, 1, 3, 8, 6, 9};
//       }
//       else{
//         arr = Arrays.stream(args[0].split(", "))
//                         .map(Integer::parseInt)
//                         .toArray(Integer[]::new);
//       }     

//       Answer ans = new Answer();      
//       ans.analyzeNumbers(arr);
//     }
// }