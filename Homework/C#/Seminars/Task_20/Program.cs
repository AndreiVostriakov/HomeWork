// Задача 33: Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве.

Console.Clear();

int[] GetArray(int size, int minValue, int maxValue)
{
    int[] result = new int[size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new Random().Next(minValue, maxValue + 1);
    }
    return result;
}

bool FindNumber (int[] InArray, int number)
{
    foreach (int element in InArray)
    {
        if (element == number)
        {
            return true;
        }
    }
    return false;
}

int[] array = GetArray(5, -10, 10);
Console.WriteLine(String.Join(", ", array));
int num = int.Parse(Console.ReadLine());
if (FindNumber(array, num))
{
    Console.WriteLine("Yes");
}
else
{
    Console.WriteLine("No");
}