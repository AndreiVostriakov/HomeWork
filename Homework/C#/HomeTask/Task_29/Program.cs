// Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму 
// натуральных элементов в промежутке от M до N.

// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30

Console.Clear();

int Recursiv(int N, int M)
{
    if (N == M) return N;
    else
    {
        return Recursiv(N + 1, M) + N;
    }

}

Console.Write("Введите число N: ");
int N = int.Parse(Console.ReadLine());
Console.Write("Введите число M: ");
int M = int.Parse(Console.ReadLine());
int sum = Recursiv(N, M);
Console.Write(sum);