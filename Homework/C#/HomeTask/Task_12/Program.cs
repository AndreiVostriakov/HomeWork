// Написать программу вычисления произведения чисел от 1 до N

Console.Clear();

Console.Write("Введите число: ");
int N = int.Parse(Console.ReadLine());

int result = 1;

for (int i = 1; i <= N; i++)
{
    result *= i;
}
Console.WriteLine($"Произведение чисел от 1 до {N} равно {result}");