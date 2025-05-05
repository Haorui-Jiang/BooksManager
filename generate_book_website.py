import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os
import sys
import re

def read_books_from_excel(file_path):
    """从Excel文件中读取实体书信息"""
    df = pd.read_excel(file_path)
    books = []
    
    for i, row in df.iterrows():
        # 读取书籍的基本信息
        name = row["书名"]
        author = row["作者"]
        publisher = row["出版社"]
        publish_year = row["出版年份"]
        category = row["类别"]
        storage_location = row["存放位置"]
        tags = row["标签"]
        
        # 处理标签字段，识别中英文逗号
        if pd.notna(tags):
            # 使用正则表达式匹配中英文逗号
            tags = re.split(r'[,，]+', tags)
            tags = [tag.strip() for tag in tags if tag.strip()]
        else:
            tags = []
        
        book = {
            "name": name,
            "author": author,
            "publisher": publisher,
            "publish_year": publish_year,
            "category": category,
            "storage_location": storage_location,
            "tags": tags
        }
        books.append(book)
    
    return books

def generate_html(books, template_path):
    """使用Jinja2生成HTML模板"""
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    html_output = template.render(books=books)
    return html_output

if __name__ == "__main__":
    excel_file = "books.xlsx"  # Excel文件路径
    template_file = "book_template.html"  # HTML模板文件路径
    output_file = "books.html"  # 输出的HTML文件路径

    # 检查Excel文件是否存在
    if not os.path.exists(excel_file):
        print(f"错误: 未找到Excel文件 {excel_file}")
        sys.exit(1)

    # 读取实体书数据
    books = read_books_from_excel(excel_file)
    if not books:
        print("警告: Excel文件中没有实体书数据")
    
    # 生成HTML内容
    html_content = generate_html(books, template_file)
    
    # 保存HTML文件
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML文件 {output_file} 已成功生成！")
