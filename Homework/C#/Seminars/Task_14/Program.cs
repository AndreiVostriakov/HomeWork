// Напишите программу, которая принимает на вход число (N) и выдаёт таблицу квадратов чисел от 1 до N.

Console.Clear();

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine());
int count = 1;

while (count <= num)
{
    Console.Write(count * count);
    if (count != num)
    {
        Console.Write(", ");
    }
    count++;
}