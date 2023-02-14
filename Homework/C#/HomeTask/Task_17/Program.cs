//Задайте массив, заполненный случайными числами.
//разработать алгоритм сортировки методом пузырька.Реализовать возврастающую сортировку.

int[] Getarray(int size, int minValue, int maxValue)
{
    int[] result = new int[size];

    for (int i = 0; i < size; i++)
    {
        result[i] = new Random().Next(minValue, maxValue + 1);
    }
    return result;
}

int[] sortArray(int[] OldArray)
{
    int temp;
    for (int i = 0; i < OldArray.Length - 1; i++)
    {
        for (int j = i + 1; j < OldArray.Length; j++)
        {
            if (OldArray[i] > OldArray[j])
            {
                temp = OldArray[i];
                OldArray[i] = OldArray[j];
                OldArray[j] = temp;
            }
        }
    }
    return OldArray;
}

Console.Clear();

int[] array = Getarray(10, 0, 10);
Console.WriteLine(string.Join(", ", array));

int[] newArray = sortArray(OldArray: array);
Console.WriteLine(newArray);