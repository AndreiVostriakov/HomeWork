package Homework.Java.Lessons.Task1;

import java.util.Scanner;

public class Tasks {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите первое число: ");
        int a = sc.nextInt();
        System.out.println("Введите второе число: ");
        int b = sc.nextInt();
        char ch = '+';
        int result = calculate(a, b, ch);
        System.out.println(result);
        sc.close();
    }

    public static int calculate(int a, int b, char op) {
        int x = 0;
        switch (op) {
            case '+':
                x = a + b;
                break;
            case '-':
                x = a - b;
                break;
            case '*':
                x = a * b;
                break;
            case '/':
                x = a / b;
                break;   
            default:
                System.out.println("Некорректный оператор: 'оператор'");
                break;
        }
        return x;
    }

}
