### HW RAKE
#### Совместно с Машей Бибаевой
- [x] текст про фильм "Чёрная Пантера"
- [x] [ключевые слова выделены мной и Машей в гуглдоке + топ слова](https://github.com/kartozia/nlp_Kartozia/blob/master/4th/RAKE/panther_keywords.txt)

#### Процент совпадения: 

- [x] [результат выдачи RAKE](./panther_keywords.txt)

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
В остальном, RAKE достаточно неплохо выделил ключеные слова

#### Ошибочно выделенные слова (на наш взгляд): 

- [x] [улучшенный код RAKE](./rake.py)

#### Что было улучшено?
 - улучшен preprocessing (были убраны кавычки, тире и лишние знаки препинания)
 - добавлена лемматизация (Mystem)
 - максимальная длина для ключевого слова — 3 вместо 5
 - минимальная частота конструкции повышена до 3
 - стоп-лист попробовала расширить списком из nltk —> не очень эффективно
 
- [] [запуск RAKE на русском тексте]
