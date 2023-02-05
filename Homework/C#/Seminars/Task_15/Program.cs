// Посчитать сумму чисел от 1 до А

Console.Clear();

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine());

int count = 0;
for (int i = 1; i <= num; i++)
{
    count += i;
}
Console.Write(count);






