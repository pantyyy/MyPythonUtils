"""
    作用 :
        根据指定列 , 读取excel表格数据

    参数:
        excel_obj : excel对象
        sheet_name : 表格名称
        row_num : 指定的列
        
    返回值:
        数组
"""
def read_excel_by_cols(excel_obj , sheet_name , row_num):

    # 根据名称获取表格
    table_obj = excel_obj.sheet_by_name(sheet_name)
    # 获取指定列的值 ， 返回数组
    col_list = table_obj.col_values(row_num)
    return col_list


"""
    作用 :
        根据指定列 , 读取excel表格数据

    参数:
        excel_obj : excel对象
        sheet_name : 表格名称
        row_num : 指定的列

    返回值:
        数组
"""
def read_excel_by_cols(excel_obj, sheet_name, row_num):
    # 根据名称获取表格
    table_obj = excel_obj.sheet_by_name(sheet_name)
    # 获取指定列的值 ， 返回数组
    col_list = table_obj.col_values(row_num)
    return col_list


"""
    作用 :
        根据指定行 , 读取excel表格数据

    参数:
        excel_obj : excel对象
        sheet_name : 表格名称
        col_num : 指定的行

    返回值:
        数组
"""
def read_excel_by_rows(excel_obj, sheet_name, col_num):
    # 根据名称获取表格
    table_obj = excel_obj.sheet_by_name(sheet_name)
    # 获取指定行的值 ， 返回数组
    row_list = table_obj.row_values(col_num)
    return row_list


"""
    作用 :
        根据指定坐标 , 读取excel表格数据

    参数:
        excel_obj : excel对象
        sheet_name : 表格名称
        col_num : 列位置
        row_num : 行位置

    返回值:
        字符串
"""
def read_excel_by_location(excel_obj, sheet_name, col_num , row_num):
    # 根据名称获取表格
    table_obj = excel_obj.sheet_by_name(sheet_name)
    data = table_obj.cell(col_num , row_num).value
    return data



"""
    作用 :
        根据指定行 , 写入数据

    参数:
        sheet : 表格对象
        data_list : 需要写入的数据
        row_num : 行位置
"""
def write_excel_by_rows(sheet, data_list , row_num):
    for i in range(0 , len(data_list)):
        sheet.write(row_num , i , data_list[i])


"""
    作用 :
        根据指定列 , 写入数据

    参数:
        sheet : 表格对象
        data_list : 需要写入的数据
        row_num : 列位置
"""
def write_excel_by_cols(sheet, data_list , col_num):
    for i in range(0 , len(data_list)):
        sheet.write(i , col_num , data_list[i])

"""
    作用 :
        根据指定坐标 , 写入数据

    参数:
        sheet : 表格对象
        data_list : 需要写入的数据
        row_num : 行位置
        col_num : 列位置
"""
def write_excel_by_location(sheet , data , row_num , col_num):
    sheet.write(row_num , col_num , data)