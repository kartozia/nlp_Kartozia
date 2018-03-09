### HW RAKE
#### Совместно с Машей Бибаевой
- [x] [текст про фильм "Чёрная Пантера" + ключевые слова выделены мной и Машей в гуглдоке](https://docs.google.com/document/d/1j5p2sc8HoWWiSpwcUqXYE2kylt7paMbPTUtc8Y06p9Y/edit?usp=sharing)
- [x] таблица по ключевым словам

Ключевые слова|Инга|Маша|RAKE
--------------|----|----|----
Black panther|+|+|+(выделяет в составе нескольких триграмм)
To try to say something|-|+|-
A controlled political stance|+|-|+
Uncertainty of our own world|+|-|-
Superhero movie machine|+|+|-
Marvel movies|+|+|-
Distinct voice of writer-director Ryan Coogler|+|-|-
Isolationist policy|+|-|-
Country of Wakanda|-|+|-
Conceals its power|-|+|-
Reexamine this policy|-|+|-
Erik “Killmonger” Stevens|+|+|-
Wakanda|+|-|-
Demonstrates an ethical complexity|+|-|-
Put up an invisible shield|+|-|-
An invisible shield|+|+|-
But, there is a cost|-|+|-
A historic four-day box office gross|-|+|-
Marvel’s first venture into serious social commentary|-|+|-
reflect the anxiety of the audience|+|+|-
civil liberties issues|+|-|-
drone strikes|+|-|-
the president’s kill list|+|-|-
preemptive technology|+|-|-


#### Процент совпадения: 
- [x] [результат выдачи оригинального RAKE](./old_RAKE.txt)
- [x] [результат выдачи улучшенного RAKE](./panther_keywords.txt)

#### Топ-15:
1. controlled political stance, 9.0
2. 20th century fox, 9.0
3. sharp political edges, 9.0
4. harm mass consumption, 9.0
5. brooke obie observes, 9.0
6. stifling studio system, 9.0
7. iron man began, 9.0
8. great political thrillers, 9.0
9. invisible man living, 8.5
10. nick fury debate, 8.5
11. black panther arrived, 8.333333333333332
12. black panther arrives, 8.333333333333332
13. black panther demonstrates, 8.333333333333332
14. black panther doesn, 8.333333333333332
15. clanging marvel gears, 8.0

11-14 могли бы быть объединены в одно ключевое слово: black panther
В остальном, RAKE достаточно неплохо выделил ключеные слова, однако совпадений с выделенными нами словами почти не было (только black panther и a controlled political stance).

#### Ошибочно выделенные слова (на наш взгляд): 

- [x] [улучшенный код RAKE](./rake.py)

#### Что было улучшено?
 - улучшен preprocessing (были убраны кавычки, тире и лишние знаки препинания)
 - добавлена лемматизация (Mystem)
 - максимальная длина для ключевого слова — 3 вместо 5
 - минимальная частота конструкции повышена до 3
 - стоп-лист попробовала расширить списком из nltk —> не очень эффективно
 
- [] [запуск RAKE на русском тексте]
