package Homework.Java.Homework.Task2;

import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;


public class Tasktwo {
    public static void main(String[] args) {
        int[] arr = { 9, 4, 8, 3, 1 };
        // int[] arr = {9, 3, 4, 8, 2, 5, 7, 1, 6, 10};
        sort(arr);
    }

    public static void sort(int[] arr) {
        try (FileWriter writer = new FileWriter("log.txt")) {
            SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm");
            String times;
            for (int i = 0; i < arr.length; i++) {
                boolean flag = true;
                for (int j = 0; j < arr.length - (i + 1); j++) {
                    if(arr[j] > arr[j + 1]) {
                        flag = false;
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
                times = sdf.format(new Date());
                writer.write(times + " " + Arrays.toString(arr) + System.lineSeparator());
                if (flag) break;
            }
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}



