# BooksManager 📚
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

本项目为基于 Python 构建的实体藏书管理目录网站项目。通过该项目，用户可以轻松地从 Excel 文件中读取电子书信息，并将其展示在一个美观且功能丰富的网页上。项目提供了书籍搜索、分类浏览、标签筛选等功能。

## 主要功能

- **数据读取**：从 Excel 文件中读取电子书的详细信息，包括书名、作者、出版社、出版日期、分类、书籍存放位置、标签等。
- **网页展示**：基于 Jinja2 及 Bootstrap5 创建网页，将书籍基本信息以卡片式布局展示在网页上。
- **书籍搜索**：提供搜索框，允许用户按书名、作者、出版社或标签检索电子书。
- **分类展示**：通过侧边栏展示书籍的所属类型，用户可以通过分类列表查看不同类型的书籍。
- **存放位置**：记录不同书籍的存放位置，从而在藏书较多的情况下更方便的找到对应的书籍。

## 使用教程

1. 准备包含书籍信息的 Excel 文件 (`books.xlsx`)，确保其包含以下列：书名、作者、出版社、出版年份、类别、存放位置、标签，并将其与 `generate_book_website.py` 和 `book_template.html` 放置在同一目录下。

3. 确保已安装 Python 3.6 或更高版本。

4. 安装项目所需的 Python 依赖库：`pandas` 和 `Jinja2`。可以使用以下命令安装：
   ```bash
   pip install pandas Jinja2
   ```

5. 运行 Python 脚本：
   ```bash
   python generate_book_website.py
   ```

6. 打开生成的 `books.html` 文件，即可在浏览器中查看书籍管理网页。

## 技术栈

- **核心框架**：Python 3.8+
- **数据处理**：pandas + re
- **网页生成**：Jinja2 + Bootstrap5

## 项目结构

- **generate_book_website.py**: Python 脚本，用于读取 Excel 文件并生成书籍 HTML 网页。
- **book_template.html**: HTML 模板文件，定义了书籍管理网页的结构和样式。
- **books.xlsx**：Excel 文件，存储书籍信息（需自行创建或准备）。
- **books.html**：生成的输出文件，包含书籍管理网页内容。
