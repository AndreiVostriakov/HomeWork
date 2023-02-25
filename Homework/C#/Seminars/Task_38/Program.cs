// Задача 67: Напишите программу, которая будет принимать на вход число и
// возвращать сумму его цифр.
// 453 -> 12
// 45 -> 9

Console.Clear();

int SumNumber(int N)
{
    if (N == 0) return 0;
    else
    {
        return N % 10 + SumNumber(N / 10);
    }
}

int N = int.Parse(Console.ReadLine());
Console.Write(SumNumber(N));