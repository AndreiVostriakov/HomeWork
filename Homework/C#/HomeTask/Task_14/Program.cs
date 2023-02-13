//Задайте массив заполненный случайными положительными трёхзначными числами. 
//Напишите программу, которая покажет кол-во чётных чисел в массиве.

int[] Getarray(int size, int minValue, int maxValue)
{
    int[] result = new int[size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new Random().Next(minValue, maxValue + 1);
    }
    return result;
}

Console.Clear();

Console.Write("Введите число, обозначающее кол-во чисел в массиве: ");
int number = int.Parse(Console.ReadLine());

int[] array = Getarray(number, 100, 999);
Console.WriteLine(string.Join(", ", array));

int count = 0;

foreach (int element in array)
{
    if (element % 2 == 0)
    {
        count++;
    }
}

Console.WriteLine($"Кол-во чётных числе в массиве равна: {count}");