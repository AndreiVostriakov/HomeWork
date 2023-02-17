// Задача 40: Напишите программу, которая принимает на вход три 
// числа и проверяет, может ли существовать треугольник со сторонами такой длины

bool CheckTreeEnd(int a, int b, int c)
{
    return(a + b > c && a + c > b && b + c > a);
}

Console.WriteLine("Введите первое число");
int x = int.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число");
int y = int.Parse(Console.ReadLine());
Console.WriteLine("Введите третье число");
int z = int.Parse(Console.ReadLine());

if (CheckTreeEnd(x, y, y))
{
    Console.WriteLine("Не существует");
}
else
{
    Console.WriteLine("Cуществует");
}