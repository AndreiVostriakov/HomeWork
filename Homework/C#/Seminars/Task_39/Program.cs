// Напишите программу, которая на вход принимает два числа A и B, и
// возводит число А в целую степень B с помощью рекурсии

int RaicingToPower(int a, int b)
{
    if (b == 0) return 1;
    else 
    {
        return a * RaicingToPower(a, b - 1);
    }
}

Console.WriteLine("введите число : ");
int n = int.Parse(Console.ReadLine()!);
Console.WriteLine("введите cтепень : ");
int m = int.Parse(Console.ReadLine()!);
Console.WriteLine(RaicingToPower(n, m));