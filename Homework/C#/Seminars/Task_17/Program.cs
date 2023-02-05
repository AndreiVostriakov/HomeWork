using System.Runtime.InteropServices;
// Определить количество цифр в числе

Console.Clear();

Console.Write("Введите число: ");
int A = int.Parse(Console.ReadLine());

int count = 0;

while (A != 0)
{
    A = A / 10;
    count++;
}

Console.Write(count);


// int count = 1;

// while (A >= 0 || A <= -10)
// {
//     A = A / 10;
//     count++;
// }

// Console.Write(count);