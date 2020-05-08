"""
操作excel
安装xlwt库 'pip3 install xlwt'
安装xlrd库 'pip3 install xlrd'
安装xlutils库 'pip3 install xlutils'
"""

import xlwt
import xlrd
from xlutils.copy import copy


def write_excel():
    # 只能写不能读
    text = [['姓名', '性别', '班级', '分数'],
            ['mary', '女', '1班', 89],
            ['tom', '男', '4班', 99],
            ['jack', '男', '2班', 90],
            ['rose', '女', '3班', 78]
            ]
    # 新建一个excel
    book = xlwt.Workbook()
    # 添加一个sheet页
    sheet = book.add_sheet('sheet1')
    # 控制行
    row = 0
    for stu in text:
        # 控制列
        col = 0
        # 再循环里面list的值，每一列
        for s in stu:
            sheet.write(row, col, s)
            col += 1
        row += 1
    # 保存
    book.save('/Users/mac/Documents/Python/file/stu_achievement.xls')


def read_excel():
    # 只能读不能写
    # 打开一个excel
    book = xlrd.open_workbook('/Users/mac/Documents/Python/file/stu_achievement.xls')
    # 根据顺序获取sheet
    sheet = book.sheet_by_index(0)
    # 根据sheet页名字获取sheet
    # sheet1 = book.sheet_by_name('sheet1')
    # 指定行和列获取数据
    print(sheet.cell(0, 0).value)
    print(sheet.cell(0, 1).value)
    print(sheet.cell(0, 2).value)
    print(sheet.cell(0, 3).value)
    # 获取excel里面有多少列
    print(sheet.ncols)
    # 获取excel里面有多少行
    print(sheet.nrows)
    print(sheet.get_rows())
    for i in sheet.get_rows():
        # 获取每一行的数据
        print(i)
    # 获取第一行
    print(sheet.row_values(0))
    # 0 1 2 3 4 5
    for i in range(sheet.nrows):
        # 获取第几行的数据
        print(sheet.row_values(i))

    # 取第一列的数据
    print(sheet.col_values(1))
    for i in range(sheet.ncols):
        # 获取第几列的数据
        print(sheet.col_values(i))


def update_excel():
    # 修改excel
    book1 = xlrd.open_workbook('/Users/mac/Documents/Python/file/stu_achievement.xls')
    # 拷贝一份原来的excel
    book2 = copy(book1)
    # print(dir(book2))
    # 获取第几个sheet页
    sheet = book2.get_sheet(0)
    sheet.write(1, 3, 0)
    sheet.write(1, 0, 'hello')
    book2.save('/Users/mac/Documents/Python/file/stu_achievement.xls')


write_excel()
# read_excel()
# update_excel()
