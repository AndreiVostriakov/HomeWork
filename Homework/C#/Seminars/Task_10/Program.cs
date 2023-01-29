// Напишите программу, которая будет принимать на вход два числа и проверяет, кратно ли оно число квадратом другого.

Console.Clear();

Console.Write("Введите первое число: ");
int num1 = int.Parse(Console.ReadLine()!);
Console.Write("Введите первое число: ");
int num2 = int.Parse(Console.ReadLine()!);

int a1 = num1 * num1;
int a2 = num2 * num2;
if (a1 == num2 || a2 == num1)
{
    Console.WriteLine("Да");
}
else
{
    Console.WriteLine("Нет");
}



// Console.Clear();
//  int first = Convert.ToInt32(Console.Readline());
//  int second = Convert.ToInt32(Console.Readline());
//  if (Math.Pow(first) == second) Console.WriteLine($"Первое число {first} является квадратом второго {second}");
//  else if (Math.Pow(second) == first) Console.WriteLine($"Второе число {second} является квадратом превого {first}");
//  else Console.WriteLine(" Числа не являются квадратами другого");
