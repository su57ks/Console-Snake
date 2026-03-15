# 🐍 Консольная Змейка / Console Snake

<div align="center">

![Version](https://img.shields.io/badge/версия-2.0.0-brightgreen.svg?style=for-the-badge&labelColor=black)
![License](https://img.shields.io/badge/лицензия-GPLv3-blue.svg?style=for-the-badge&labelColor=black)
![Python](https://img.shields.io/badge/Python-3.x-3776AB.svg?style=for-the-badge&labelColor=black&logo=python)
![Console](https://img.shields.io/badge/платформа-консоль-black.svg?style=for-the-badge&labelColor=black)
![Dependencies](https://img.shields.io/badge/зависимости-1-important.svg?style=for-the-badge&labelColor=black)
![Human written](https://img.shields.io/badge/написано-человеком-ff69b4.svg?style=for-the-badge&labelColor=black)

**✨ Классическая игра "Змейка" с едой, счётчиком очков и пользовательскими картами ✨**

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
- [📊 Достоинства и недостатки](#-достоинства-и-недостатки)
- [📜 Лицензия](#-лицензия)
- [👨‍💻 Для разработчиков](#-для-разработчиков)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [🚀 Project Launch](#-project-launch)
- [📝 Project Description](#-project-description)
- [✨ Key Features](#-key-features)
- [🎮 Gameplay & Mechanics](#-gameplay--mechanics)
- [📊 Advantages and Disadvantages](#-advantages-and-disadvantages)
- [📜 License](#-license)
- [👨‍💻 For Developers](#-for-developers)

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

**Console Snake** — это классическая игра "Змейка", реализованная полностью в терминале. Проект включает:

- **Еду** — зелёные яблоки, которые увеличивают длину змейки и счёт
- **Счётчик очков** — отображается после каждого хода
- **Телепортацию** — при выходе за границы поля змейка появляется с противоположной стороны
- **Цветные карты** — каждая клетка может иметь свой RGB-цвет
- **Стены** — непроходимые препятствия на карте

Проект написан вручную, без использования искусственного интеллекта — только чистый Python, одна зависимость и человеческий подход к каждой строчке кода.

🔗 **[Информационный сайт игры](https://su57ks.github.io/Snake-info/)** — более подробно и наглядно

---

### ✨ Ключевые возможности

| Категория | Функция | Описание |
|-----------|---------|----------|
| 🎮 **Геймплей** | Управление WASD | Интуитивное управление с горячими клавишами |
| | Еда (яблоки) | Зелёные блоки, увеличивающие длину и счёт |
| | Счётчик очков | Отображается после каждого хода |
| | Телепортация | При выходе за границы поля змейка появляется с противоположной стороны |
| | Стены | Непроходимые препятствия на карте |
| 🎨 **Визуал** | Цветная графика | Змейка — красные блоки, еда — зелёные, поле — цвета из карты |
| | Поддержка ANSI | 24-битные цвета в терминале |

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
2. Съедайте зелёные яблоки (`██`) — они увеличивают длину змейки и счёт
3. При выходе за границу поля змейка телепортируется на противоположную сторону
4. Столкновение с собственным хвостом приводит к смерти
5. Столкновение со стеной приводит к смерти
6. Счёт отображается после каждого хода

#### Цвета в терминале
- **Змейка**: красный цвет
- **Еда**: зелёный цвет
- **Поле**: цвета задаются в карте

---

### 📊 Достоинства и недостатки

#### ✅ Достоинства
- **✍️ Написано человеком** — код написан вручную, без использования ИИ
- **📦 Минимум зависимостей** — всего **1** сторонняя библиотека (`keyboard`)
- **🎨 Цветной интерфейс** — полноцветный вывод в терминале
- **🗺 Пользовательские карты** — можно создавать свои уровни
- **🔄 Телепортация** — нестандартная механика вместо стен по краям
- **⚡ Многопоточность** — отзывчивое управление

#### ❌ Недостатки
- **🖥 Консольный интерфейс** — нет графического интерфейса
- **🍎 Проблемы с permissions** — на Mac/Linux `keyboard` требует прав суперпользователя
- **🐌 Нет ускорения** — скорость движения постоянная

---

### 📜 Лицензия

Проект распространяется под лицензией **GNU General Public License v3 (GPLv3)**.

**Основные положения:**
- ✅ Свободное использование и распространение
- ✅ Доступ к исходному коду
- ✅ Модификация и улучшение
- ❌ Закрытие исходного кода

---

### 👨‍💻 Для разработчиков

Вся техническая документация, описание функций, структура карт и руководство по созданию своих уровней находится в отдельном файле:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — для разработчиков и тех, кто хочет разобраться в устройстве проекта

Там вы найдёте:
- Полное описание всех функций `snake.py`
- Детальный разбор ключевых механик
- Формат карт и примеры
- Настройки `user.json`
- Планы по развитию

---

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

> **Important:** On macOS and Linux, the `keyboard` library may require superuser rights. Alternatively, use `sudo python snake.py`.

---

### 📝 Project Description

**Console Snake** is a classic Snake game implemented entirely in the terminal. The project includes:

- **Food** — green apples that increase snake length and score
- **Score counter** — displayed after each move
- **Teleportation** — snake appears on the opposite side when leaving the field
- **Colored maps** — each cell can have its own RGB color
- **Walls** — impassable obstacles on the map

The project is hand-written, without using artificial intelligence — just pure Python, one dependency, and a human approach to every line of code.

🔗 **[Game Info Site](https://su57ks.github.io/Snake-info/)** — more details and visuals

---

### ✨ Key Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🎮 **Gameplay** | WASD control | Intuitive hotkey control |
| | Food (apples) | Green blocks that increase length and score |
| | Score counter | Displayed after each move |
| | Teleportation | Appear on opposite side when leaving the field |
| | Walls | Impassable obstacles on the map |
| 🎨 **Visual** | Colored graphics | Snake — red, food — green, field — colors from map |
| | ANSI support | 24-bit colors in terminal |

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
2. Eat green apples (`██`) — they increase length and score
3. When leaving the field, the snake teleports to the opposite side
4. Collision with own tail leads to death
5. Collision with a wall leads to death
6. Score is displayed after each move

---

### 📊 Advantages and Disadvantages

#### ✅ Advantages
- **✍️ Human-written** — code written manually, without AI
- **📦 Minimal dependencies** — only **1** library (`keyboard`)
- **🎨 Colored interface** — full-color terminal output
- **🗺 Custom maps** — create your own levels
- **🔄 Teleportation** — non-standard mechanic
- **⚡ Multithreading** — responsive controls

#### ❌ Disadvantages
- **🖥 Console interface** — no graphical interface
- **🍎 Permission issues** — `keyboard` needs sudo on Mac/Linux
- **🐌 No speed increase** — constant movement speed

---

### 📜 License

This project is licensed under the **GNU General Public License v3 (GPLv3)**.

**Key provisions:**
- ✅ Free use and distribution
- ✅ Access to source code
- ✅ Modification and improvement
- ❌ Closing the source code

---

### 👨‍💻 For Developers

All technical documentation, function descriptions, map structure, and guides for creating your own levels are in a separate file:

➡️ **[DEVELOPER.md](DEVELOPER.md)** — for developers and those who want to understand the project's internals

There you will find:
- Complete description of all `snake.py` functions
- Detailed analysis of key mechanics
- Map format and examples
- `user.json` settings
- Development plans

---

<div align="center">

**Made with soul for true fans of the classics** 💗

*If you like the project — give it a star on GitHub! ⭐*

[![Info Site](https://img.shields.io/badge/info_site-Snake--info-9cf?style=for-the-badge)](https://su57ks.github.io/Snake-info/)

[⬆ Back to top](#-консольная-змейка--console-snake)

</div>
