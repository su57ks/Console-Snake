# 🗺️ Карты для Console Snake

В этой папке находятся примеры карт для игры. Каждая карта хранится в отдельном JSON-файле.

---

## 📋 Содержание

<details>
<summary><b>🇷🇺 Русская версия</b></summary>

<br>

- [📋 Список карт](#-список-карт)
- [🚀 Как использовать](#-как-использовать)
- [🛠️ Создание своей карты](#-создание-своей-карты)
- [📄 Формат карты](#-формат-карты)
- [⚠️ Важно](#-важно)

</details>

<details>
<summary><b>🇬🇧 English version</b></summary>

<br>

- [📋 Available Maps](#-available-maps)
- [🚀 How to Use](#-how-to-use)
- [🛠️ Creating Your Own Map](#-creating-your-own-map)
- [📄 Map Format](#-map-format)
- [⚠️ Important](#-important)

</details>

---

## 🇷🇺 Русская версия

### 📋 Список карт

| Файл | Название | Описание | Автор |
|------|----------|----------|-------|
| `default.json` | Default map | Стандартная карта с жёлтым полем (15×13) | @su57ks |
| `example.json` | Example map | Пример карты для ознакомления с форматом (3×1) | @su57ks |

### 🚀 Как использовать

1. Выберите нужную карту (например, `default.json`)
2. Скопируйте её содержимое в файл `data.json` в корневой папке проекта:
   ```bash
   cp maps/default.json data.json
   ```
3. Запустите игру:
   ```bash
   python snake.py
   ```

### 🛠️ Создание своей карты

1. Создайте новый JSON-файл в этой папке (например, `my_map.json`)
2. Используйте `example.json` как шаблон
3. Заполните поля:
   - `name` — название карты
   - `description` — описание
   - `author` — ваше имя
   - `size` — размеры [x, y]
   - `start` — начальное положение змейки (ключ -1 обязателен)
   - `structure` — объект с клетками (ключи в формате `"x:y"`)
4. Для каждой клетки укажите:
   - `empty`: `true` (проходимо) или `false` (стена)
   - `color`: RGB-цвет `[r, g, b]` (0-255)
5. Скопируйте готовый файл в `data.json` и тестируйте

### 📄 Формат карты

```json
{
  "name": "Название карты",
  "description": "Описание карты",
  "author": "Автор",
  "size": [ширина, высота],
  "start": { "-1": [x, y], "0": [x, y], "1": [x, y], ... },
  "structure": {
    "0:0": { "empty": true, "color": [255, 255, 0] },
    "1:0": { "empty": true, "color": [255, 255, 0] },
    ...
  }
}
```

| Поле | Тип | Описание |
|------|-----|----------|
| `name` | string | Название карты |
| `description` | string | Описание карты |
| `author` | string | Автор карты |
| `size` | array | Размеры [x, y] |
| `start` | object | Начальное положение змейки (ключи -1, 0, 1, 2...) |
| `structure` | object | Объект клеток с ключами `"x:y"` |
| `empty` | bool | `true` — проходимо, `false` — стена |
| `color` | array | RGB-цвет [r, g, b] |

### ⚠️ Важно

- Ключ `-1` в `start` обязателен — это технический элемент
- Индексы в `start` должны идти по порядку: -1, 0, 1, 2, 3...
- Больший индекс = голова змейки
- Для поля размером 15×13 нужно 195 записей в `structure`

---

## 🇬🇧 English version

### 📋 Available Maps

| File | Name | Description | Author |
|------|------|-------------|--------|
| `default.json` | Default map | Standard map with yellow field (15×13) | @su57ks |
| `example.json` | Example map | Example map for learning the format (3×1) | @su57ks |

### 🚀 How to Use

1. Choose a map (e.g., `default.json`)
2. Copy its contents to the `data.json` file in the project root:
   ```bash
   cp maps/default.json data.json
   ```
3. Run the game:
   ```bash
   python snake.py
   ```

### 🛠️ Creating Your Own Map

1. Create a new JSON file in this folder (e.g., `my_map.json`)
2. Use `example.json` as a template
3. Fill in the fields:
   - `name` — map name
   - `description` — description
   - `author` — your name
   - `size` — dimensions [x, y]
   - `start` — snake starting position (key -1 is required)
   - `structure` — cell object with `"x:y"` keys
4. For each cell, specify:
   - `empty`: `true` (passable) or `false` (wall)
   - `color`: RGB color `[r, g, b]` (0-255)
5. Copy the finished file to `data.json` and test

### 📄 Map Format

```json
{
  "name": "Map name",
  "description": "Map description",
  "author": "Author",
  "size": [width, height],
  "start": { "-1": [x, y], "0": [x, y], "1": [x, y], ... },
  "structure": {
    "0:0": { "empty": true, "color": [255, 255, 0] },
    "1:0": { "empty": true, "color": [255, 255, 0] },
    ...
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Map name |
| `description` | string | Map description |
| `author` | string | Map author |
| `size` | array | Dimensions [x, y] |
| `start` | object | Snake starting position (keys -1, 0, 1, 2...) |
| `structure` | object | Cell object with `"x:y"` keys |
| `empty` | bool | `true` — passable, `false` — wall |
| `color` | array | RGB color [r, g, b] |

### ⚠️ Important

- Key `-1` in `start` is required — it's a technical element
- Indices in `start` must be sequential: -1, 0, 1, 2, 3...
- Higher index = snake head
- For a 15×13 field, you need 195 entries in `structure`

---

<div align="center">

**✍️ Примеры карт для Console Snake / Console Snake map examples**

[⬆ Наверх](#-карты-для-console-snake)

</div>
