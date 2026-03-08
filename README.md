# 🐍 Консольная Змейка / Console Snake

<div align="center">

![Version](https://img.shields.io/badge/версия-1.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-GPLv3-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Console](https://img.shields.io/badge/платформа-консоль-black.svg?style=for-the-badge&labelColor=black)

**✨ Классическая игра "Змейка" с расширенными возможностями: цветной интерфейс, пользовательские карты и система телепортации через стены ✨**

</div>

---

## 📋 Содержание
- [🐍 Русская версия](#-русская-версия)
  - [🚀 Запуск проекта](#-запуск-проекта)
  - [👥 Команда проекта](#-команда-проекта)
  - [📝 Описание проекта](#-описание-проекта)
  - [✨ Ключевые возможности](#-ключевые-возможности)
  - [🎮 Геймплей и механики](#-геймплей-и-механики)
  - [🗺 Система карт](#-система-карт)
  - [📁 Структура проекта](#-структура-проекта)
  - [🛠 Технологии](#-технологии)
  - [📜 Лицензия](#-лицензия)
- [🇬🇧 English version](#-english-version)
  - [🚀 Project Launch](#-project-launch)
  - [👥 Project Team](#-project-team)
  - [📝 Project Description](#-project-description)
  - [✨ Key Features](#-key-features)
  - [🎮 Gameplay & Mechanics](#-gameplay--mechanics)
  - [🗺 Map System](#-map-system)
  - [📁 Project Structure](#-project-structure-1)
  - [🛠 Technologies](#-technologies-1)
  - [📜 License](#-license-1)

---

## 🐍 Русская версия

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

### 👥 Команда проекта

| Роль | Имя | Контакт |
|------|-----|---------|
| 👨‍💻 **Автор** | Aizen | [@su57ks](https://t.me/su57ks) |

---

### 📝 Описание проекта
**Console Snake** — это классическая игра "Змейка", реализованная полностью в терминале с необычными механиками. Вместо стандартных стен змейка телепортируется при выходе за границы поля, а карты хранятся в формате JSON, что позволяет создавать собственные уровни с уникальными цветовыми схемами.

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
1. Змейка постоянно движется в выбранном направлении
2. При выходе за границу поля она появляется с противоположной стороны (эффект "тора")
3. Столкновение с собственным хвостом приводит к смерти
4. Цель — набрать как можно больше очков (функция еды в разработке)

#### Отображение в терминале
```
Змейка (█):
\033[38;2;255;0;0m██\033[m — голова и тело

Поле (░):
\033[38;2;255;255;0m░░\033[m — пустые клетки
```

---

### 🗺 Система карт

#### Формат JSON
```json
{
  "name": "Map of Soul society",
  "description": "Hado №90: Kurohitsugi!",
  "author": "Aizen Sosuke",
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

### 📜 Лицензия

Проект распространяется под лицензией **GNU General Public License v3 (GPLv3)**.

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

Это свободная лицензия: вы можете распространять и/или изменять
программу в соответствии с условиями GNU General Public License...
```

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

### 👥 Project Team

| Role | Name | Contact |
|------|------|---------|
| 👨‍💻 **Author** | Aizen | [@su57ks](https://t.me/su57ks) |

---

### 📝 Project Description
**Console Snake** is a classic Snake game implemented entirely in the terminal with unusual mechanics. Instead of standard walls, the snake teleports when going beyond the field boundaries, and maps are stored in JSON format, allowing you to create custom levels with unique color schemes.

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🎮 **Gameplay** | WASD control | Intuitive hotkey control |
| | Teleportation | Snake appears on the opposite side when leaving the field |
| | Game timer | Displays current session time |
| 🎨 **Visual** | Colored graphics | Snake — red blocks (`██`), field — yellow (`░░`) |
| | ANSI support | 24-bit colors in terminal |
| 🗺 **Maps** | JSON format | Easy level creation and editing |
| | RGB colors | Each cell can have its own color |
| | Obstacle system | Ability to create impassable walls |
| ⚡ **Technical** | Multithreading | Separate thread for key waiting |

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
1. The snake continuously moves in the chosen direction
2. When leaving the field, it appears on the opposite side ("torus" effect)
3. Collision with own tail leads to death
4. Goal — to score as many points as possible (food function in development)

---

### 🗺 Map System

#### JSON Format
```json
{
  "name": "Map of Soul society",
  "description": "Hado №90: Kurohitsugi!",
  "author": "Aizen Sosuke",
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
