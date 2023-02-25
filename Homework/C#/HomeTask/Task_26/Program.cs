// Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.

int[,,] GetArray(int m, int n, int t)
{
    int[,,] result = new int[m, n, t];
    var rnd = new Random();
    int[] listOfNumbers = Enumerable.Range(10, 89).OrderBy(x => rnd.Next()).Take(89).ToArray();
    int index = 0;
    for (int i = 0; i < result.GetLength(0); i++)
    {
        for (int j = 0; j < result.GetLength(1); j++)
        {
            for (int k = 0; k < result.GetLength(2); k++)
            {
                result[i, j, k] = listOfNumbers[index];
                index++;
            }
        }
    }
    return result;
}

void PrintArray(int[,,] inArray)
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1); j++)
        {
            for (int k = 0; k < inArray.GetLength(2); k++)
            {
                Console.Write($"{inArray[i, j, k]} ({i},{j},{k}) \t ");
            }
            Console.WriteLine(" ");
        }
        Console.WriteLine(" ");
    }
    Console.WriteLine(" ");
}

Console.Write("Введите кол-во страниц: ");
int page = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во столбцов: ");
int col = int.Parse(Console.ReadLine()!);
Console.Write("Введите кол-во строк: ");
int row = int.Parse(Console.ReadLine()!);


int[,,] array = GetArray(page, row, col);

PrintArray(array);
Console.WriteLine();

