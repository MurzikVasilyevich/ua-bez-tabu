# ua-bez-tabu
Документ створен на основі книги Лесі Ставицької [Українська мова без табу. Словник нецензурної лексики та її відповідників: Обсценізми, евфемізми, сексуалізми](https://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%BC%D0%BE%D0%B2%D0%B0_%D0%B1%D0%B5%D0%B7_%D1%82%D0%B0%D0%B1%D1%83).

# Шановні!
Будь ласка, не соромтесь [надавати](https://github.com/MurzikVasilyevich/ua-bez-tabu/issues/new/choose) свої пропозиції щодо:
- додавання термінів
- форматів, яких вам не вистачає:
  - JSON - вже в наявності [synonyms.json](/data/synonyms.json)
  - REST
  - XML - вже в наявності [synonyms.xml](/data/synonyms.xml)
- категоризації
- та ін.

# Про репозиторій
Основна інформація знаходиться у файлі [synonyms.csv](./synonyms.csv). Цей файл є першоджерелом.
Інформація у форматі JSON та XML знаходиться у теці [data](./data/).

# Чатбот
Посилання на бота: [Українська без табу](https://t.me/ua_bez_tabu_bot).
![image](https://user-images.githubusercontent.com/93987936/183085723-52b12bc2-2da3-448a-815f-5c8b46d553dc.png)

# Колонки файлу [synonyms.csv](./synonyms.csv)
- group - група термінів
- term - термін
- synonym - синонім до терміну
- isWord - слово (1) або словосполучення (0)


# ToDo
* [x] Зробити чатбот, що виводить синонім до терміну
* [x] Переробити файл у формат JSON
* [x] Додати XML
* [ ] Markdown
* [ ] Зробити бібліотеку Python
