// напишите программу которая перевернёт одномерный массив.
// (последний элемент будет на первом месте, а первый на последнем)
// [1, 2, 3, 4, 5, 6] == [6, 5, 4, 3, 2, 1]
// [6, 7, 3, 6] == [6, 3, 7, 6]

int[] GetArray(int size, int minValue, int maxValue)
{
    int[] result = new int[size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new Random().Next(minValue, maxValue + 1);
    }
    return result;
}

void ReversArray1(int[] inArray)
{
    for (int i = 0; i < inArray.Length / 2; i++)
    {
        int temp = inArray[i];
        inArray[i] = inArray[inArray.Length - 1 - i];
        inArray[inArray.Length - 1 - i] = temp;

    }
}

int[] ReversArray2(int[] inArray)
{
    int[] result = new int[inArray.Length];

    for (int i = 0; i < inArray.Length; i++)
    {
        result[i] = inArray[inArray.Length - 1 - i];
    }
    return result;
}

int[] array = GetArray(5, 0, 10);
Console.WriteLine(string.Join(", ", array));
ReversArray1(array);
Console.WriteLine(string.Join(", ", array));
int[] reversed = ReversArray2(array);
Console.WriteLine(string.Join(", ", reversed));
