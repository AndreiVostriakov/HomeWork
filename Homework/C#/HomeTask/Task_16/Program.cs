// Задайте массив вещественных чисел.
// Найдите разницу между максимальным и минимальным элементом массива.

double[] Gatearray(int size, int minValue, int maxValue)
{
    Random rand = new Random();
    double[] result = new double[size];
    for (int i = 0; i < result.Length; i++)
    {
        result[i] = Math.Round(rand.NextDouble() + rand.Next(minValue, maxValue + 1), 4);
    }
    return result;
}

double maximal(double[] everyArray)
{
    double maxNum = everyArray[0];
    for (int j = 1; j < everyArray.Length; j++)
    {
        if (everyArray[j] > maxNum)
        {
            maxNum = everyArray[j];
        }
    }
    return maxNum;
}

double minimal(double[] everyArray)
{
    double minNum = everyArray[0];
    for (int j = 1; j < everyArray.Length; j++)
    {
        if (everyArray[j] < minNum)
        {
            minNum = everyArray[j];
        }
    }
    return minNum;
}

Console.Clear();

double[] array = Gatearray(5, -10, 10);
Console.WriteLine(string.Join(", ", array));

double min = minimal(array);
double max = maximal(array);

Console.WriteLine($"Разность максимального значения {max} и минимального значения {min} массива равна: {max - min}");


// double Number(double[] everyArray)
// {
//     double maxNum = everyArray[0];
//     double minNum = everyArray[0];
//     if (everyArray[1] > maxNum)
//     {
//         maxNum = everyArray[1];
//     }
//     else
//     {
//         minNum = everyArray[1];
//     }

//     for (int j = 2; j < everyArray.Length; j++)
//     {
//         if (maxNum > everyArray[j])
//         {
//             if (everyArray[j] < minNum)
//             {
//                 minNum = everyArray[j];
//             }
//         }
//         maxNum = everyArray[j];
//     }
//     return maxNum minNum;
// }