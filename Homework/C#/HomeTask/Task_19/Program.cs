// напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями
//  y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем
// k1 = 5, b1 = 2, k2 = 9, b2 = 4, -> (-0,5; -0,5)

double findX(double a1, double c1, double a2, double c2)
{
    double x;
    x = Math.Round((c2 - c1) / (a1 - a2), 2);
    return x;
}

double findY(double a1, double c1, double a2, double c2, double x)
{
    double y;
    y = Math.Round(a1 * x + c1, 2);
    y = Math.Round(a2 * x + c2, 2);
    return y;
}

Console.WriteLine("Введите число к1");
double k1 = double.Parse(Console.ReadLine());
Console.WriteLine("Введите число b1");
double b1 = double.Parse(Console.ReadLine());
Console.WriteLine("Введите число к2");
double k2 = double.Parse(Console.ReadLine());
Console.WriteLine("Введите число b2");
double b2 = double.Parse(Console.ReadLine());

if (k1 != k2)
{
    double X = findX(k1, b1, k2, b2);
    double Y = findY(k1, b1, k2, b2, X);
    Console.WriteLine($"Две прямые имею 1 точку пересения c координатами ({X},{Y})");
}
else if (k1 == k2 && b1 == b2)
{
    Console.WriteLine("Две прямые совпадают и имеют множество общих точек");
}
else if (k1 == k2 && b1 != b2)
{
    Console.WriteLine("Прямые являются паралелльными и не имеют точек пересечения");
}
else
{
    Console.WriteLine("Прямые не имеют общих признаков и точек пересечения");
}

