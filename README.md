# 🐍 Консольная Змейка / Console Snake

<div align="center">

![Version](https://img.shields.io/badge/версия-1.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-GPLv3-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Console](https://img.shields.io/badge/платформа-консоль-black.svg?style=for-the-badge&labelColor=black)
![Dependencies](https://img.shields.io/badge/зависимости-1-important.svg?style=for-the-badge&labelColor=black)
![Human written](https://img.shields.io/badge/написано-человеком-ff69b4.svg?style=for-the-badge&labelColor=black)

**✨ Классическая игра "Змейка" с цветным интерфейсом, телепортацией и пользовательскими картами ✨**

[![Info Site](https://img.shields.io/badge/инфо_сайт-Snake--info-9cf?style=for-the-badge)](https://su57ks.github.io/Snake-info/)

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
  - [Формат data.json](#-формат-datajson)
  - [Конфигурация user.json](#-конфигурация-userjson)
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
  - [data.json Format](#-datajson-format)
  - [user.json Configuration](#-userjson-configuration)
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

# Установите единственную зависимость
pip install keyboard

# Запустите игру
python snake.py
```

#### Требования
- Python 3.x
- Библиотека: `keyboard` (единственная зависимость)
- Терминал с поддержкой ANSI-цветов (все современные терминалы)

> **Важно:** На macOS и Linux для работы `keyboard` могут потребоваться права суперпользователя. Альтернативно можно использовать `sudo python snake.py`.

---

### 📝 Описание проекта
**Console Snake** — это классическая игра "Змейка", реализованная полностью в терминале. Особенность проекта — телепортация при выходе за границы поля вместо стандартных стен, цветное отображение и полноценная поддержка пользовательских карт в формате JSON (теперь карты полностью интегрированы в геймплей!).

Проект написан вручную, без использования искусственного интеллекта — только чистый Python, минимум зависимостей и человеческий подход к каждой строчке кода.

🔗 **[Информационный сайт игры](https://su57ks.github.io/Snake-info/)** — более подробно и наглядно

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🎮 **Геймплей** | Управление WASD | Интуитивное управление с горячими клавишами |
| | Телепортация | При выходе за границы поля змейка появляется с противоположной стороны |
| | Таймер игры | Отображается время текущей сессии |
| | Препятствия на карте | Стены, которые убивают змейку при столкновении |
| 🎨 **Визуал** | Цветная графика | Змейка — красные блоки (`██`), поле — настраиваемые цвета из карты |
| | Поддержка ANSI | 24-битные цвета в терминале, каждый блок может иметь свой RGB-цвет |
| 🗺 **Карты** | JSON-формат | Простое создание и редактирование уровней |
| | Полная интеграция | Карты теперь влияют на геймплей (цвета поля и стены) |
| | RGB-цвета | Каждая клетка может иметь свой цвет |
| | Система препятствий | Возможность создавать непроходимые стены (`empty: false`) |
| ⚡ **Техническое** | Многопоточность | Отдельный поток для ожидания клавиш |
| | Умная очистка | Адаптивная очистка экрана под среду выполнения |
| | **Минимум зависимостей** | Всего **1** сторонняя библиотека (`keyboard`) |

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
4. **Столкновение со стеной** (клетка с `"empty": false`) также приводит к смерти
5. Время игры отображается после каждого хода

#### Отображение в терминале
```
Змейка (█):
\033[38;2;255;0;0m██\033[m — красные блоки (цвет фиксированный)

Поле (░):
цвет берётся из data.json для каждой клетки
```

---

### 🗺 Система карт

#### Главный файл карт: `data.json`
Игра загружает карту из `data.json` при запуске. Формат полностью обновлён и теперь использует объект для быстрого доступа к клеткам.

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "structure": {
        "0:0": {"coords": [0, 0], "empty": true, "color": [255, 255, 0]},
        "1:0": {"coords": [1, 0], "empty": true, "color": [255, 255, 0]},
        ...
        "14:12": {"coords": [14, 12], "empty": true, "color": [255, 255, 0]}
      }
    }
  }
}
```

#### Поля карты
| Поле | Тип | Описание |
|------|-----|----------|
| `name` | string | Название уровня |
| `description` | string | Описание уровня |
| `author` | string | Создатель карты |
| `size` | array | Размеры [x, y] |
| `structure` | object | Объект клеток с ключами `"x:y"` |
| `coords` | array | Координаты [x, y] |
| `empty` | bool | `true` — проходимо, `false` — стена (смерть) |
| `color` | array | RGB-цвет [r, g, b] для отрисовки клетки |

> **Важно:** Теперь карты **полностью интегрированы**! Цвет поля берётся из `data.json`, а стены (`empty: false`) убивают змейку.

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
| | |
|---|------|
| **✍️ Написано человеком** | **Самое главное** — код написан вручную, без использования ChatGPT и других ИИ. Каждая строчка продумана и написана своими руками |
| **📦 Минимум зависимостей** | Всего **1** сторонняя библиотека (`keyboard`). Всё остальное — чистый Python |
| **🎨 Цветной интерфейс** | Полноцветный вывод в терминале с поддержкой 24-битных RGB-цветов для каждой клетки |
| **🗺 Полная поддержка карт** | Карты полностью интегрированы: влияют на цвета и создают стены |
| **🔄 Телепортация** | Нестандартная механика вместо скучных стен |
| **⚡ Многопоточность** | Отзывчивое управление благодаря отдельному потоку для клавиш |
| **🔄 Умная очистка** | Адаптируется под среду выполнения (консоль/IDE) |

#### ❌ Недостатки
| | |
|---|------|
| **🖥 Консольный интерфейс** | Всё происходит в терминале — нет графического интерфейса, только символы |
| **🍎 Проблемы с permissions** | На macOS и Linux библиотека `keyboard` требует прав суперпользователя |
| **🍔 Отсутствует еда** | Механика сбора еды пока не реализована — змейка имеет фиксированную начальную длину |
| **🚫 Нет счёта** | Отсутствует система подсчёта очков и рекордов |
| **🐌 Нет ускорения** | Скорость движения постоянная, не увеличивается |
| **📁 Одна карта** | Пока загружается только `default` карта, без выбора |

---

### 📁 Структура проекта

```
📦 Console-Snake
├── 📄 snake.py                          # Основной файл игры
├── 📄 data.json                         # Файл с картой (теперь здесь)
├── 📄 user.json                         # Конфигурация пользователя
├── 📄 README.md                          # Документация
└── 📄 LICENSE                            # Лицензия GPLv3
```

> **Примечание:** Папка `maps/` больше не используется — все карты хранятся в `data.json`.

---

### 🛠 Технологии

| Технология | Применение |
|------------|------------|
| **Python 3** | Основная логика игры |
| **keyboard** | Глобальный перехват нажатий клавиш (единственная зависимость) |
| **threading** | Асинхронное ожидание ввода |
| **ANSI escape codes** | Цветной вывод в терминал |
| **JSON** | Хранение карты и конфигурации |
| **codecs** | Чтение файлов с UTF-8 BOM |

---

## 👨‍💻 Для разработчиков

### 🔧 Функции snake.py

| Функция | Назначение | Параметры | Возвращаемое значение |
|---------|------------|-----------|----------------------|
| `clear()` | Очищает экран в зависимости от среды | Нет | `None` |
| `w_move()`, `a_move()`, `s_move()`, `d_move()` | Функции-обёртки для вызова `calculate()` | Нет | `None` |
| `close()` | Завершает игру с сообщением "Good luck!" | Нет | `None` (завершает процесс) |
| `lst2str(lst)` | Преобразует список строк в одну строку | `lst`: список строк | `string`: объединённая строка |
| `dict2str(dct)` | Преобразует словарь строк в одну строку | `dct`: словарь с индексами 0..n | `string`: объединённая строка |
| `draw(positions_dict)` | Отрисовывает игровое поле | `positions_dict`: координаты змейки | `None` (выводит в консоль) |
| `out(position)` | Обрабатывает выход за границы поля (телепортация) | `position`: список [x, y] | `position`: скорректированные координаты |
| `free(positions_dict)` | Находит свободные клетки на поле | `positions_dict`: координаты змейки | `free`: список свободных клеток |
| `calculate(command)` | Основная функция движения и логики | `command`: "w", "a", "s", "d" | `None` (обновляет глобальные переменные) |

#### Детальный разбор ключевых функций

**Загрузка карты при старте**
```python
with codecs.open("data.json", "r", "utf_8_sig") as f:
    map = json.load(f)["maps"]["default"]
```
Теперь карта загружается из `data.json` один раз при запуске и доступна глобально.

---

**draw(positions_dict)** — отрисовка поля (обновлена)
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
                color = map["structure"][f"{x}:{y}"]["color"]  # Цвет из карты!
                line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"
        lines[y] = line
    print(dict2str(lines))
```
**Что нового:**
- Цвет поля теперь берётся из `data.json` для каждой клетки
- Поддержка 24-битных RGB-цветов

---

**calculate(command)** — проверка стен
```python
def calculate(command):
    # ... вычисление новой позиции ...
    upgr_last = out(last)
    new_positions[mx] = upgr_last

    for num in nums:
        # Проверка на столкновение с телом ИЛИ со стеной!
        if positions[num] == upgr_last or map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]
    # ...
```
**Что нового:**
- Добавлена проверка на столкновение со стеной (`"empty": false`)
- Смерть при попадании на такую клетку

---

### 🗺 Формат data.json

Теперь игра использует единый файл `data.json` для хранения карты:

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "structure": {
        "0:0": {"coords": [0, 0], "empty": true, "color": [255, 255, 0]},
        "0:1": {"coords": [0, 1], "empty": true, "color": [255, 255, 0]},
        ...
      }
    }
  }
}
```

**Как создать свою карту:**
1. Скопируйте структуру `default`
2. Измените `name`, `description`, `author`
3. Задайте нужные цвета для каждой клетки (RGB)
4. Установите `"empty": false` для клеток-стен
5. Сохраните в `data.json`

---

### ⚙️ Конфигурация user.json

```json
{"enviroment": "special"}
```

| Поле | Значение | Описание |
|------|----------|----------|
| `enviroment` | `"console"` | Для системной очистки экрана (`cls`/`clear`) |
| | `"special"` | Для очистки через 100 пустых строк (для IDE) |

---

### 🚀 Планы по развитию

- [x] **Полная интеграция JSON-карт** (цвета и стены)
- [ ] Добавить механику еды и роста змейки
- [ ] Система подсчёта очков и рекордов
- [ ] Увеличение скорости с ростом змейки
- [ ] Выбор карты при старте (не только `default`)
- [ ] Сохранение прогресса
- [ ] Поддержка разных цветовых схем через `user.json`

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

[![Info Site](https://img.shields.io/badge/инфо_сайт-Snake--info-9cf?style=for-the-badge)](https://su57ks.github.io/Snake-info/)

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

# Install the only dependency
pip install keyboard

# Run the game
python snake.py
```

#### Requirements
- Python 3.x
- Library: `keyboard` (only dependency)
- Terminal with ANSI color support

---

### 📝 Project Description
**Console Snake** is a classic Snake game implemented entirely in the terminal. The project features teleportation when leaving the field boundaries instead of standard walls, colored display, and full support for user-created maps in JSON format (maps are now fully integrated into gameplay!).

The project is hand-written, without using artificial intelligence — just pure Python, minimal dependencies, and a human approach to every line of code.

🔗 **[Game Info Site](https://su57ks.github.io/Snake-info/)** — more details and visuals

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🎮 **Gameplay** | WASD control | Intuitive hotkey control |
| | Teleportation | Snake appears on the opposite side when leaving the field |
| | Game timer | Displays current session time after each move |
| | Map obstacles | Walls that kill the snake on collision |
| 🎨 **Visual** | Colored graphics | Snake — red blocks (`██`), field — colors from map |
| | ANSI support | 24-bit colors in terminal, each cell can have its own RGB color |
| 🗺 **Maps** | JSON format | Easy level creation and editing |
| | Full integration | Maps now affect gameplay (field colors and walls) |
| | RGB colors | Each cell can have its own color |
| | Obstacle system | Impassable walls (`empty: false`) |
| ⚡ **Technical** | Multithreading | Separate thread for key waiting |
| | Smart clearing | Adaptive screen clearing for different environments |
| | **Minimal dependencies** | Only **1** third-party library (`keyboard`) |

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
4. **Collision with a wall** (`"empty": false` cell) also leads to death
5. Game time is displayed after each move

---

### 🗺 Map System

#### Main map file: `data.json`
The game loads the map from `data.json` at startup. The format has been updated to use an object for fast cell access.

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "structure": {
        "0:0": {"coords": [0, 0], "empty": true, "color": [255, 255, 0]},
        "1:0": {"coords": [1, 0], "empty": true, "color": [255, 255, 0]},
        ...
        "14:12": {"coords": [14, 12], "empty": true, "color": [255, 255, 0]}
      }
    }
  }
}
```

#### Map Fields
| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Level name |
| `description` | string | Level description |
| `author` | string | Map creator |
| `size` | array | Dimensions [x, y] |
| `structure` | object | Cell object with `"x:y"` keys |
| `coords` | array | Coordinates [x, y] |
| `empty` | bool | `true` — passable, `false` — wall (death) |
| `color` | array | RGB color [r, g, b] for cell rendering |

> **Important:** Maps are now **fully integrated**! Field colors come from `data.json`, and walls (`empty: false`) kill the snake.

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
| | |
|---|------|
| **✍️ Human-written** | **The most important** — code is written manually, without ChatGPT or other AI. Every line is thought through and written by hand |
| **📦 Minimal dependencies** | Only **1** third-party library (`keyboard`). Everything else is pure Python |
| **🎨 Colored interface** | Full-color terminal output with 24-bit RGB support for each cell |
| **🗺 Full map support** | Maps are fully integrated: affect colors and create walls |
| **🔄 Teleportation** | Non-standard mechanic instead of boring walls |
| **⚡ Multithreading** | Responsive controls thanks to separate thread for keys |
| **🔄 Smart clearing** | Adapts to execution environment (console/IDE) |

#### ❌ Disadvantages
| | |
|---|------|
| **🖥 Console interface** | Everything happens in the terminal — no graphical interface, only symbols |
| **🍎 Permission issues** | On macOS and Linux, the `keyboard` library requires superuser rights |
| **🍔 No food mechanic** | Food collection is not implemented yet — the snake has a fixed starting length |
| **🚫 No score system** | No point tracking or high scores |
| **🐌 No speed increase** | Movement speed is constant, doesn't increase |
| **📁 Single map** | Only `default` map loads, no selection yet |

---

### 📁 Project Structure

```
📦 Console-Snake
├── 📄 snake.py                          # Main game file
├── 📄 data.json                         # Map file (now here)
├── 📄 user.json                         # User configuration
├── 📄 README.md                          # Documentation
└── 📄 LICENSE                            # GPLv3 License
```

> **Note:** The `maps/` folder is no longer used — all maps are stored in `data.json`.

---

### 🛠 Technologies

| Technology | Application |
|------------|-------------|
| **Python 3** | Main game logic |
| **keyboard** | Global key press interception (only dependency) |
| **threading** | Asynchronous input waiting |
| **ANSI escape codes** | Colored terminal output |
| **JSON** | Map storage and configuration |
| **codecs** | Reading UTF-8 BOM files |

---

## 👨‍💻 For Developers

### 🔧 snake.py Functions

| Function | Purpose | Parameters | Return Value |
|---------|------------|-----------|----------------------|
| `clear()` | Clears screen based on environment | None | `None` |
| `w_move()`, `a_move()`, `s_move()`, `d_move()` | Wrapper functions to call `calculate()` | None | `None` |
| `close()` | Exits the game with "Good luck!" message | None | `None` (terminates process) |
| `lst2str(lst)` | Converts a list of strings into one string | `lst`: list of strings | `string`: joined string |
| `dict2str(dct)` | Converts a dictionary of strings into one string | `dct`: dictionary with indices 0..n | `string`: joined string |
| `draw(positions_dict)` | Draws the game field | `positions_dict`: snake coordinates | `None` (prints to console) |
| `out(position)` | Handles boundary exit (teleportation) | `position`: list [x, y] | `position`: corrected coordinates |
| `free(positions_dict)` | Finds free cells on the field | `positions_dict`: snake coordinates | `free`: list of free cells |
| `calculate(command)` | Main movement and logic function | `command`: "w", "a", "s", "d" | `None` (updates global variables) |

#### Key Functions Detailed

**Map loading at start**
```python
with codecs.open("data.json", "r", "utf_8_sig") as f:
    map = json.load(f)["maps"]["default"]
```
Now the map is loaded from `data.json` once at startup and is globally available.

---

**draw(positions_dict)** — updated rendering
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
                color = map["structure"][f"{x}:{y}"]["color"]  # Color from map!
                line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"
        lines[y] = line
    print(dict2str(lines))
```
**What's new:**
- Field color now comes from `data.json` for each cell
- Support for 24-bit RGB colors

---

**calculate(command)** — wall collision
```python
def calculate(command):
    # ... calculate new position ...
    upgr_last = out(last)
    new_positions[mx] = upgr_last

    for num in nums:
        # Collision with body OR with wall!
        if positions[num] == upgr_last or map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]
    # ...
```
**What's new:**
- Added wall collision check (`"empty": false`)
- Death upon hitting such a cell

---

### 🗺 data.json Format

The game now uses a single `data.json` file to store the map:

```json
{
  "maps": {
    "default": {
      "name": "Default map",
      "description": "обычная карта",
      "author": "@su57ks",
      "size": [15, 13],
      "structure": {
        "0:0": {"coords": [0, 0], "empty": true, "color": [255, 255, 0]},
        "0:1": {"coords": [0, 1], "empty": true, "color": [255, 255, 0]},
        ...
      }
    }
  }
}
```

**How to create your own map:**
1. Copy the `default` structure
2. Change `name`, `description`, `author`
3. Set desired RGB colors for each cell
4. Set `"empty": false` for wall cells
5. Save to `data.json`

---

### ⚙️ user.json Configuration

```json
{"enviroment": "special"}
```

| Field | Value | Description |
|-------|-------|-------------|
| `enviroment` | `"console"` | For system screen clearing (`cls`/`clear`) |
| | `"special"` | For clearing via 100 empty lines (for IDEs) |

---

### 🚀 Development Plans

- [x] **Full JSON map integration** (colors and walls)
- [ ] Add food mechanic and snake growth
- [ ] Score system and high scores
- [ ] Speed increase as snake grows
- [ ] Map selection at startup (not just `default`)
- [ ] Progress saving
- [ ] Support for different color schemes via `user.json`

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

[![Info Site](https://img.shields.io/badge/info_site-Snake--info-9cf?style=for-the-badge)](https://su57ks.github.io/Snake-info/)

[⬆ Back to top](#-консольная-змейка--console-snake)

</div>
