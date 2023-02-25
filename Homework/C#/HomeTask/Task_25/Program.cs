// Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.

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

int[,] MultiplicationArray(int[,] inArray1, int[,] inArray2)
{
    int[,] resultMultiplicationArray = new int[inArray1.GetLength(0), inArray2.GetLength(1)];
    for (int i = 0; i < inArray1.GetLength(0); i++)
    {
        for (int j = 0; j < inArray2.GetLength(1); j++)
        {
            resultMultiplicationArray[i, j] = 0;
            for (int k = 0; k < inArray1.GetLength(1); k++)
            {
                resultMultiplicationArray[i, j] += inArray1[i, k] * inArray2[k, j];
            }
        }
    }
    return resultMultiplicationArray;
}

Console.Write("Введите кол-во строк в первой матрице: ");
int row1 = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов в первой матрице: ");
int col1 = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во строк во второй матрице: ");
int row2 = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов во второй матрице: ");
int col2 = int.Parse(Console.ReadLine()!);

int[,] array1 = GetArray(row1, col1, 0, 10);
int[,] array2 = GetArray(row2, col2, 0, 10);

PrintArray(array1);
Console.WriteLine();
PrintArray(array2);
Console.WriteLine();
int[,] newArray;
if (array1.GetLength(1) == array2.GetLength(0))
{
    newArray = MultiplicationArray(array1, array2);
    PrintArray(newArray);
}
else if (array2.GetLength(1) == array1.GetLength(0))
{
    newArray = MultiplicationArray(array2, array1);
    PrintArray(newArray);
}
else
{
    Console.WriteLine("Матрицы нельзя перемножить");
}

