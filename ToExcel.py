import openpyxl

# Создаем новую книгу Excel
workbook = openpyxl.Workbook()

# Выбираем активный лист
sheet = workbook.active

# Ваш Python код, который вы хотите записать в Excel
python_code = """
def hello_world():
    print("Hello, World!")

hello_world()
"""

# Записываем код в ячейку A1
sheet['A1'] = python_code

# Указываем путь для сохранения файла
file_path = "/полный/путь/к/вашему/файлу/python_code.xlsx"

# Сохраняем книгу Excel по указанному пути
workbook.save(file_path)

print("Python код сохранен в Excel файле по пути:", file_path)
