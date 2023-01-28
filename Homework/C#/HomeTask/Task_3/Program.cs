// Напишите программу, которая на входе принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).

Console.Clear();

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine());

if(num % 2 == 0)
{
    Console.WriteLine("Число " + num + " является чётным.");
}
else
{
    Console.WriteLine("Число " + num + " не чётное.");
}