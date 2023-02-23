using System.Resources;
// Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.

int[,] GetArray(int m, int n, int minValue, int maxValue)
{
    int[,] result = new int[m, n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(minValue, maxValue + 1);
        }
    }
    return result;
}

void PrintArray(int[,] inArray)
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            Console.Write($"{inArray[i, j]}\t ");
        }
        Console.WriteLine();
    }
}

int[] SumOfEachLine(int[,] inArray)
{
    int[] oldArray = new int[inArray.GetLength(0)];
    int sum = 0;
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            sum += inArray[i, j];
            oldArray[i] = sum;
        }
        sum = 0;
    }
    return oldArray;
}

void MinSum(int[] inArray)
{
    int minNum = inArray[0];
    int numberRow = 1;
    for (int i = 1; i < inArray.Length; i++)
    {
        if (minNum > inArray[i])
        {
            minNum = inArray[i];
            numberRow++;
        }
    }
    Console.Write($" В {numberRow} строке сумма элементов самая маленькая, и равна {minNum}");
}

Console.Write("Введите кол-во строк: ");
int row = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов: ");
int col = int.Parse(Console.ReadLine()!);

int[,] array = GetArray(row, col, 0, 10);

PrintArray(array);
Console.WriteLine();
int[] newArray = SumOfEachLine(array);
MinSum(newArray);
