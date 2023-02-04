// напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

Console.Clear();

Console.Write("Первая координатная точка по Х: ");
int x1 = int.Parse(Console.ReadLine());

Console.Write("Первая координатная точка по Y: ");
int y1 = int.Parse(Console.ReadLine());

Console.Write("Вторая координатная точка по Х: ");
int x2 = int.Parse(Console.ReadLine());
Console.Write("Вторая координатная точка по Y: ");
int y2 = int.Parse(Console.ReadLine());

double AB = Math.Pow((x1 - x2), 2);
double AB1 = Math.Pow((y1 - y2), 2);

double C = Math.Sqrt(AB + AB1);
// C = Math.Round(C, 2);

Console.Write($"{C:f2}");

