// Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.

Console.Clear();

Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine());
int num = number;

if (number < 100)
{
    Console.WriteLine($"Третьей цифры в числе {number} нет");
}

while (num >= 100)
{
    if (num < 1000)
    {
        int result = num % 10;
        Console.WriteLine($"Третья цифра числа {number} является {result}");
        break;
    }
    num /= 10;
}
