// напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа.

Console.Clear();

Console.Write("Введите трёхзначное число: ");
int num = int.Parse(Console.ReadLine());

int num_1 = num % 10;
Console.Write(num_1);