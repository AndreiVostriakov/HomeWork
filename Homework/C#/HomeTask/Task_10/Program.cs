// Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.

Console.Clear();

Console.Write("Введите координаты по оси X для первой точки: ");
int x1 = int.Parse(Console.ReadLine());
Console.Write("Введите координаты по оси Y для первой точки: ");
int y1 = int.Parse(Console.ReadLine());
Console.Write("Введите координаты по оси Z для первой точки: ");
int z1 = int.Parse(Console.ReadLine());

Console.Write("Введите координаты по оси X для второй точки: ");
int x2 = int.Parse(Console.ReadLine());
Console.Write("Введите координаты по оси Y для второй точки: ");
int y2 = int.Parse(Console.ReadLine());
Console.Write("Введите координаты по оси Z для второй точки: ");
int z2 = int.Parse(Console.ReadLine());

double SquareX = Math.Pow((x1 - x2), 2);
double SquareY = Math.Pow((y1 - y2), 2);
double SquareZ = Math.Pow((z1 - z2), 2);


double length = Math.Sqrt(SquareX + SquareY + SquareZ);
// C = Math.Round(C, 2);

Console.Write($"{length:f2}");
