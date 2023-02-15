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
    for (int m = 0; m < OldArray.Length - 1; m++)
    {
        for (int j = m + 1; j < OldArray.Length; j++)
        {
            if (OldArray[j] > OldArray[m])
            {
                temp = OldArray[j];
                OldArray[j] = OldArray[m];
                OldArray[m] = temp;
            }
        }
    }
    return OldArray;
}

Console.Clear();

int[] array = Getarray(11, 0, 20);
Console.WriteLine(string.Join(", ", array));

int[] newArray = sortArray(array);
Console.WriteLine(string.Join(", ", newArray));