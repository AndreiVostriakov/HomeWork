// Напишите программу, которая будет создавать копию заданного массива с помощью поэлементного копирования

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

int[] CopyArray(int[] inArray)
{
    int[] array = new int[inArray.Length];
    for (int i = 0; i < inArray.Length; i++)
    {
        array[i] = inArray[i];
    }
    return array;

}

int[] array = GetArray(5, -10, 10);
Console.WriteLine(string.Join(", ", array));
int[] CopyArr = CopyArray(array);
Console.WriteLine(string.Join(", ", CopyArr));