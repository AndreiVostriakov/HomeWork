//  Напишите программу, которая будет преобразовывать 
// десятичное число в двоичное

Console.Clear();

string DecToBin(int num)
{
    string result = "";
    while (num > 0)
    {
        result = (num % 2).ToString() + result;
        num /= 2;
    }
    return result;
}

Console.WriteLine("Введите число");
int x = int.Parse(Console.ReadLine());
Console.WriteLine(DecToBin(x));