# 🐍 Консольная Змейка / Console Snake

<div align="center">

![Version](https://img.shields.io/badge/версия-1.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-GPLv3-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Console](https://img.shields.io/badge/платформа-консоль-black.svg?style=for-the-badge&labelColor=black)
![Dependencies](https://img.shields.io/badge/зависимости-1-important.svg?style=for-the-badge&labelColor=black)

**✨ Классическая игра "Змейка" с цветным интерфейсом, телепортацией и пользовательскими картами ✨**

</div>

---

## 📋 Содержание

<details>
<summary><b>🇷🇺 Русская версия</b></summary>

<br>

- [🚀 Запуск проекта](#-запуск-проекта)
- [📝 Описание проекта](#-описание-проекта)
- [✨ Ключевые возможности](#-ключевые-возможности)
- [🎮 Геймплей и механики](#-геймплей-и-механики)
- [🗺 Система карт](#-система-карт)
- [📊 Достоинства и недостатки](#-достоинства-и-недостатки)
- [📁 Структура проекта](#-структура-проекта)
- [🛠 Технологии](#-технологии)
- [👨‍💻 Для разработчиков](#-для-разработчиков)
  - [Функции snake.py](#-функции-snakepy)
  - [Как добавить карту](#-как-добавить-карту)
  - [Планы по развитию](#-планы-по-развитию)
- [📜 Лицензия](#-лицензия)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [🚀 Project Launch](#-project-launch)
- [📝 Project Description](#-project-description)
- [✨ Key Features](#-key-features)
- [🎮 Gameplay & Mechanics](#-gameplay--mechanics)
- [🗺 Map System](#-map-system)
- [📊 Advantages and Disadvantages](#-advantages-and-disadvantages)
- [📁 Project Structure](#-project-structure)
- [🛠 Technologies](#-technologies)
- [👨‍💻 For Developers](#-for-developers)
  - [snake.py Functions](#-snakepy-functions)
  - [How to Add a Map](#-how-to-add-a-map)
  - [Development Plans](#-development-plans)
- [📜 License](#-license)

</details>

---

## 🇷🇺 Русская версия

### 🚀 Запуск проекта

#### Локальный запуск
```bash
# Клонируйте репозиторий
git clone https://github.com/su57ks/Console-Snake.git

# Перейдите в папку проекта
cd Console-Snake

# Установите зависимости
pip install keyboard

# Запустите игру
python snake.py
```

#### Требования
- Python 3.x
- Библиотека `keyboard` (для обработки нажатий клавиш)
- Терминал с поддержкой ANSI-цветов (все современные терминалы)

> **Важно:** На macOS и Linux для работы `keyboard` могут потребоваться права суперпользователя. Альтернативно можно использовать `sudo python snake.py`.

---

### 📝 Описание проекта
**Console Snake** — это классическая игра "Змейка", реализованная полностью в терминале. Особенность проекта — телепортация при выходе за границы поля вместо стандартных стен, цветное отображение и поддержка пользовательских карт в формате JSON.

Проект написан "руками" без использования сложных игровых движков — только чистый Python и минимум зависимостей.

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🎮 **Геймплей** | Управление WASD | Интуитивное управление с горячими клавишами |
| | Телепортация | При выходе за границы поля змейка появляется с противоположной стороны |
| | Таймер игры | Отображается время текущей сессии |
| 🎨 **Визуал** | Цветная графика | Змейка — красные блоки (`██`), поле — жёлтые (`░░`) |
| | Поддержка ANSI | 24-битные цвета в терминале |
| 🗺 **Карты** | JSON-формат | Простое создание и редактирование уровней |
| | RGB-цвета | Каждая клетка может иметь свой цвет |
| | Система препятствий | Возможность создавать непроходимые стены |
| ⚡ **Техническое** | Многопоточность | Отдельный поток для ожидания клавиш |
| | Минимум зависимостей | Всего 1 сторонняя библиотека |

---

### 🎮 Геймплей и механики

#### Управление
| Клавиша | Действие |
|---------|----------|
| `W` | Движение вверх |
| `A` | Движение влево |
| `S` | Движение вниз |
| `D` | Движение вправо |
| `Ctrl+C` | Выход из игры |

#### Правила
1. Змейка движется в выбранном направлении
2. При выходе за границу поля она появляется с противоположной стороны (телепортация)
3. Столкновение с собственным хвостом приводит к смерти
4. Время игры отображается после каждого хода

#### Отображение в терминале
```
Змейка (█):
\033[38;2;255;0;0m██\033[m — красные блоки

Поле (░):
\033[38;2;255;255;0m░░\033[m — жёлтые блоки
```

---

### 🗺 Система карт

#### Формат JSON
```json
{
  "name": "Example Map",
  "description": "Map description",
  "author": "Author Name",
  "size": [3, 1],
  "structure": [
    {
      "coords": [0, 0],
      "empty": true,
      "color": [240, 240, 240]
    },
    {
      "coords": [1, 0],
      "empty": false,
      "color": [100, 100, 100]
    }
  ]
}
```

#### Поля карты
| Поле | Тип | Описание |
|------|-----|----------|
| `name` | string | Название уровня |
| `description` | string | Описание уровня |
| `author` | string | Создатель карты |
| `size` | array | Размеры [x, y] |
| `structure` | array | Массив клеток |
| `coords` | array | Координаты [x, y] |
| `empty` | bool | `true` — проходимо, `false` — стена |
| `color` | array | RGB-цвет [r, g, b] |

> **Примечание:** Система карт находится в разработке и пока не интегрирована в основной геймплей.

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
| | |
|---|------|
| **👨‍💻 Написано человеком** | Весь код написан вручную, без использования готовых шаблонов и игровых движков — чувствуется живой подход |
| **📦 Мало зависимостей** | Всего 1 сторонняя библиотека (`keyboard`). Всё остальное — чистый Python |
| **🎨 Цветной интерфейс** | Полноцветный вывод в терминале с поддержкой 24-битных RGB-цветов |
| **🧩 Расширяемость** | Легко добавлять новые карты через JSON |
| **🔄 Телепортация** | Нестандартная механика вместо скучных стен |
| **⚡ Многопоточность** | Отзывчивое управление благодаря отдельному потоку для клавиш |

#### ❌ Недостатки
| | |
|---|------|
| **🖥 Консольный интерфейс** | Всё происходит в терминале — нет графического интерфейса, только символы |
| **🍎 Проблемы с permissions** | На macOS и Linux библиотека `keyboard` требует прав суперпользователя |
| **🍔 Отсутствует еда** | Механика сбора еды пока не реализована — змейка имеет фиксированную начальную длину |
| **🚫 Нет счёта** | Отсутствует система подсчёта очков и рекордов |
| **🐌 Нет ускорения** | Скорость движения постоянная, не увеличивается |
| **🗺 Карты не в игре** | JSON-карты существуют, но пока не влияют на геймплей |

---

### 📁 Структура проекта

```
📦 Console-Snake
├── 📄 snake.py                          # Основной файл игры
├── 📁 maps/                              # Папка с картами
│   └── 📄 example.json                    # Пример карты
├── 📄 README.md                          # Документация
└── 📄 LICENSE                            # Лицензия GPLv3
```

---

### 🛠 Технологии

| Технология | Применение |
|------------|------------|
| **Python 3** | Основная логика игры |
| **keyboard** | Глобальный перехват нажатий клавиш |
| **threading** | Асинхронное ожидание ввода |
| **ANSI escape codes** | Цветной вывод в терминал |
| **JSON** | Хранение и загрузка карт |

---

## 👨‍💻 Для разработчиков

### 🔧 Функции snake.py

| Функция | Назначение | Параметры | Возвращаемое значение |
|---------|------------|-----------|----------------------|
| `w_move()`, `a_move()`, `s_move()`, `d_move()` | Функции-обёртки для вызова `calculate()` с соответствующим направлением | Нет | `None` |
| `close()` | Завершает игру с сообщением "Good luck!" | Нет | `None` (завершает процесс) |
| `lst2str(lst)` | Преобразует список строк в одну строку с переносами | `lst`: список строк | `string`: объединённая строка |
| `dict2str(dct)` | Преобразует словарь строк в одну строку с переносами | `dct`: словарь с индексами 0..n | `string`: объединённая строка |
| `draw(positions_dict)` | Отрисовывает игровое поле | `positions_dict`: словарь с координатами змейки | `None` (выводит в консоль) |
| `out(position)` | Обрабатывает выход за границы поля (телепортация) | `position`: список [x, y] | `position`: скорректированные координаты |
| `free(positions_dict)` | Находит свободные клетки на поле | `positions_dict`: словарь с координатами змейки | `free`: список свободных клеток |
| `calculate(command)` | Основная функция движения и логики | `command`: строка "w", "a", "s", "d" | `None` (обновляет глобальные переменные) |

#### Детальный разбор ключевых функций

**calculate(command)** — сердце игры
```python
def calculate(command):
    global positions
    global hotkey_pressed
    hotkey_pressed.set()                    # Сигнал о нажатии клавиши
    hotkey_pressed = threading.Event()      # Сброс события
    new_positions = {}
    nums = sorted(positions.keys())          # [-1, 0, 1, 2, 3]
    mx = max(nums)                           # 3 (индекс головы)
    
    # Вычисление новой позиции головы в зависимости от направления
    if command == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)                    # Телепортация если нужно
    new_positions[mx] = upgr_last            # Новая голова

    # Проверка на столкновение и перемещение остальных сегментов
    for num in nums:
        if positions[num] == upgr_last:      # Если голова врезалась в тело
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]  # Сегмент двигается за предыдущим

    print("\n"*100)                          # Очистка экрана
    draw(new_positions)                       # Отрисовка
    print("Play time:", round(time() - play_time, 2), "seconds")
    positions = new_positions                  # Обновление глобальной переменной
```
**Что делает:**
- Получает команду движения
- Вычисляет новую позицию головы
- Применяет телепортацию через `out()`
- Проверяет столкновение с телом
- Перемещает все сегменты
- Перерисовывает поле
- Обновляет таймер

**Особенности:**
- Ключ `-1` в словаре `positions` — технический элемент для будущих механик
- Змейка хранится как `{индекс: [x, y]}`, где больший индекс — голова
- Телепортация применяется только к голове

---

**draw(positions_dict)** — отрисовка поля
```python
def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(YSIZE):
        line = ""
        for x in range(XSIZE):
            find = False
            for position in positions:
                if position[0] == x and position[1] == y:
                    line += "\033[38;2;255;0;0m██\033[m"  # Красная змейка
                    find = True
            if find is False:
                line += "\033[38;2;255;255;0m░░\033[m"    # Жёлтое поле
        lines[y] = line
    print(dict2str(lines))
```
**Что делает:**
- Проходит по всем клеткам поля
- Проверяет, есть ли в клетке сегмент змейки
- Если есть — рисует красный блок
- Если нет — рисует жёлтый блок
- Форматирует вывод через `dict2str()`

**Особенности:**
- Двойной цикл по Y и X
- Использует ANSI-коды для 24-битного цвета
- Каждый вызов полностью перерисовывает поле

---

**out(position)** — телепортация
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
**Что делает:**
- Проверяет, находится ли точка в пределах поля
- Если вышла за левый край — появляется справа
- Если вышла за правый край — появляется слева
- Если вышла за верхний край — появляется снизу
- Если вышла за нижний край — появляется сверху

**Особенности:**
- Создаёт эффект "тора" (игровое поле замкнуто в кольцо)
- Применяется только к голове змейки

---

**free(positions_dict)** — поиск свободных клеток
```python
def free(positions_dict):
    positions = list(positions_dict.values())
    print(positions)
    free = []
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions:
                free.append([x, y])
    return free
```
**Что делает:**
- Получает все занятые клетки
- Проходит по всему полю
- Если клетка не занята — добавляет в список свободных

**Особенности:**
- Функция заготовлена для будущей механики еды
- Сейчас только выводит занятые позиции в консоль

---

### 🗺 Как добавить карту

1. Создайте JSON-файл в папке `/maps`
2. Заполните структуру по примеру `example.json`:

```json
{
  "name": "Название карты",
  "description": "Описание",
  "author": "Ваше имя",
  "size": [ширина, высота],
  "structure": [
    {
      "coords": [x, y],
      "empty": true/false,
      "color": [r, g, b]
    }
  ]
}
```

3. Координаты должны быть в пределах `size`
4. `empty: false` создаёт непроходимую стену
5. Цвет задаётся в формате RGB (0-255)

> **Важно:** Интеграция карт в игру находится в разработке

---

### 🚀 Планы по развитию

- [ ] Добавить механику еды и роста змейки
- [ ] Интегрировать JSON-карты в геймплей
- [ ] Система подсчёта очков и рекордов
- [ ] Увеличение скорости с ростом змейки
- [ ] Загрузка случайной карты при старте
- [ ] Сохранение прогресса

---

### 📜 Лицензия

Проект распространяется под лицензией **GNU General Public License v3 (GPLv3)**.

**Основные положения:**
- ✅ Свободное использование и распространение
- ✅ Доступ к исходному коду
- ✅ Модификация и улучшение
- ❌ Закрытие исходного кода

Полный текст лицензии доступен в файле [LICENSE](LICENSE).

<div align="center">

**Сделано с душой для настоящих фанатов классики** 💗

*Если вам понравился проект — поставьте звезду на GitHub! ⭐*

[⬆ Наверх](#-консольная-змейка--console-snake)

</div>

---

## 🇬🇧 English version

### 🚀 Project Launch

#### Local launch
```bash
# Clone the repository
git clone https://github.com/su57ks/Console-Snake.git

# Go to the project folder
cd Console-Snake

# Install dependencies
pip install keyboard

# Run the game
python snake.py
```

#### Requirements
- Python 3.x
- `keyboard` library
- Terminal with ANSI color support

---

### 📝 Project Description
**Console Snake** is a classic Snake game implemented entirely in the terminal. The project features teleportation when leaving the field boundaries instead of standard walls, colored display, and support for user-created maps in JSON format.

The project is "hand-coded" without complex game engines — just pure Python and minimal dependencies.

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🎮 **Gameplay** | WASD control | Intuitive hotkey control |
| | Teleportation | Snake appears on the opposite side when leaving the field |
| | Game timer | Displays current session time after each move |
| 🎨 **Visual** | Colored graphics | Snake — red blocks (`██`), field — yellow (`░░`) |
| | ANSI support | 24-bit colors in terminal |
| 🗺 **Maps** | JSON format | Easy level creation and editing |
| | RGB colors | Each cell can have its own color |
| | Obstacle system | Ability to create impassable walls |
| ⚡ **Technical** | Multithreading | Separate thread for key waiting |
| | Minimal dependencies | Only 1 third-party library |

---

### 🎮 Gameplay & Mechanics

#### Controls
| Key | Action |
|-----|--------|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| `Ctrl+C` | Exit game |

#### Rules
1. The snake moves in the chosen direction
2. When leaving the field, it appears on the opposite side (teleportation)
3. Collision with own tail leads to death
4. Game time is displayed after each move

---

### 🗺 Map System

#### JSON Format
```json
{
  "name": "Example Map",
  "description": "Map description",
  "author": "Author Name",
  "size": [3, 1],
  "structure": [
    {
      "coords": [0, 0],
      "empty": true,
      "color": [240, 240, 240]
    },
    {
      "coords": [1, 0],
      "empty": false,
      "color": [100, 100, 100]
    }
  ]
}
```

#### Map Fields
| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Level name |
| `description` | string | Level description |
| `author` | string | Map creator |
| `size` | array | Dimensions [x, y] |
| `structure` | array | Array of cells |
| `coords` | array | Coordinates [x, y] |
| `empty` | bool | `true` — passable, `false` — wall |
| `color` | array | RGB color [r, g, b] |

> **Note:** The map system is under development and not yet integrated into the main gameplay.

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
| | |
|---|------|
| **👨‍💻 Hand-coded** | All code is written manually, without ready-made templates or game engines — a personal touch is evident |
| **📦 Minimal dependencies** | Only 1 third-party library (`keyboard`). Everything else is pure Python |
| **🎨 Colored interface** | Full-color terminal output with 24-bit RGB support |
| **🧩 Extensibility** | Easy to add new maps via JSON |
| **🔄 Teleportation** | Non-standard mechanic instead of boring walls |
| **⚡ Multithreading** | Responsive controls thanks to separate thread for keys |

#### ❌ Disadvantages
| | |
|---|------|
| **🖥 Console interface** | Everything happens in the terminal — no graphical interface, only symbols |
| **🍎 Permission issues** | On macOS and Linux, the `keyboard` library requires superuser rights |
| **🍔 No food mechanic** | Food collection is not implemented yet — the snake has a fixed starting length |
| **🚫 No score system** | No point tracking or high scores |
| **🐌 No speed increase** | Movement speed is constant, doesn't increase |
| **🗺 Maps not in game** | JSON maps exist but don't affect gameplay yet |

---

### 📁 Project Structure

```
📦 Console-Snake
├── 📄 snake.py                          # Main game file
├── 📁 maps/                              # Maps folder
│   └── 📄 example.json                    # Example map
├── 📄 README.md                          # Documentation
└── 📄 LICENSE                            # GPLv3 License
```

---

### 🛠 Technologies

| Technology | Application |
|------------|-------------|
| **Python 3** | Main game logic |
| **keyboard** | Global key press interception |
| **threading** | Asynchronous input waiting |
| **ANSI escape codes** | Colored terminal output |
| **JSON** | Map storage and loading |

---

## 👨‍💻 For Developers

### 🔧 snake.py Functions

| Function | Purpose | Parameters | Return Value |
|---------|------------|-----------|----------------------|
| `w_move()`, `a_move()`, `s_move()`, `d_move()` | Wrapper functions to call `calculate()` with corresponding direction | None | `None` |
| `close()` | Exits the game with "Good luck!" message | None | `None` (terminates process) |
| `lst2str(lst)` | Converts a list of strings into one string with line breaks | `lst`: list of strings | `string`: joined string |
| `dict2str(dct)` | Converts a dictionary of strings into one string with line breaks | `dct`: dictionary with indices 0..n | `string`: joined string |
| `draw(positions_dict)` | Draws the game field | `positions_dict`: dictionary with snake coordinates | `None` (prints to console) |
| `out(position)` | Handles boundary exit (teleportation) | `position`: list [x, y] | `position`: corrected coordinates |
| `free(positions_dict)` | Finds free cells on the field | `positions_dict`: dictionary with snake coordinates | `free`: list of free cells |
| `calculate(command)` | Main movement and logic function | `command`: string "w", "a", "s", "d" | `None` (updates global variables) |

#### Detailed Analysis of Key Functions

**calculate(command)** — the heart of the game
```python
def calculate(command):
    global positions
    global hotkey_pressed
    hotkey_pressed.set()                    # Signal key press
    hotkey_pressed = threading.Event()      # Reset event
    new_positions = {}
    nums = sorted(positions.keys())          # [-1, 0, 1, 2, 3]
    mx = max(nums)                           # 3 (head index)
    
    # Calculate new head position based on direction
    if command == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)                    # Teleport if needed
    new_positions[mx] = upgr_last            # New head

    # Collision check and move other segments
    for num in nums:
        if positions[num] == upgr_last:      # If head collides with body
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]  # Segment follows previous

    print("\n"*100)                          # Clear screen
    draw(new_positions)                       # Draw
    print("Play time:", round(time() - play_time, 2), "seconds")
    positions = new_positions                  # Update global variable
```
**What it does:**
- Gets movement command
- Calculates new head position
- Applies teleportation via `out()`
- Checks collision with body
- Moves all segments
- Redraws field
- Updates timer

**Features:**
- Key `-1` in `positions` dictionary is a technical element for future mechanics
- Snake stored as `{index: [x, y]}`, higher index = head
- Teleportation applied only to head

---

**draw(positions_dict)** — field rendering
```python
def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(YSIZE):
        line = ""
        for x in range(XSIZE):
            find = False
            for position in positions:
                if position[0] == x and position[1] == y:
                    line += "\033[38;2;255;0;0m██\033[m"  # Red snake
                    find = True
            if find is False:
                line += "\033[38;2;255;255;0m░░\033[m"    # Yellow field
        lines[y] = line
    print(dict2str(lines))
```
**What it does:**
- Iterates through all field cells
- Checks if cell contains snake segment
- If yes — draws red block
- If no — draws yellow block
- Formats output via `dict2str()`

**Features:**
- Double loop over Y and X
- Uses ANSI codes for 24-bit color
- Each call completely redraws the field

---

**out(position)** — teleportation
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
**What it does:**
- Checks if point is within field boundaries
- If left edge — appears on right
- If right edge — appears on left
- If top edge — appears on bottom
- If bottom edge — appears on top

**Features:**
- Creates "torus" effect (field is looped)
- Applied only to snake's head

---

**free(positions_dict)** — find free cells
```python
def free(positions_dict):
    positions = list(positions_dict.values())
    print(positions)
    free = []
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions:
                free.append([x, y])
    return free
```
**What it does:**
- Gets all occupied cells
- Iterates through entire field
- If cell is free — adds to free list

**Features:**
- Prepared for future food mechanics
- Currently only prints occupied positions to console

---

### 🗺 How to Add a Map

1. Create a JSON file in the `/maps` folder
2. Fill in the structure following `example.json`:

```json
{
  "name": "Map name",
  "description": "Description",
  "author": "Your name",
  "size": [width, height],
  "structure": [
    {
      "coords": [x, y],
      "empty": true/false,
      "color": [r, g, b]
    }
  ]
}
```

3. Coordinates must be within `size` limits
4. `empty: false` creates an impassable wall
5. Color is set in RGB format (0-255)

> **Important:** Map integration into the game is under development

---

### 🚀 Development Plans

- [ ] Add food mechanic and snake growth
- [ ] Integrate JSON maps into gameplay
- [ ] Score system and high scores
- [ ] Speed increase as snake grows
- [ ] Load random map on start
- [ ] Progress saving

---

### 📜 License

This project is licensed under the **GNU General Public License v3 (GPLv3)**.

**Key provisions:**
- ✅ Free use and distribution
- ✅ Access to source code
- ✅ Modification and improvement
- ❌ Closing the source code

Full license text is available in the [LICENSE](LICENSE) file.

<div align="center">

**Made with soul for true fans of the classics** 💗

*If you like the project — give it a star on GitHub! ⭐*

[⬆ Back to top](#-консольная-змейка--console-snake)

</div>
