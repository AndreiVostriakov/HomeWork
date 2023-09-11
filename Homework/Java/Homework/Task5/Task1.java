package Homework.Java.Homework.Task5;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

class PhoneBook {
    private Map<String, List<String>> phoneBook;

    public PhoneBook() {
        phoneBook = new HashMap<>();
    }

    public void add(String lastName, String phoneNumber) {
        List<String> numbers = phoneBook.getOrDefault(lastName, new ArrayList<>());
        numbers.add(phoneNumber);
        phoneBook.put(lastName, numbers);
    }

    public List<String> get(String lastName) {
        return phoneBook.getOrDefault(lastName, Collections.emptyList());
    }

    public void remove(String lastName) {
        phoneBook.remove(lastName);
    }

    public void list() {
        for (Map.Entry<String, List<String>> entry : phoneBook.entrySet()) {
            String lastName = entry.getKey();
            List<String> numbers = entry.getValue();
            System.out.println(lastName + ": " + numbers);
        }
    }
}

public class Task1 {
    public static void main(String[] args) {
        PhoneBook phoneBook = new PhoneBook();
        Scanner sc = new Scanner(System.in);
        boolean flag = true;
        while (flag) {
            System.out.println("Введите команду: ");
            String command = sc.nextLine();

            if (command.startsWith("ADD")) {
                String[] parts = command.split(" ");
                if (parts.length != 3) {
                    System.out.println("Неверный формат команды ADD");
                    continue;
                }
                String lastName = parts[1];
                String phoneNumber = parts[2];
                phoneBook.add(lastName, phoneNumber);
                System.out.println("Контакт успешно добавлен");
            } else if (command.startsWith("GET")) {
                String[] parts = command.split(" ");
                if (parts.length != 2) {
                    System.out.println("неверный формат команды GET");
                    continue;
                }
                String lastName = parts[1];
                List<String> numbers = phoneBook.get(lastName);
                if (numbers.isEmpty()) {
                    System.out.println("Не найдена запись с фамилией " + lastName);
                } else {
                    System.out.println("Номера: " + numbers);
                }
            } else if (command.startsWith("REMOVE")) {
                String[] parts = command.split(" ");
                if (parts.length != 2) {
                    System.out.println("неверный формат команды REMOVE");
                    continue;
                }
                String lastName = parts[1];
                List<String> numbers = phoneBook.get(lastName);
                if (numbers.isEmpty()) {
                    System.out.println("Не найдена запись с фамилией " + lastName);
                } else {
                    phoneBook.remove(lastName);
                    System.out.println("Контакт удалён");
                }
            } else if (command.equals("LIST")) {
                phoneBook.list();
            } else if (command.equals("EXIT")) {
                flag = false;
            } else {
                System.out.println("Неизвестная команда");
            }
        }
    }
}
