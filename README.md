# Analyzer with ANTLR4

Минимальный **интерпретатор** учебного языка на Python с использованием **ANTLR 4**: лексический и синтаксический анализ заданы грамматикой, обход дерева разбора — паттерном Visitor.

## Язык

- **Программа** — один оператор до конца ввода.
- **Операторы:** `if (условие) оператор`, `if (условие) оператор else оператор`, `print(выражение);`
- **Условия:** `<` и `==` между двумя выражениями.
- **Выражения:** целые числа (`INT`).

Пробелы, табы и переводы строк игнорируются.

## Структура проекта

| Файл | Назначение |
|------|------------|
| `myLanguage.g4` | Грамматика (лексер + парсер). Единственный источник истины для синтаксиса. |
| `main.py` | Точка входа: разбор строки, построение дерева, интерпретация через `MyTreeVisitor`. |
| `MyLanguageLexer.py`, `myLanguageParser.py`, `myLanguageVisitor.py` | Сгенерированы ANTLR 4.13.2 из `myLanguage.g4`. |
| `.antlr/` | Артефакты генерации (в т.ч. Java). |

## Зависимости

- **Python 3** с установленным пакетом **antlr4**:
  ```bash
  pip install antlr4-python3-runtime
  ```

## Запуск

```bash
python main.py
```

В примере выполняется программа  
`if (1 < 2) if (3 == 4) print(0); else print(9);`  
— условие `1 < 2` истинно, `3 == 4` ложно, поэтому выводится **else**-ветка: `OUTPUT: 9`.

## Регенерация парсера

Если меняется `myLanguage.g4`, заново сгенерировать лексер/парсер/визитор для Python:

```bash
antlr4 -Dlanguage=Python3 -visitor -no-listener myLanguage.g4
```

Требуется [ANTLR 4 tool](https://www.antlr.org/download.html) (JAR или `antlr4` в PATH). Сгенерированные файлы перезапишут текущие `*Lexer.py`, `*Parser.py`, `*Visitor.py`.

## Идея реализации

Цепочка **InputStream → Lexer → CommonTokenStream → Parser** даёт дерево разбора для правила `program`. Класс `MyTreeVisitor` наследует сгенерированный `myLanguageVisitor` и переопределяет методы визита для нужных контекстов (`visitPrintStat`, `visitIfStat`, `visitIfElseStat`, `visitLessCond`, `visitEqualCond`, `visitIntExpr`), реализуя интерпретацию: вычисление условий и вывод значений через `print`.
