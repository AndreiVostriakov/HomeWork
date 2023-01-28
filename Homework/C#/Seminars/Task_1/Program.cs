// напишите программу, которая на входе принимает число и выводит квадрат (число умноженное на само себя).

Console.Clear();

Console.Write("Введите число: ");
int number = int.Parse(Console.ReadLine());

int sqr = number * number;

// ToInt32 это тоже самое что и int. Convert преобразует число из вещественного в целое число. Math библиотека математических действий. Pow возведение в степень, но оно возвращает вещественное число. Первое это число, а второе это степень.
// int sqr1 = Convert.ToInt32(Math.Pow(number, 2));

Console.WriteLine($"Квадрат числа {number} равен {sqr}");





