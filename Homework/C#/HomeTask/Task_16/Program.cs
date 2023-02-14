// Задайте массив вещественных чисел.
// Найдите разницу между максимальным и минимальным элементом массива.

double[] Gatearray(int size, int minValue, int maxValue)
{
    Random rand = new Random();
    double[] result = new double[size];
    for (int i = 0; i < result.Length; i++)
    {
        result[i] = Math.Round(rand.NextDouble() + rand.Next(minValue, maxValue + 1), 2);
    }
    return result;
}

double Number(double[] array)
{
    double maxNum = array[0];
    double minNum = array[0];
    if (maxNum > array[1])
    {
        minNum = array[0];
    }
    else
    {
        maxNum = array[1];
    }

    for (int j = 2; j < array.Length; j++)
    {
        if (maxNum > array[j])
        {
            if (minNum > array[j])
            {
                minNum = array[j];
            }
        }
        maxNum = array[j];
    }
    return maxNum - minNum;
}


Console.Clear();

double[] array = Gatearray(5, -10, 10);
Console.WriteLine(string.Join(", ", array));

double difference = Number(array);
Console.WriteLine(difference);

