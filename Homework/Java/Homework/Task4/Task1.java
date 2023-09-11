package Homework.Java.Homework.Task4;

import java.util.LinkedList;

class MyQueue<T> {

    final LinkedList<T> states = new LinkedList<>();

    public void enqueue(T element) {
        // Напишите свое решение ниже
        states.addLast(element);
    }

    public T dequeue() {
        // Напишите свое решение ниже
        T firstElement = states.removeFirst();
        return firstElement;
    }

    public T first() {
        // Напишите свое решение ниже
        T firstElementWithoutRemove = states.getFirst();
        return firstElementWithoutRemove;
    }

    public LinkedList<T> getElements() {
        // Напишите свое решение ниже
        return states;
    }
}

public class Task1 {
    public static void main(String[] args) {
        MyQueue<Object> queue;
        queue = new MyQueue<>();

        if (args.length == 0) {
            // При отправке кода на Выполнение, вы можете варьировать эти параметры
            queue.enqueue(18);
            queue.enqueue(26);
            queue.enqueue(53);
            queue.enqueue(90);
        } else {
            queue.enqueue(Integer.parseInt(args[0]));
            queue.enqueue(Integer.parseInt(args[1]));
            queue.enqueue(Integer.parseInt(args[2]));
            queue.enqueue(Integer.parseInt(args[3]));
        }

        // System.out.println(queue.getElements());

        queue.dequeue();
        queue.dequeue();
        // System.out.println(queue.getElements());

        System.out.println(queue.first());
    }
}








// import java.util.LinkedList;

// class MyQueue<T> {
//     private LinkedList<T> elements = new LinkedList<>();

//     public MyQueue() {
//     }

//     public MyQueue(LinkedList<T> elements) {
//         this.elements = elements;
//     }

//     public void enqueue(T element){
//         elements.add(element);
//     }

//     public T dequeue(){
//         T first = elements.getFirst();
//         elements.removeFirst();
//         return first;
//     }

//     public T first(){
//         return elements.getFirst();
//     }

//     public LinkedList<T> getElements() {
//         return elements;
//     }

//     public void setElements(LinkedList<T> elements) {
//         this.elements = elements;
//     }
// }

// public class Printer {
//     public static void main(String[] args) {
//         MyQueue<Integer> queue;
//         queue = new MyQueue<>();

//         if (args.length == 0) {
//             queue.enqueue(1);
//             queue.enqueue(10);
//             queue.enqueue(15);
//             queue.enqueue(5);
//         } else {
//             queue.enqueue(Integer.parseInt(args[0]));
//             queue.enqueue(Integer.parseInt(args[1]));
//             queue.enqueue(Integer.parseInt(args[2]));
//             queue.enqueue(Integer.parseInt(args[3]));
//         }

//         System.out.println(queue.getElements());

//         queue.dequeue();
//         queue.dequeue();
//         System.out.println(queue.getElements());

//         System.out.println(queue.first());
//     }
// }