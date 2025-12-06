# Python Basic Programming Syntax — Tutorials & Examples

A comprehensive, beginner-friendly collection of Python notes and runnable scripts. Topics include core syntax, OOP, exceptions, files & OS, modules/packages, web scraping, and mini Pygame projects. Each example is small, focused, and easy to run from the command line.

## Why This Repository
- Practical, hands-on learning with minimal boilerplate
- Organized by topic for quick lookup and reference
- Examples are self-contained and demonstrate one concept at a time
- Suitable for self-study, coursework, and interview warm‑ups

## Folder Structure
```
基本编程语法学习笔记/
├─ 单例设计/                 # design patterns: singleton via __new__
├─ 封装系统项目集/           # simple encapsulation exercises & projects
├─ 异常/                     # try/except, raise, propagation
├─ 文件的基本操作/           # file I/O, copy, read/write, os utilities
├─ 模块/                     # imports, packages, aliases, setup
│  └─ hm_message/            # tiny example package (send/receive)
├─ 爬虫/                     # requests, BeautifulSoup, regex, CSV outputs
│  ├─ 学习案例/              # small learning demos
│  └─ 实战正式项目/          # full scraping scripts with data
├─ pygame项目实战/           # step-by-step Pygame demos & mini games
├─ test/ test1/              # small sandboxes for experiments
└─ resources/screenshots/    # put screenshots used in README here
```

## Detailed Contents

### 单例设计 (Singleton via `__new__`)
- `__new__方法重写.py`: Demonstrates overriding `__new__` to ensure only one instance is created. Explains lifecycle differences between `__new__` and `__init__`, object identity (`id()`), and typical pitfalls such as multiple inheritance.
- Use cases: configuration managers, connection pools, and loggers.

### 封装系统项目集 (Encapsulation Exercises)
- `士兵开枪封装案例.py`: Encapsulates Soldier and Gun interactions; methods like `fire()`, ammo management, and responsibility boundaries between objects.
- 名片管理系统: `cards_main.py`, `cards_tools.py`: CLI CRUD demo with functions for add/search/update/delete, file persistence patterns to extend, and simple input validation.
- 房子家具增添系统: 家具类与房屋类的组合关系、面积占用、可用空间检测与异常处理建议。

### 异常 (Exceptions)
- `完整的异常语法.py`: Full try/except/else/finally flow; where to place cleanup.
- `异常的传递.py`: Shows stack propagation and where exceptions surface.
- `异常的简单捕获.py`, `捕获错误类型.py`: Catching broad vs specific exceptions; trade-offs.
- `抛出异常.py`: Raising custom exceptions with helpful messages.

### 文件的基本操作 (Files & OS)
- Read/Write: `读取文件.py`, `写入文件.py`, line-by-line `分行读取文件.py` for memory efficiency.
- Copying: `复制小文件.py` vs `复制大文件.py` (buffered reads and chunk sizes).
- Utilities: `os模块.py` for path ops, listing, and existence checks.
- `eval计算器.py`: Parsing simple arithmetic safely; caveats and safer alternatives (`ast.literal_eval`).
- Notes: `Readme` and `Readme[复件]` contain quick tips.

### 模块 (Modules & Packages)
- Import styles: `导入模块.py`, `from_import 导入.py`, aliases `导入模块指定别名.py`.
- Package example `hm_message/`: `send_message.py`, `receive_message.py`, `__init__.py` layout and relative imports.
- `setup.py`: Minimal packaging primer; how Python finds modules; PYTHONPATH basics.
- Name guard demos: `_name_测试导入.py`, `_name_测试模块.py` illustrate `if __name__ == "__main__":` usage.

### 爬虫 (Web Scraping)
- 学习案例:
	- `requests爬虫.py`: Basic GET requests, headers, response handling.
	- `Beautiful soup 爬虫.py`: Parsing HTML with `bs4`, element selection.
	- `正则表达式*.py`: Extracting structured data via regex; pros/cons vs DOM parsers.
	- JSON conversions: `json转换为python.py`, `把python转变为json.py`, sample `text.json`.
- 实战正式项目:
	- `豆瓣高分电影排行榜*.py`: Fetch and write `douban_movies.csv` with columns like title, rating, url.
	- 番茄小说采集: `番茄小说数据爬取*.py`, `fanqie_*.csv` outputs; pagination and category selection.
	- `当当网爬取数据.py`: Example of multi-page scraping and deduplication strategies.
	- `爬取网页所有图片.py`: Download images; file naming, collision handling, and retry policies.
	- `疫情采集信息项目.py`: Data extraction into CSV/JSON; rate-limit and error handling notes.
	- Ethics & legality: obey `robots.txt`, add delays, and do not overload servers.

### 类的继承_派生 (OOP: Inheritance & Polymorphism)
- `单继承.py`, `多继承.py`: Linear vs diamond inheritance; method resolution order (MRO).
- `覆盖父类方法.py`, `拓展父类方法.py`: Overriding and calling `super()` correctly.
- `多态案例.py`: Interface-based programming; behavior substitution.
- Attributes/methods: `类属性.py`, `类方法.py`, `静态方法.py` differences and use cases.
- Privacy: `父类的私有属性及方法.py`, `私有属性与方法.py` show name mangling and access patterns.

### pygame项目实战 (Pygame Demos)
- `1.pygame入门.py` → `9.事件监听.py`: Progressive steps from window creation, drawing backgrounds and sprites, `Rect` usage, to game loop and event handling.
- `大鱼吃小鱼.py`: A small playable demo; movement, collision detection, scoring, and simple state management.
- `测试模块.py`: Quick checks and sandboxes for Pygame utilities.
- Images under `pygame项目实战/images/` used by demos.

### Tests & Sandboxes
- `test/`, `test1/` subfolders provide scratch space for experimenting with code snippets and quick validations.

## Setup
- Requirements: `Python 3.8+`
- Optional dependencies for specific folders are listed in `requirements.txt`:
	- `requests` and `beautifulsoup4` for web scraping
	- `pygame` for Pygame demos

Install all optional dependencies at once:
```bat
pip install -r requirements.txt
```

## How to Run Examples
1) Navigate to the folder of the example.
2) Run the script in `cmd`:
```bat
python 路径\到\示例.py
```
3) For scraping scripts in `爬虫/实战正式项目/`, make sure you have network access and note that outputs like CSV files will be created next to the script.
4) For `pygame项目实战/`, ensure `pygame` is installed and a windowed environment is available.
5) For package demos under `模块/hm_message/`, run a module or import functions:
```bat
python 模块\_name_测试模块.py
python -c "from 模块.hm_message.send_message import send; send()"
```

## Running Tips
- Prefer virtual environments for isolating dependencies.
- On Windows, enable UTF‑8 in `cmd` if you see encoding issues:
```bat
chcp 65001
```
- Use `python -m pip install ...` if `pip` is not on PATH.

## Highlights by Topic
- OOP & Patterns: inheritance, polymorphism, overriding, singleton via `__new__`
- Exceptions: error types, simple/advanced catching, raising, propagation
- Files & OS: safe read/write, copying large files, `os` utilities, `eval` demo
- Modules & Packages: absolute/relative imports, aliases, simple package layout
- Web Scraping: `requests`, `BeautifulSoup`, regex parsing, data export to CSV
- Pygame: window setup, drawing, events, game loop, small playable demos

## Example Outputs
- Scraping: CSV files like `douban_movies.csv`, `fanqie_*.csv` with headers; logs printed on progress and failures.
- Files: Copies created in destination folders; large file copies use chunked reads.
- Pygame: Window renders sprites and detects collisions; close with `Esc` or window button.

## FAQ
- Q: Why are there many small scripts?
	- A: Each script focuses on one concept to reduce cognitive load.
- Q: Do I need all dependencies?
	- A: No. Install only what's needed per folder, or use `requirements.txt` to install all.
- Q: Can I use this for teaching?
	- A: Yes. The examples are designed for classroom demos and assignments.

## Maintainers Notes
- This repository is actively curated for teaching and self‑study.
- Examples are intentionally small and focused; feel free to extend.

## Contributing
- Fork the repository and create a feature branch.
- Keep examples small and focused; match folder/topic organization.
- Add a short docstring and minimal comments to explain intent.
- Provide sample inputs/outputs when relevant (CSV, JSON, screenshots).

## License
MIT
