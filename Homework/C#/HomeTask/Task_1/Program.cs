// Напишите программу, которая на вход принимает два числа и выдает, какое число большее, а какое меньшее.

Console.Clear();

Console.Write("Введите первое число: ");
int num_1 = int.Parse(Console.ReadLine());
Console.Write("Введите второе число: ");
int num_2 = int.Parse(Console.ReadLine());

if(num_1 > num_2)
{
    Console.WriteLine("Первое число больше второго. Значит число " + num_1 + " максимальное, а число " + num_2 + " минимальное ");
}
else
{
    Console.WriteLine("Второе число больше первого. Значит число " + num_2 + " максимальное, а число " + num_1 + " минимальное");
}
