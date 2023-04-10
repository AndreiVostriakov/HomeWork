# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            print(f"{X} {Y} {Z} = {int(not(X and Y) or Z)}\t")
                
