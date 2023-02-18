// Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.

// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет

double[,] GetArray(int m, int n, int minValue, int maxValue)
{
    double[,] result = new double[m, n];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = Math.Round(new Random().Next(minValue, maxValue + 1) + new Random().NextDouble(), 2);
        }
    }
    return result;
}

void PrintArray(double[,] inArray)
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

void Find(double[,] inArray, int line, int column)
{
    if (inArray.GetLength(0) > line && inArray.GetLength(1) > column)
    {
        Console.WriteLine(inArray[line, column]);
    }
    else
    {
        Console.WriteLine("Такого числа нет");
    }
}

Console.Clear();
double[,] array = GetArray(4, 4, 0, 10);
PrintArray(array);
Console.WriteLine();
Console.Write("Введите номер строки массива: ");
int row = int.Parse(Console.ReadLine());
Console.Write("Введите номер столбца массива: ");
int col = int.Parse(Console.ReadLine());
Find(array, row, col);