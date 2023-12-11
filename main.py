from bs4 import BeautifulSoup
import tkinter as tk

def on_button_click():
    user_input = entry.get()
    printTheCrashingIssue(user_input)


def printTheCrashingIssue(tableHtml):
    # 使用lxml解析器解析HTML
    soup = BeautifulSoup(tableHtml, 'lxml')

    # 找到所有的<tr>标签
    table = soup.find('table')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for index, row in enumerate(rows, start=1):
        title_text = ""

        title = row.find('div', {'class': 'title-wrapper'})

        event_cell = row.find_all('td')[3]
        event_text = event_cell.get_text(strip=True)

        version_cell = row.find_all('td')[2]

        if title is not None:
            title_text = title.get_text(strip=True)

        if version_cell:
            version_span_element = version_cell.find('span', class_='mat-mdc-tooltip-trigger')
            if version_span_element:
                version_text = version_span_element.get_text(strip=True)

                print(f"{index}. {title_text} {event_text} 影響版本 {version_text}")

        if index == 3:
            break

# 创建主窗口
root = tk.Tk()
root.title("输入窗口示例")
# 设置窗口的宽度和高度
root.geometry("1080x720")  # 设置宽度为400像素，高度为200像素
# 创建一个标签
label = tk.Label(root, text="请输入你的信息：")
label.pack()

# 创建一个输入框
entry = tk.Entry(root)
entry.pack(fill="both", expand=True,padx=50, pady=50)

# 创建一个按钮
button = tk.Button(root, text="确定", command=on_button_click)
button.pack()

# 启动主事件循环
root.mainloop()
