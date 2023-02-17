// Пользователь вводит с клавиатуры М чисел.
// Посчитайте, сколько чисел больше 0 ввел пользователь

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

int positiveNumbers(int[] inArray)
{
    int count = 0;
    foreach (int element in inArray)
    {
        if (element > 0)
        {
            count++;
        }
    }
    return count;
}

Console.WriteLine("Введите цифру, указывающуу кол-во чисел в сгенерированном массиве:");
int M = int.Parse(Console.ReadLine());
int[] array = GetArray(M, -100, 100);
Console.WriteLine(string.Join(", ", array));
int total = positiveNumbers(array);
Console.WriteLine(total);