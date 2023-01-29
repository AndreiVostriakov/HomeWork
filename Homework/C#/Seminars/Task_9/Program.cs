// Напишите программу, которая будет принимать на вход два число и проверяет, кратно ли оно одновременно 7 и 23

Console.Clear();

Console.Write("Введите первое число: ");
int num = int.Parse(Console.ReadLine()!);


if (num % 7 == 0 && num % 23 == 0)
{
    Console.WriteLine($"{num} кратно 7 и 23");
}
else
{
    Console.WriteLine($"{num} не кратно 7 и 23");
}