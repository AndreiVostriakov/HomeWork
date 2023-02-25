// // Напишите программу, которая заполнит спирально массив 4 на 4.

int[,] GetArray(int row, int column)
{
    int[,] result = new int[row, column];
    int move;
    if (row > column)
    {
        move = row / 2;
    }
    else
    {
        move = column / 2;
    }

    int count = 0;
    for (int i = 0; i < move; i++)
    {
        for (int j = 0 + i; j < column - i; j++)
        {
            result[i, j] = count++;
        }
        if (count >= column * row)
        {
            break;
        }
        for (int k = 1 + i; k < row - i; k++)
        {
            result[k, column - 1 - i] = count++;
        }
        if (count >= column * row)
        {
            break;
        }
        for (int v = column - 2 - i; v >= 0 + i; v--)
        {
            result[row - 1 - i, v] = count++;
        }
        if (count >= column * row)
        {
            break;
        }
        for (int d = row - 2 - i; d > 0 + i; d--)
        {
            result[d, i] = count++;
        }

    }

    if (row == column && row % 2 == 1)
    {
        result[row / 2, column / 2] = count++;
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

Console.Write("Введите кол-во строк: ");
int row = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов: ");
int col = int.Parse(Console.ReadLine()!);

int[,] array = GetArray(row, col);

PrintArray(array);
Console.WriteLine();
