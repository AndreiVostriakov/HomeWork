// Задайте двумерный массив из целых чисел. Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.

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

int[] MinElementToArray2D(int[,] inArray)
{
    int min = inArray[0, 0];
    int minrow = 0;
    int mincol = 0;
    for (int i = 0; i < inArray.GetLength(dimension: 0); i++)
    {
        for (int j = 0; j < inArray.GetLength(dimension: 1); j++)
        {
            if (min > inArray[i, j])
            {
                min = inArray[i, j];
                minrow = i;
                mincol = j;
            }
        }
    }
    return new int[] {minrow, mincol};
}

int[,] DeleteArray(int[,] inArray, int[] minIndexes)
{
    int[,] result = new int[inArray.GetLength(0) - 1, inArray.GetLength(1) - 1];
    int row = 0;
    int col = 0;
    for (int i = 0; i < inArray.GetLength(dimension: 0); i++)
    {
        if (i == minIndexes[0])
        {
            continue;
        }
        for (int j = 0; j < inArray.GetLength(dimension: 1); j++)
        {
            if (j != minIndexes[1])
            {
                result[row, col] = inArray[i, j];
                col++;
            }
            
        }
        row++;
        col = 0;
    }
    return result;
}



Console.Write("Введите кол-во строк: ");
int row = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов: ");
int col = int.Parse(Console.ReadLine()!);

int[,] array = GetArray(row, col, 0, 10);

PrintArray(array);
Console.WriteLine();
int[] minIndex = MinElementToArray2D(array);
int[,] result = DeleteArray(array, minIndex);
PrintArray(result);