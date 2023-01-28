// Напишите программу, которая будет выдавать название дня недели по заданному номеру.

Console.Clear();

Console.Write("Введите номер дня недели: ");
int num = Convert.ToInt32(Console.ReadLine());

if(num == 1)
{
    Console.WriteLine("Это Понедельник");
}
else if(num == 2)
{
    Console.WriteLine("Это Вторник");
}
else if(num == 3)
{
    Console.WriteLine("Это Среда");
}
else if(num == 4)
{
    Console.WriteLine("Это Четверг");
}
else if(num == 5)
{
    Console.WriteLine("Это Пятница");
}
else if(num == 6)
{
    Console.WriteLine("Это Суббота");
}
else if(num == 7)
{
    Console.WriteLine("Это Воскресенье");
}
else
{
    Console.WriteLine("Я не знаю такого дня недели");
}





// Console.WriteLine("Если захотите выйти введите 100");

// int num;
// while(true)
// {
//     Console.Write("Введите номер дня недели: ");
//     num = int.Parse(Console.ReadLine());
//     switch (num)
//     {
//         case 1:
//             Console.WriteLine("Это Понедельник");
//             break;
//         case 2:
//             Console.WriteLine("Это Вторник");
//             break;
//         case 3:
//             Console.WriteLine("Это Среда");
//             break;
//         case 4:
//             Console.WriteLine("Это Четверг");
//             break;
//         case 5:
//             Console.WriteLine("Это Пятница");
//             break;
//         case 6:
//             Console.WriteLine("Это Суббота");
//             break;
//         case 7:
//             Console.WriteLine("Это Воскресенье");
//             break;
//         default:
//             Console.WriteLine("Такого дня недели нет");
//             break;
//     }
//     if(num == 100);
// }