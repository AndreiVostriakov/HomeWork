// Задача 68: Напишите программу вычисления функции Аккермана с помощью 
// рекурсии. Даны два неотрицательных числа m и n. 

// m = 2, n = 3 -> A(n,m) = 9

Console.Clear();

int A(int m, int n)
{
    if (m == 0) return n + 1;
    if (m != 0 && n == 0) return A(m - 1, 1);
    if (m > 0 && n > 0) return A(m-1, A(m,n-1));
    else
    {
        return A(m,n);
    }

}

Console.Write("Введите число N: ");
int M = int.Parse(Console.ReadLine());
Console.Write("Введите число M: ");
int N = int.Parse(Console.ReadLine());
int akkerman = A(M, N);
Console.Write(akkerman);