package Homework.Java.Homework.Task2;

import java.util.Arrays;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class Task1 {

    private static final Logger logger = Logger.getLogger(Task1.class.getName());

    public static void main(String[] args) throws Exception {
        int[] mas = new int[] { 9, 4, 8, 3, 1 };
        sort(mas);
    }

    public static void sort(int[] arr) {    
        try {
            FileHandler fh = new FileHandler("log.txt");
            logger.addHandler(fh);
            SimpleFormatter sFormatter = new SimpleFormatter();
            fh.setFormatter(sFormatter);
        } catch (Exception e) {
            e.printStackTrace();
        }
        int temp = 0;
        for (int i = arr.length - 1; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
            logger.info(Arrays.toString(arr) + "\n");
        }
    }
}