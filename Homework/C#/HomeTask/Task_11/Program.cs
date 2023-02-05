// Посчитать сумму цифр в числе

Console.Clear();

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine());

int result = num % 10;

while (num != 0)
{
    num /= 10;
    result += num % 10;
}

Console.WriteLine($"Сумма цифр в числе равна {result}");