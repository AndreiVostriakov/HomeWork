// Задача 55: Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.

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

int[,] Inversed(int[,] inArray)
{
    int[,] NewArray = new int[inArray.GetLength(1), inArray.GetLength(0)];
    for (int i = 0; i < inArray.GetLength(1); i++)
    {
        for (int j = 0; j < inArray.GetLength(0); j++)
        {
            NewArray[i, j] = inArray[j, i];

        }
    }
    return NewArray;
}

int[,] array = GetArray(4, 4, -10, 10);

PrintArray(array);
Console.WriteLine();
if (array.GetLength(0) == array.GetLength(1))
{
    int[,] revers = Inversed(array);
    PrintArray(revers);
}
else
{
    Console.WriteLine("Выполнить смену строк на столбцы не возможно");
}


