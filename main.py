# install OpenPyXl using "pip install openpyxl"

import openpyxl
from openpyxl import Workbook, load_workbook

# Load in your workbook

book = load_workbook('menuItems.xlsx')
sheet = book.active

print(sheet["A2"].value)

sheet["A2"].value = "tortellini"

book.save('new_menuItems.xlsx')