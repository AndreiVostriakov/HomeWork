// Напишите программу, которая на вход принимает два числа и проверяет, является ли первое число квадратом второго.
Console.Clear();

Console.WriteLine("Введите первое число: ");
int number_1 = int.Parse(Console.ReadLine());

Console.WriteLine("Введите второе число:");
int number_2 = int.Parse(Console.ReadLine());

int sqr = number_2 * number_2;

if(sqr == number_1)
{
    Console.WriteLine($"{number_1} является квадратом {number_2}");
}
else
{
    Console.WriteLine($"{number_1} не является квадратом {number_2}");
}
