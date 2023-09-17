package Homework.Java.Homework.Task6;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;
import java.util.Scanner;

class Book {
    private HashMap<String, TreeSet<String>> phoneBook;

    public Book() {
        phoneBook = new HashMap<>();
    }

    public void addContackt(String name, String phoneNumber) {
        TreeSet<String> phones = phoneBook.getOrDefault(name, new TreeSet<>());
        phones.add(phoneNumber);
        phoneBook.put(name, phones);
    }

    public void removeContackt(String name, String phoneNumber) {
        TreeSet<String> phones = phoneBook.getOrDefault(name, new TreeSet<>());
        phones.remove(phoneNumber);
        if (phones.isEmpty()) {
            phoneBook.remove(name);
        } else {
            phoneBook.put(name, phones);
        }
    }

    public TreeSet<String> getPhones(String name) {
        return phoneBook.get(name);
    }

    public HashMap<String, TreeSet<String>> getAllContacts() {
        return phoneBook;
    }

    public void printBook() {
        for (String name : phoneBook.keySet()) {
            TreeSet<String> phones = phoneBook.get(name);
            System.out.println(name + ": " + phones);
        }
    }

    public List<String> sortContactsByPnones() {
        List<Map.Entry<String, TreeSet<String>>> sortedEntries = new ArrayList<>(phoneBook.entrySet());
        sortedEntries.sort((e1, e2) -> e2.getValue().size() - e1.getValue().size());

        List<String> result = new ArrayList<>();
        for (Map.Entry<String, TreeSet<String>> entry : sortedEntries) {
            result.add(entry.getKey() + ": " + entry.getValue());
        }
        return result;
    }

}

public class Task6 {
    public static void main(String[] args) {
        Book phoneBook = new Book();

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
                phoneBook.addContackt(lastName, phoneNumber);
                System.out.println("Контакт успешно добавлен");
            } else if (command.startsWith("GET")) {
                String[] parts = command.split(" ");
                if (parts.length != 2) {
                    System.out.println("неверный формат команды GET");
                    continue;
                }
                String lastName = parts[1];
                TreeSet<String> phones = phoneBook.getPhones(lastName);
                if (phones.isEmpty()) {
                    System.out.println("Не найдена запись с фамилией " + lastName);
                } else {
                    System.out.println("Номера: " + phones);
                }
            } else if (command.startsWith("REMOVE")) {
                String[] parts = command.split(" ");
                if (parts.length != 3) {
                    System.out.println("неверный формат команды REMOVE");
                    continue;
                }
                String lastName = parts[1];
                String phoneNumber = parts[2];
                TreeSet<String> phones = phoneBook.getPhones(lastName);
                if (phones.isEmpty()) {
                    System.out.println("Не найдена запись с фамилией " + lastName);
                } else {
                    phoneBook.removeContackt(lastName, phoneNumber);
                    System.out.println("Контакт удалён");
                }
            } else if (command.equals("LIST")) {
                List<String> sortedContacts = phoneBook.sortContactsByPnones();
                System.out.println("Контакты отсортированы по телефонам: ");
                for (String contact : sortedContacts) {
                    System.out.println(contact);
                }
            } else if (command.equals("EXIT")) {
                flag = false;
            } else {
                System.out.println("Неизвестная команда");
            }
        }
    }
}
