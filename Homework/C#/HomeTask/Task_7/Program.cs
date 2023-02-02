// // Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

// Console.Clear();

// string[] week = { "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" };


// Console.Write("Введите цифру обозначающую день недели: ");
// int number = int.Parse(Console.ReadLine());

// int index = number - 1;

// if (index < week.Length)
// {
//     if (number <= 5)
//     {
//         Console.WriteLine($"Дак, это {week[index]} и это рабочий день");
//     }
//     else
//     {
//         Console.WriteLine($"Дак, это {week[index]} и это выходной день");
//     }
// }
// else
// {
//     Console.WriteLine("Такого дня недели нет");
// }



Console.Clear();

Console.Write("Введите цифру обозначающую день недели: ");
int number = int.Parse(Console.ReadLine());

if (number > 0 && number <= 5)
{
    Console.WriteLine("Это рабочий день");
}
else if (number >5 && number <= 7)
{
    Console.WriteLine("Это выходной день");
}
else
{
    Console.WriteLine("Такого дня недели не существует");
}