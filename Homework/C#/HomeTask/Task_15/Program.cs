//Задайте одномерный массив, заполненный случайными числами.
//Найдите сумму элементов, стоящих на нечётных позициях.

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

Console.Write("Введите число, обозначающее кол-во элементов в массиве: ");
int number = int.Parse(Console.ReadLine());
Console.WriteLine("Введите 2 цифры, обозначающие в каком диапазоне буду сгенерированы случайные числа в массиве: ");
int num1 = int.Parse(Console.ReadLine());
int num2 = int.Parse(Console.ReadLine());

int[] array = Getarray(number, num1, num2);
Console.WriteLine(string.Join(", ", array));

int count = 0;

for(int j = 1; j < array.Length; j += 2)
{
    count += array[j];
}

Console.WriteLine($"Сумма элементов, стоящих на нечётных позициях в массиве равна: {count}");