#### Задача 1

Решение: Для того, чтобы получить количество двоек у учеников с 10ю и более пятерками можно отправить SQL запрос:

```sql
SELECT name, SUM(CASE WHEN mark = 2 THEN 1 ELSE 0 END) as sum_two
FROM students
GROUP BY name
HAVING SUM(CASE WHEN mark = 5 THEN 1 ELSE 0 END) > 9
ORDER BY name
```

Данные из таблицы students группируются по имени студента, метод SUM подсчитывает количество двоек у студентов. Результат группировки фильтруется с помощью HAVING. ORDER BY сортирует результат по имени студента.

Результат выполнения работы на тестовой БД:

<img src="C:\Users\Сочный нектарин\AppData\Roaming\Typora\typora-user-images\image-20231101125254923.png" alt="image-20231101125254923" style="zoom:80%;" />

#### Задача 2

Решение: Для того, чтобы получить средний балл каждого ученика по каждому предмету можно отправить SQL запрос:

```sql
SELECT name, ROUND(AVG(mark), 2) as avg_mark, subject
FROM studentsSubject
GROUP BY name, subject
ORDER BY name, subject
```

Данные из таблицы students группируются по имени студента и предмету, метод AVG  вычисляет средней балл для каждого предмета и каждого студента. Метод ROUND округляет результат до двух знаков. ORDER BY сортирует результат по имени студента и предмету.

Результат выполнения работы на тестовой БД:

<img src="C:\Users\Сочный нектарин\AppData\Roaming\Typora\typora-user-images\image-20231101125915736.png" alt="image-20231101125915736" style="zoom:80%;" />

Я использовала докер PostgreSQL и библиотеку  psycopg2 для отправки запросов к бд. В папках FirstTask и SecondTask программы для создания базы данных и таблиц, заполнения их тестовыми данными и отправки запросов из заданий.
