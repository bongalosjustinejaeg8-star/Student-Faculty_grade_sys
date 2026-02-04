from openpyxl import Workbook, load_workbook

grades = "Sample Grades DB.xlsx"
wb1 = load_workbook(grades)
ws1 = wb1.active