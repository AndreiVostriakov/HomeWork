// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.

Console.Clear();

Console.Write("Введите число: ");
int N = int.Parse(Console.ReadLine());

int count = 1;

while (count <= N)
{
    Console.Write($"{count} в 3 степени равен " + count * count * count);
    if (count != N)
    {
        Console.WriteLine(", ");
    }
    count++;
}