# 👨‍💻 Для разработчиков

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![JSON](https://img.shields.io/badge/JSON-карты-000000.svg?style=for-the-badge&labelColor=black)
![Threading](https://img.shields.io/badge/многопоточность-да-success.svg?style=for-the-badge&labelColor=black)

**Полная техническая документация проекта Console Snake**

</div>

---

## 📋 Содержание

<details>
<summary><b>🇷🇺 Русская версия</b></summary>

<br>

- [📁 Структура проекта](#-структура-проекта)
- [🔧 Полное описание функций snake.py](#-полное-описание-функций-snakepy)
- [🔍 Детальный разбор ключевых функций](#-детальный-разбор-ключевых-функций)
  - [clear() — адаптивная очистка экрана](#clear--адаптивная-очистка-экрана)
  - [keyByValue() — поиск ключа по значению](#keybyvalue--поиск-ключа-по-значению)
  - [draw() — отрисовка игрового поля](#draw--отрисовка-игрового-поля)
  - [out() — телепортация](#out--телепортация)
  - [free() — поиск свободных клеток для еды](#free--поиск-свободных-клеток-для-еды)
  - [calculate() — сердце игры](#calculate--сердце-игры)
- [🗺 Система карт](#-система-карт)
  - [Формат data.json](#-формат-datajson)
  - [Поля карты](#-поля-карты)
  - [Начальное положение змейки](#-начальное-положение-змейки)
  - [Пример карты](#-пример-карты)
- [📁 Папка maps](#-папка-maps)
  - [Как использовать карты из папки maps](#-как-использовать-карты-из-папки-maps)
  - [Создание своей карты](#-создание-своей-карты)
- [⚙️ Файл user.json](#-файл-userjson)
- [🚀 Планы по развитию](#-планы-по-развитию)
- [🐛 Известные баги](#-известные-баги)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [📁 Project Structure](#-project-structure)
- [🔧 Complete snake.py Functions Description](#-complete-snakepy-functions-description)
- [🔍 Detailed Analysis of Key Functions](#-detailed-analysis-of-key-functions)
  - [clear() — adaptive screen clearing](#clear--adaptive-screen-clearing)
  - [keyByValue() — find key by value](#keybyvalue--find-key-by-value)
  - [draw() — game field rendering](#draw--game-field-rendering)
  - [out() — teleportation](#out--teleportation)
  - [free() — find free cells for food](#free--find-free-cells-for-food)
  - [calculate() — the heart of the game](#calculate--the-heart-of-the-game)
- [🗺 Map System](#-map-system)
  - [data.json Format](#-datajson-format)
  - [Map Fields](#-map-fields)
  - [Snake Starting Position](#-snake-starting-position)
  - [Map Example](#-map-example)
- [📁 Maps Folder](#-maps-folder)
  - [How to Use Maps from the maps Folder](#-how-to-use-maps-from-the-maps-folder)
  - [Creating Your Own Map](#-creating-your-own-map)
- [⚙️ user.json File](#-userjson-file)
- [🚀 Development Plans](#-development-plans)
- [🐛 Known Bugs](#-known-bugs)

</details>

---

## 📁 Структура проекта

```
📦 Console-Snake
├── 📄 snake.py                          # Основной файл игры
├── 📄 data.json                         # Активная карта (загружается в игру)
├── 📄 user.json                         # Конфигурация пользователя
├── 📁 maps/                              # Папка с примерами карт
│   ├── 📄 default.json                    # Стандартная карта
│   └── 📄 example.json                     # Пример карты для ознакомления
├── 📄 README.md                          # Документация для пользователей
├── 📄 DEVELOPER.md                       # Документация для разработчиков
└── 📄 LICENSE                            # Лицензия GPLv3
```

**Назначение файлов:**

| Файл | Назначение |
|------|------------|
| `snake.py` | Весь код игры |
| `data.json` | Карта, которую загружает игра |
| `user.json` | Настройки пользователя (режим очистки экрана) |
| `maps/` | Папка с примерами карт |
| `README.md` | Документация для пользователей |
| `DEVELOPER.md` | Документация для разработчиков |

---

## 🔧 Полное описание функций snake.py

| Функция | Назначение | Параметры | Возвращаемое значение | Описание |
|---------|------------|-----------|----------------------|----------|
| `clear()` | Очищает экран | Нет | `None` | Читает `user.json`, если `enviroment: "console"` — вызывает `os.system('cls'/'clear')`, иначе печатает 100 пустых строк |
| `keyByValue(dct, value)` | Поиск ключа по значению | `dct`: словарь, `value`: значение | `key` или `None` | Ищет ключ, соответствующий переданному значению |
| `w_move()` | Обработчик клавиши W | Нет | `None` | Вызывает `calculate("w")` |
| `a_move()` | Обработчик клавиши A | Нет | `None` | Вызывает `calculate("a")` |
| `s_move()` | Обработчик клавиши S | Нет | `None` | Вызывает `calculate("s")` |
| `d_move()` | Обработчик клавиши D | Нет | `None` | Вызывает `calculate("d")` |
| `close()` | Завершает игру | Нет | `None` | Печатает "Good luck!", отключает все хоткеи и завершает процесс |
| `lst2str(lst)` | Преобразует список строк в одну строку | `lst`: список строк | `string` | Склеивает элементы списка через перенос строки, убирает последний `\n` |
| `dict2str(dct)` | Преобразует словарь строк в одну строку | `dct`: словарь с индексами 0..n | `string` | Проходит по ключам по порядку, склеивает значения через `\n` |
| `draw(positions_dict)` | Отрисовывает игровое поле | `positions_dict`: словарь с координатами змейки | `None` | Проходит по всем клеткам, рисует змейку красным, еду зелёным, поле — цветом из карты |
| `out(position)` | Обрабатывает выход за границы поля | `position`: список [x, y] | `position` | Если координаты выходят за пределы — телепортирует на противоположную сторону |
| `free(positions_dict, head)` | Находит свободные клетки | `positions_dict`: координаты змейки, `head`: координаты головы | `free`: список свободных клеток | Ищет клетки, не занятые змейкой, не стены и не рядом с головой |
| `calculate(command)` | Основная функция движения | `command`: "w", "a", "s", "d" | `None` | Вычисляет новую позицию, проверяет столкновения, обрабатывает еду, вызывает `clear()` и `draw()` |

---

## 🔍 Детальный разбор ключевых функций

### `clear()` — адаптивная очистка экрана

```python
def clear():
    with codecs.open("user.json", "r", "utf_8_sig") as f:
        user = json.load(f)
        if user["enviroment"] == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n" * 100)
```

**Как работает:**
1. Открывает `user.json` с поддержкой UTF-8 BOM (важно для файлов, сохранённых в некоторых редакторах)
2. Загружает JSON и читает поле `enviroment`
3. Если значение `"console"`:
   - На Windows вызывает `os.system('cls')`
   - На Linux/macOS вызывает `os.system('clear')`
4. Если любое другое значение (например, `"special"`):
   - Печатает 100 пустых строк (имитация очистки для IDE)

**Зачем это нужно:** В разных средах (консоль, PyCharm, онлайн-редакторы) очистка экрана работает по-разному. Эта функция обеспечивает корректную очистку в любой среде.

---

### `keyByValue()` — поиск ключа по значению

```python
def keyByValue(dct, value):
    for key in dct.keys():
        if dct[key] == value:
            return key
```

**Как работает:**
- Проходит по всем ключам словаря
- Сравнивает значение по ключу с искомым
- Возвращает первый подходящий ключ

**Зачем нужна:** Используется в `draw()` для проверки, является ли клетка головой змейки (ключ -1 не отрисовывается). Без этой функции нельзя было бы отличить голову от тела, так как они выглядят одинаково.

---

### `draw()` — отрисовка игрового поля

```python
def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(YSIZE):
        line = ""
        for x in range(XSIZE):
            find = False
            for position in positions:
                key = keyByValue(positions_dict, position)
                if position == [x, y] and key != -1:
                    line += "\033[38;2;255;0;0m██\033[m"  # красная змейка
                    find = True
            if find is False:
                global apple
                if [x, y] == apple:
                    line += "\033[38;2;0;255;0m██\033[m"  # зелёная еда
                else:
                    color = map["structure"][f"{x}:{y}"]["color"]
                    line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"  # поле из карты
        lines[y] = line
    print(dict2str(lines))
```

**Как работает:**
1. Проходит по всем Y (от 0 до YSIZE-1)
2. Для каждого Y проходит по всем X (от 0 до XSIZE-1)
3. Проверяет, есть ли в этой клетке сегмент змейки (исключая ключ -1)
4. Если есть — добавляет красный блок `██` с ANSI-кодом цвета
5. Если нет — проверяет, не яблоко ли это
6. Если яблоко — добавляет зелёный блок `██`
7. Иначе берёт из карты (`map["structure"][f"{x}:{y}"]["color"]`) RGB-цвет и добавляет блок `░░` с этим цветом
8. Сохраняет строку в словарь `lines`
9. Вызывает `dict2str(lines)` для преобразования в одну строку и печатает

**Важно:**
- Ключ `-1` в словаре `positions` — технический элемент, он не отрисовывается
- Цвет поля полностью определяется картой
- Яблоко имеет фиксированный зелёный цвет

---

### `out()` — телепортация

```python
def out(position):
    if XSIZE > position[0] > -1 and YSIZE > position[1] > -1:
        return position
    if position[0] == -1:
        position[0] = XSIZE - 1
    elif position[0] == XSIZE:
        position[0] = 0
    if position[1] == -1:
        position[1] = YSIZE - 1
    elif position[1] == YSIZE:
        position[1] = 0
    return position
```

**Как работает:**
1. Проверяет, находится ли точка внутри поля
2. Если да — возвращает её без изменений
3. Если нет — обрабатывает каждый случай:
   - `x == -1` (ушла влево) → `x = XSIZE - 1` (появляется справа)
   - `x == XSIZE` (ушла вправо) → `x = 0` (появляется слева)
   - `y == -1` (ушла вверх) → `y = YSIZE - 1` (появляется снизу)
   - `y == YSIZE` (ушла вниз) → `y = 0` (появляется сверху)
4. Возвращает скорректированные координаты

**Создаваемый эффект:** Игровое поле замкнуто в тор (пончик) — классическая механика из старых аркад, где нет стен, а есть бесконечное пространство.

---

### `free()` — поиск свободных клеток для еды

```python
def free(positions_dict, head):
    positions = list(positions_dict.values())
    free = []
    near = [out([head[0] + 1, head[1]]), out([head[0] - 1, head[1]]), 
            out([head[0], head[1] + 1]), out([head[0], head[1] - 1])]
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions and map["structure"][f"{x}:{y}"]["empty"] == True and [x, y] not in near:
                free.append([x, y])
    return free
```

**Как работает:**
1. Получает список всех занятых клеток (тело змейки)
2. Вычисляет клетки рядом с головой (чтобы еда не появлялась прямо перед носом) с учётом телепортации
3. Двойным циклом проходит по всем клеткам поля
4. Добавляет клетку в список, если:
   - Она не занята змейкой
   - Это не стена (`empty: true`)
   - Она не рядом с головой
5. Возвращает список свободных клеток

**Зачем нужна:** Чтобы размещать еду только в допустимых местах. Исключение клеток рядом с головой предотвращает появление еды, которую невозможно съесть без манёвра.

---

### `calculate()` — сердце игры

```python
def calculate(command):
    global positions
    global hotkey_pressed
    global score
    global apple
    hotkey_pressed.set()
    hotkey_pressed = threading.Event()
    new_positions = {}
    nums = sorted(positions.keys())
    mx = max(nums)
    
    # Вычисление новой позиции головы
    if command == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)  # телепортация если нужно

    # Проверка на стену
    if map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
        print("You died :(")
        close()

    # Проверка на столкновение с телом
    for num in nums:
        if positions[num] == upgr_last:
            print("You died :(")
            close()

    # Обработка еды
    if upgr_last == apple:
        score += 1
        apple = []
        new_positions[mx + 1] = upgr_last  # добавляем новый сегмент
        for num in nums:
            if num == mx:
                continue
            new_positions[num + 1] = positions[num + 1]
        new_positions[-1] = positions[-1]  # сохраняем технический ключ
    else:
        # Обычное движение
        new_positions[mx] = upgr_last
        for num in nums:
            if num == mx:
                continue
            new_positions[num] = positions[num + 1]

    clear()  # очистка экрана
    
    # Создание нового яблока если съели
    if apple == []:
        free_ = free(new_positions, upgr_last)
        if free_:  # проверка, что есть свободные клетки
            apple = choice(free_)
    
    draw(new_positions)  # отрисовка
    
    print("Play time:", round(time() - play_time, 2), "seconds")
    print("Score:", score)
    positions = new_positions  # обновление глобальной переменной
```

**Как работает:**
1. Сигнализирует о нажатии клавиши через `hotkey_pressed.set()`
2. Создаёт новое событие для следующего хода
3. Определяет индекс головы (максимальный ключ в словаре `positions`)
4. Вычисляет новую позицию головы в зависимости от команды
5. Применяет телепортацию через `out()`
6. Проверяет, не является ли новая клетка стеной — если да, смерть
7. Проверяет, не врезалась ли голова в тело — если да, смерть
8. Проверяет, не съела ли змейка яблоко:
   - Если съела: увеличивает счёт, добавляет новый сегмент, сохраняет технический ключ -1
   - Если нет: обычное движение (хвост сдвигается)
9. Очищает экран через `clear()`
10. Если яблоко съедено — создаёт новое в случайной свободной клетке
11. Отрисовывает поле через `draw()`
12. Печатает время игры и счёт
13. Обновляет глобальную переменную `positions`

**Особенности:**
- Ключ `-1` в словаре `positions` — технический элемент, используется как маркер
- Змейка хранится как `{индекс: [x, y]}`, где больший индекс — голова
- При поедании яблока добавляется новый сегмент перед головой (индекс mx+1)
- Технический ключ -1 всегда копируется в новый словарь

---

## 🗺 Система карт

Игра использует файл `data.json` для хранения активной карты. В папке `maps/` находятся примеры карт в отдельных файлах.

### 📄 Формат data.json

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "start": { "-1": [1, 6], "0": [2, 6] },
      "structure": {
        "0:0": { "empty": true, "color": [255, 255, 0] },
        "0:1": { "empty": true, "color": [255, 255, 0] },
        ...
        "14:12": { "empty": true, "color": [255, 255, 0] }
      }
    }
  }
}
```

### 📋 Поля карты

| Поле | Тип | Описание | Пример |
|------|-----|----------|--------|
| `name` | string | Название уровня | `"Default map"` |
| `description` | string | Описание уровня | `"обычная карта"` |
| `author` | string | Создатель карты | `"@su57ks"` |
| `size` | array | Размеры [x, y] | `[15, 13]` |
| `start` | object | Начальное положение змейки | `{ "-1": [1, 6], "0": [2, 6] }` |
| `structure` | object | Объект клеток с ключами `"x:y"` | см. ниже |
| `empty` | bool | `true` — проходимо, `false` — стена | `true` |
| `color` | array | RGB-цвет [r, g, b] для отрисовки клетки | `[255, 255, 0]` |

### 🐍 Начальное положение змейки

Поле `start` определяет начальное положение змейки. Ключи — это индексы сегментов, значения — координаты [x, y].

```json
"start": { 
  "-1": [1, 6],   # технический ключ (не отрисовывается)
  "0": [2, 6],    # первый сегмент (хвост)
  "1": [3, 6],    # второй сегмент
  "2": [4, 6],    # третий сегмент
  "3": [5, 6]     # четвёртый сегмент (голова)
}
```

**Правила:**
- Ключи должны быть целыми числами (в JSON они записываются как строки)
- Ключ `-1` обязателен — это технический элемент
- Ключи должны идти по порядку: -1, 0, 1, 2, 3...
- Больший индекс = голова

### 🌟 Пример карты

```json
{
  "name": "Maze",
  "description": "лабиринт с препятствиями",
  "author": "Player",
  "size": [10, 10],
  "start": { "-1": [1, 1], "0": [2, 1], "1": [3, 1] },
  "structure": {
    "0:0": { "empty": false, "color": [100, 100, 100] },
    "1:0": { "empty": false, "color": [100, 100, 100] },
    "2:0": { "empty": false, "color": [100, 100, 100] },
    "3:0": { "empty": true, "color": [200, 200, 0] },
    "4:0": { "empty": true, "color": [200, 200, 0] },
    ...
  }
}
```

---

## 📁 Папка maps

Папка `maps/` содержит примеры карт в отдельных JSON-файлах.

**Содержимое папки:**
- `default.json` — стандартная карта (жёлтое поле, размер 15×13)
- `example.json` — пример карты для ознакомления с форматом (размер 3×1)

### 📌 Как использовать карты из папки maps

Чтобы использовать карту из папки `maps/`, нужно скопировать её содержимое в файл `data.json`:

```bash
# Например, использовать стандартную карту
cp maps/default.json data.json

# Затем запустить игру
python snake.py
```

### 🛠️ Создание своей карты

1. Создайте новый JSON-файл в папке `maps/`, например `my_map.json`
2. Используйте `example.json` как шаблон
3. Заполните структуру:

```json
{
  "name": "My Map",
  "description": "моя первая карта",
  "author": "Ваше имя",
  "size": [15, 13],
  "start": { "-1": [1, 6], "0": [2, 6] },
  "structure": {}
}
```

4. Сгенерируйте структуру для всех клеток. Для поля 15×13 нужно 195 записей. Можно сгенерировать программно:

```python
size_x, size_y = 15, 13
structure = {}
for y in range(size_y):
    for x in range(size_x):
        key = f"{x}:{y}"
        structure[key] = {
            "empty": True,
            "color": [255, 255, 0]  # жёлтый цвет по умолчанию
        }
# затем сохранить в JSON
```

5. Измените цвета и `empty` для нужных клеток
6. Скопируйте готовый файл в `data.json` и тестируйте

---

## ⚙️ Файл user.json

**Назначение:** Настройки пользователя, влияющие на поведение игры.

```json
{"enviroment": "special"}
```

**Возможные значения:**

| Значение | Эффект | Когда использовать |
|----------|--------|-------------------|
| `"console"` | Системная очистка (`cls`/`clear`) | При запуске в настоящем терминале |
| `"special"` | Очистка через 100 пустых строк | При запуске в IDE (PyCharm, VS Code) или онлайн-средах |

**Как выбрать:**
- Если при запуске игра оставляет видимый мусор или некорректно очищает экран — попробуйте сменить значение
- По умолчанию стоит `"special"`, так как это работает везде

---

## 🚀 Планы по развитию

- [ ] Сохранение рекордов — запись лучших результатов в файл
- [ ] Увеличение скорости — постепенное ускорение с ростом счёта
- [ ] Выбор карты при запуске — возможность указать файл карты через аргумент командной строки
- [ ] Несколько типов еды — яблоки, вишни, бананы с разными эффектами
- [ ] Режим "Классические стены" — вместо телепортации
- [ ] Цветовые схемы — настройка цветов змейки и еды через `user.json`
- [ ] Звуковые эффекты — через терминал (beep)

---

## 🐛 Известные баги

| Баг | Описание | Статус |
|-----|----------|--------|
| Пропуск хода | При очень быстром нажатии клавиш может пропустить один ход | Исследуется |
| Цвета в старых терминалах | На некоторых старых терминалах цвета отображаются некорректно | Низкий приоритет |
| Смерть без столкновения | Иногда змейка умирает без видимой причины | Требуется воспроизведение |

---

<div align="center">

**✍️ Написано человеком, без использования ИИ**

*Если вы нашли баг или хотите предложить улучшение — создайте Issue на GitHub!*

[⬆ Наверх](#-для-разработчиков)

</div>

---

# 👨‍💻 For Developers

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![JSON](https://img.shields.io/badge/JSON-maps-000000.svg?style=for-the-badge&labelColor=black)
![Threading](https://img.shields.io/badge/multithreading-yes-success.svg?style=for-the-badge&labelColor=black)

**Complete technical documentation of the Console Snake project**

</div>

---

## 📋 Contents

- [📁 Project Structure](#-project-structure)
- [🔧 Complete snake.py Functions Description](#-complete-snakepy-functions-description)
- [🔍 Detailed Analysis of Key Functions](#-detailed-analysis-of-key-functions)
  - [clear() — adaptive screen clearing](#clear--adaptive-screen-clearing)
  - [keyByValue() — find key by value](#keybyvalue--find-key-by-value)
  - [draw() — game field rendering](#draw--game-field-rendering)
  - [out() — teleportation](#out--teleportation)
  - [free() — find free cells for food](#free--find-free-cells-for-food)
  - [calculate() — the heart of the game](#calculate--the-heart-of-the-game)
- [🗺 Map System](#-map-system)
  - [data.json Format](#-datajson-format)
  - [Map Fields](#-map-fields)
  - [Snake Starting Position](#-snake-starting-position)
  - [Map Example](#-map-example)
- [📁 Maps Folder](#-maps-folder)
  - [How to Use Maps from the maps Folder](#-how-to-use-maps-from-the-maps-folder)
  - [Creating Your Own Map](#-creating-your-own-map)
- [⚙️ user.json File](#-userjson-file)
- [🚀 Development Plans](#-development-plans)
- [🐛 Known Bugs](#-known-bugs)

---

## 📁 Project Structure

```
📦 Console-Snake
├── 📄 snake.py                          # Main game file
├── 📄 data.json                         # Active map (loaded into the game)
├── 📄 user.json                         # User configuration
├── 📁 maps/                              # Folder with map examples
│   ├── 📄 default.json                    # Standard map
│   └── 📄 example.json                     # Example map for reference
├── 📄 README.md                          # User documentation
├── 📄 DEVELOPER.md                       # Developer documentation
└── 📄 LICENSE                            # GPLv3 License
```

**File purposes:**

| File | Purpose |
|------|---------|
| `snake.py` | All game code |
| `data.json` | Map loaded by the game |
| `user.json` | User settings (screen clearing mode) |
| `maps/` | Folder with map examples |
| `README.md` | User documentation |
| `DEVELOPER.md` | Developer documentation |

---

## 🔧 Complete snake.py Functions Description

| Function | Purpose | Parameters | Return Value | Description |
|---------|------------|-----------|----------------------|-------------|
| `clear()` | Clears screen | None | `None` | Reads `user.json`, if `enviroment: "console"` — calls `os.system('cls'/'clear')`, otherwise prints 100 empty lines |
| `keyByValue(dct, value)` | Find key by value | `dct`: dictionary, `value`: value | `key` or `None` | Finds key matching the given value |
| `w_move()` | W key handler | None | `None` | Calls `calculate("w")` |
| `a_move()` | A key handler | None | `None` | Calls `calculate("a")` |
| `s_move()` | S key handler | None | `None` | Calls `calculate("s")` |
| `d_move()` | D key handler | None | `None` | Calls `calculate("d")` |
| `close()` | Exits the game | None | `None` | Prints "Good luck!", unhooks all hotkeys and terminates process |
| `lst2str(lst)` | Converts list of strings to one string | `lst`: list of strings | `string` | Joins list elements with newlines, removes last `\n` |
| `dict2str(dct)` | Converts dictionary of strings to one string | `dct`: dictionary with indices 0..n | `string` | Iterates through keys in order, joins values with `\n` |
| `draw(positions_dict)` | Draws game field | `positions_dict`: dictionary with snake coordinates | `None` | Iterates through all cells, draws snake in red, food in green, field in colors from map |
| `out(position)` | Handles boundary exit | `position`: list [x, y] | `position` | If coordinates are out of bounds — teleports to opposite side |
| `free(positions_dict, head)` | Finds free cells | `positions_dict`: snake coordinates, `head`: head coordinates | `free`: list of free cells | Finds cells not occupied by snake, not walls, and not near head |
| `calculate(command)` | Main movement function | `command`: "w", "a", "s", "d" | `None` | Calculates new position, checks collisions, handles food, calls `clear()` and `draw()` |

---

## 🔍 Detailed Analysis of Key Functions

### `clear()` — adaptive screen clearing

```python
def clear():
    with codecs.open("user.json", "r", "utf_8_sig") as f:
        user = json.load(f)
        if user["enviroment"] == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n" * 100)
```

**How it works:**
1. Opens `user.json` with UTF-8 BOM support (important for files saved in some editors)
2. Loads JSON and reads the `enviroment` field
3. If value is `"console"`:
   - On Windows calls `os.system('cls')`
   - On Linux/macOS calls `os.system('clear')`
4. If any other value (e.g., `"special"`):
   - Prints 100 empty lines (simulating clear for IDEs)

**Why this is needed:** Different environments (console, PyCharm, online editors) handle screen clearing differently. This function ensures correct clearing in any environment.

---

### `keyByValue()` — find key by value

```python
def keyByValue(dct, value):
    for key in dct.keys():
        if dct[key] == value:
            return key
```

**How it works:**
- Iterates through all dictionary keys
- Compares value by key with the target
- Returns first matching key

**Why needed:** Used in `draw()` to check if a cell is the snake's head (key -1 is not rendered). Without this function, you couldn't distinguish head from body as they look the same.

---

### `draw()` — game field rendering

```python
def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(YSIZE):
        line = ""
        for x in range(XSIZE):
            find = False
            for position in positions:
                key = keyByValue(positions_dict, position)
                if position == [x, y] and key != -1:
                    line += "\033[38;2;255;0;0m██\033[m"  # red snake
                    find = True
            if find is False:
                global apple
                if [x, y] == apple:
                    line += "\033[38;2;0;255;0m██\033[m"  # green food
                else:
                    color = map["structure"][f"{x}:{y}"]["color"]
                    line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"  # field from map
        lines[y] = line
    print(dict2str(lines))
```

**How it works:**
1. Iterates through all Y (0 to YSIZE-1)
2. For each Y, iterates through all X (0 to XSIZE-1)
3. Checks if there's a snake segment in this cell (excluding key -1)
4. If yes — adds red `██` block with ANSI color code
5. If no — checks if it's an apple
6. If apple — adds green `██` block
7. Otherwise gets RGB color from map (`map["structure"][f"{x}:{y}"]["color"]`) and adds `░░` block with that color
8. Saves the line to the `lines` dictionary
9. Calls `dict2str(lines)` to convert to one string and prints

**Important:**
- Key `-1` in `positions` dictionary is a technical element, not rendered
- Field color is completely determined by the map
- Apple has a fixed green color

---

### `out()` — teleportation

```python
def out(position):
    if XSIZE > position[0] > -1 and YSIZE > position[1] > -1:
        return position
    if position[0] == -1:
        position[0] = XSIZE - 1
    elif position[0] == XSIZE:
        position[0] = 0
    if position[1] == -1:
        position[1] = YSIZE - 1
    elif position[1] == YSIZE:
        position[1] = 0
    return position
```

**How it works:**
1. Checks if the point is inside the field
2. If yes — returns it unchanged
3. If no — handles each case:
   - `x == -1` (left edge) → `x = XSIZE - 1` (appears on right)
   - `x == XSIZE` (right edge) → `x = 0` (appears on left)
   - `y == -1` (top edge) → `y = YSIZE - 1` (appears on bottom)
   - `y == YSIZE` (bottom edge) → `y = 0` (appears on top)
4. Returns corrected coordinates

**Effect created:** The game field is a torus (donut-shaped) — a classic mechanic from old arcade games where there are no walls, but infinite space.

---

### `free()` — find free cells for food

```python
def free(positions_dict, head):
    positions = list(positions_dict.values())
    free = []
    near = [out([head[0] + 1, head[1]]), out([head[0] - 1, head[1]]), 
            out([head[0], head[1] + 1]), out([head[0], head[1] - 1])]
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions and map["structure"][f"{x}:{y}"]["empty"] == True and [x, y] not in near:
                free.append([x, y])
    return free
```

**How it works:**
1. Gets list of all occupied cells (snake body)
2. Calculates cells near the head (so food doesn't appear right in front) considering teleportation
3. Double loop over all field cells
4. Adds cell to list if:
   - Not occupied by snake
   - Not a wall (`empty: true`)
   - Not near head
5. Returns list of free cells

**Why needed:** To place food only in valid locations. Excluding cells near the head prevents food from appearing where it's impossible to eat without maneuvering.

---

### `calculate()` — the heart of the game

```python
def calculate(command):
    global positions
    global hotkey_pressed
    global score
    global apple
    hotkey_pressed.set()
    hotkey_pressed = threading.Event()
    new_positions = {}
    nums = sorted(positions.keys())
    mx = max(nums)
    
    # Calculate new head position
    if command == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)  # teleport if needed

    # Wall check
    if map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
        print("You died :(")
        close()

    # Body collision check
    for num in nums:
        if positions[num] == upgr_last:
            print("You died :(")
            close()

    # Food handling
    if upgr_last == apple:
        score += 1
        apple = []
        new_positions[mx + 1] = upgr_last  # add new segment
        for num in nums:
            if num == mx:
                continue
            new_positions[num + 1] = positions[num + 1]
        new_positions[-1] = positions[-1]  # preserve technical key
    else:
        # Normal movement
        new_positions[mx] = upgr_last
        for num in nums:
            if num == mx:
                continue
            new_positions[num] = positions[num + 1]

    clear()  # clear screen
    
    # Create new apple if eaten
    if apple == []:
        free_ = free(new_positions, upgr_last)
        if free_:  # check if there are free cells
            apple = choice(free_)
    
    draw(new_positions)  # draw
    
    print("Play time:", round(time() - play_time, 2), "seconds")
    print("Score:", score)
    positions = new_positions  # update global variable
```

**How it works:**
1. Signals key press via `hotkey_pressed.set()`
2. Creates new event for next move
3. Determines head index (maximum key in `positions` dictionary)
4. Calculates new head position based on command
5. Applies teleportation via `out()`
6. Checks if new cell is a wall — if yes, death
7. Checks if head collided with body — if yes, death
8. Checks if snake ate an apple:
   - If ate: increases score, adds new segment, preserves technical key -1
   - If not: normal movement (tail shifts)
9. Clears screen via `clear()`
10. If apple was eaten — creates new one in random free cell
11. Draws field via `draw()`
12. Prints game time and score
13. Updates global `positions` variable

**Features:**
- Key `-1` in `positions` dictionary is a technical element used as a marker
- Snake stored as `{index: [x, y]}`, where higher index = head
- When eating an apple, a new segment is added before the head (index mx+1)
- Technical key -1 is always copied to the new dictionary

---

## 🗺 Map System

The game uses the `data.json` file to store the active map. The `maps/` folder contains map examples in separate files.

### 📄 data.json Format

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "start": { "-1": [1, 6], "0": [2, 6] },
      "structure": {
        "0:0": { "empty": true, "color": [255, 255, 0] },
        "0:1": { "empty": true, "color": [255, 255, 0] },
        ...
        "14:12": { "empty": true, "color": [255, 255, 0] }
      }
    }
  }
}
```

### 📋 Map Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `name` | string | Level name | `"Default map"` |
| `description` | string | Level description | `"обычная карта"` |
| `author` | string | Map creator | `"@su57ks"` |
| `size` | array | Dimensions [x, y] | `[15, 13]` |
| `start` | object | Snake starting position | `{ "-1": [1, 6], "0": [2, 6] }` |
| `structure` | object | Cell object with `"x:y"` keys | see below |
| `empty` | bool | `true` — passable, `false` — wall | `true` |
| `color` | array | RGB color [r, g, b] for rendering | `[255, 255, 0]` |

### 🐍 Snake Starting Position

The `start` field defines the initial snake position. Keys are segment indices, values are [x, y] coordinates.

```json
"start": { 
  "-1": [1, 6],   # technical key (not rendered)
  "0": [2, 6],    # first segment (tail)
  "1": [3, 6],    # second segment
  "2": [4, 6],    # third segment
  "3": [5, 6]     # fourth segment (head)
}
```

**Rules:**
- Keys must be integers (in JSON they are written as strings)
- Key `-1` is required — it's a technical element
- Keys must be sequential: -1, 0, 1, 2, 3...
- Higher index = head

### 🌟 Map Example

```json
{
  "name": "Maze",
  "description": "maze with obstacles",
  "author": "Player",
  "size": [10, 10],
  "start": { "-1": [1, 1], "0": [2, 1], "1": [3, 1] },
  "structure": {
    "0:0": { "empty": false, "color": [100, 100, 100] },
    "1:0": { "empty": false, "color": [100, 100, 100] },
    "2:0": { "empty": false, "color": [100, 100, 100] },
    "3:0": { "empty": true, "color": [200, 200, 0] },
    "4:0": { "empty": true, "color": [200, 200, 0] },
    ...
  }
}
```

---

## 📁 Maps Folder

The `maps/` folder contains map examples in separate JSON files.

**Folder contents:**
- `default.json` — standard map (yellow field, size 15×13)
- `example.json` — example map for learning the format (size 3×1)

### 📌 How to Use Maps from the maps Folder

To use a map from the `maps/` folder, copy its contents to the `data.json` file:

```bash
# For example, use the standard map
cp maps/default.json data.json

# Then run the game
python snake.py
```

### 🛠️ Creating Your Own Map

1. Create a new JSON file in the `maps/` folder, e.g., `my_map.json`
2. Use `example.json` as a template
3. Fill in the structure:

```json
{
  "name": "My Map",
  "description": "my first map",
  "author": "Your Name",
  "size": [15, 13],
  "start": { "-1": [1, 6], "0": [2, 6] },
  "structure": {}
}
```

4. Generate structure for all cells. For a 15×13 field, you need 195 entries. You can generate them programmatically:

```python
size_x, size_y = 15, 13
structure = {}
for y in range(size_y):
    for x in range(size_x):
        key = f"{x}:{y}"
        structure[key] = {
            "empty": True,
            "color": [255, 255, 0]  # default yellow color
        }
# then save to JSON
```

5. Change colors and `empty` for desired cells
6. Copy the finished file to `data.json` and test

---

## ⚙️ user.json File

**Purpose:** User settings affecting game behavior.

```json
{"enviroment": "special"}
```

**Possible values:**

| Value | Effect | When to use |
|-------|--------|-------------|
| `"console"` | System clearing (`cls`/`clear`) | When running in a real terminal |
| `"special"` | Clearing via 100 empty lines | When running in IDEs (PyCharm, VS Code) or online environments |

**How to choose:**
- If the game leaves visible garbage or doesn't clear the screen correctly — try changing the value
- Default is `"special"` because it works everywhere

---

## 🚀 Development Plans

- [ ] High scores — save best results to file
- [ ] Speed increase — gradual acceleration as score grows
- [ ] Map selection at startup — ability to specify map file via command line argument
- [ ] Multiple food types — apples, cherries, bananas with different effects
- [ ] "Classic Walls" mode — instead of teleportation
- [ ] Color schemes — customize snake and food colors via `user.json`
- [ ] Sound effects — via terminal (beep)

---

## 🐛 Known Bugs

| Bug | Description | Status |
|-----|-------------|--------|
| Missed move | Very fast key presses may skip a move | Investigating |
| Colors in old terminals | Colors display incorrectly on some old terminals | Low priority |
| Death without collision | Sometimes the snake dies for no apparent reason | Needs reproduction |

---

<div align="center">

**✍️ Written by human, without AI**

*If you found a bug or want to suggest an improvement — create an Issue on GitHub!*

[⬆ Back to top](#-for-developers)

</div>
