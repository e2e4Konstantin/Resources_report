from openpyxl.worksheet import worksheet

from layout.layout_setting import headers, width_columns, items_styles


def write_main_header(sheet: worksheet):
    sheet.append(["."])
    sheet.append(headers["main"])
    for column in range(1, len(headers["main"]) + 1):
        sheet.cell(row=2, column=column).font = items_styles['main_header']['font']
        sheet.cell(row=2, column=column).fill = items_styles['main_header']['fill']
        sheet.cell(row=2, column=column).border = items_styles['main_header']['border']


    for width in width_columns:
        sheet.column_dimensions[width].width = width_columns[width]
