// Напишите программу которая принимает на вход координаты точки (Х и Y), и выдаёт номер четверти в плоскости в которой находится точка.

Console.Clear();

Console.Write("Введите число X: ");
int X = int.Parse(Console.ReadLine());

Console.Write("Введите число Y: ");
int Y = int.Parse(Console.ReadLine());

if (Y > 0)
{
    if (X > 0)
    {
        Console.Write("Первая четверть");
    }
    else
    {
        Console.Write("Вторая четверть");
    }
}
else
{
    if (X < 0)
    {
        Console.Write("Третья четверть");
    }
    else
    {
        Console.Write("Четвёртая четверть");
    }
}