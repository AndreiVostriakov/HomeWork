// Напишите программу, которая выводит случайное трехзначное число и удаляет вторую цифру этого числа.

Console.Clear();

int num = new Random().Next(100, 1000);
int a1 = num / 100;
int a2 = num % 10;

int max = a1;

if (max < a2)
{
    max = a2;
}
Console.WriteLine($"Рандомное число {num}");
Console.WriteLine($"Получилось число: {num / 100 * 10 + num % 10}");


// Console.Clear();

// int a = new Random().Next(100, 1000);
// int result = a / 100 * 10 + a % 10;
// Console.WriteLine($"Рандомное число: {a}");
// Console.WriteLine($"Получилось число: {result}");