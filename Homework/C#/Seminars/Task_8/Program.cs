// Напишите программу, которая будет принимать на вход два числа и выводит, 
// является ли второе число кратным первому. 
// Если число 2 не кратно числу 1, 
// то программа выводит остаток от деления

Console.Clear();

Console.Clear();

Console.Write("Введите первое число: ");
int num1 = int.Parse(Console.ReadLine()!);
Console.Write("Введите второе число: ");
int num2 = int.Parse(Console.ReadLine()!);

int ost = num1 % num2;
if (ost == 0) Console.WriteLine("Кратно");
else Console.WriteLine($"Не кратно, остаток {ost}");


// Console.Clear();
//  int first = new Random().Next(1,100);
//  int second = new Random().Next(1,100);
//  int ost = first % second;
// if (ost == 0) Console.WriteLine($"Число {first} кратное {second}");
// else Console.WriteLine($"Остаток от деления {ost}");