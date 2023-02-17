//  Не используя рекурсию, выведите первые N чисел 
// Фибоначчи. Первые два числа Фибоначчи: 0 и 1

Console.Clear();

int[] Fibonacci(int N)
{
    int[] result = new int[N];
    result[0] = 0;
    result[1] = 1;
    for (int i = 2; i < N; i++)
    {
        result[i] = result[i - 1] + result[i - 2];
    }
    return result;
}

Console.WriteLine("Введите число");
int x = int.Parse(Console.ReadLine());
int[] array = Fibonacci(x);
Console.WriteLine(string.Join(", ", array));