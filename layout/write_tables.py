from pandas import DataFrame, isna
import numpy
from openpyxl.worksheet import worksheet
from openpyxl.utils.cell import column_index_from_string

from data_frame_features import read_data_frame, info_data_frame
from file_features.message import output_message

from layout.layout_setting import headers, width_columns, items_styles


def _set_style(sheet: worksheet, row: int, column: int, style_name: str):
    sheet.cell(row=row, column=column).font = items_styles[style_name]['font']
    sheet.cell(row=row, column=column).fill = items_styles[style_name]['fill']
    sheet.cell(row=row, column=column).border = items_styles[style_name]['border']


def _attributes_output(src_attributes: str, start_column: int, sheet: worksheet, row: int) -> int:
    if not isna(src_attributes):
        sheet.cell(row=row, column=start_column).value = headers['attribute'][0]
        for column in range(start_column, start_column + len(headers["attribute"])):
            _set_style(sheet, row, column, 'attributes_header')

        attributes = src_attributes.split(',')
        attributes_length = len(attributes)
        for i, attribute in enumerate(attributes):
            column = start_column + i
            sheet.cell(row=row + 1, column=column).value = attribute
            _set_style(sheet, row + 1, column, 'attributes_volume')
            _set_style(sheet, row, column, 'attributes_header')

        if attributes_length > 1:
            sheet.merge_cells(start_row=row, start_column=start_column,
                              end_row=row, end_column=start_column + attributes_length - 1)
        return start_column + attributes_length
    return start_column


def _parameters_output(src_parameters: str, start_column: int, sheet: worksheet, row: int):
    if not isna(src_parameters):
        parameters = src_parameters.split(',')
        # print(parameters)
        parameters_length = len(parameters)
        if parameters_length > 0:
            mini_table_header = headers['option']  # таблица: 'от', 'до', 'ед.изм.', 'шаг', 'тип'
            parameter_tile_length = len(mini_table_header)
            column = start_column
            for parameter in parameters:
                sheet.cell(row=row, column=column).value = parameter  # название параметра
                _set_style(sheet, row, column, 'parameter_title')

                for i, item in enumerate(mini_table_header):
                    sheet.cell(row=row + 1, column=column + i).value = item
                    _set_style(sheet, row + 1, column + i, 'parameter_table')

                column_delta = parameter_tile_length - 1
                sheet.merge_cells(start_row=row, start_column=column, end_row=row, end_column=column + column_delta)
                column += column_delta + 1


def _table_line_output(table_info: numpy.record, sheet: worksheet, row: int) -> int:
    if table_info:
        sheet.cell(row=row, column=column_index_from_string('C')).value = table_info['C']
        for column in range(1, len(headers["table"]) + 1):
            sheet.cell(row=row, column=column).font = items_styles['table']['font']
            sheet.cell(row=row, column=column).fill = items_styles['table']['fill']
            sheet.cell(row=row, column=column).border = items_styles['table']['border_up']

            sheet.cell(row=row + 1, column=column).font = items_styles['table']['font']
            sheet.cell(row=row + 1, column=column).fill = items_styles['table']['fill']
            sheet.cell(row=row + 1, column=column).border = items_styles['table']['border_down']

        column_h = column_index_from_string('H')
        end_attributes_column = _attributes_output(table_info['G'], start_column=column_h, sheet=sheet, row=row)

        _parameters_output(table_info['H'], end_attributes_column, sheet, row)

        sheet.row_dimensions[row].height = 12
        sheet.row_dimensions[row + 1].height = 12
        return row + 2
    return row


def write_tables(input_file_name: str, sheet: worksheet, start_line: int, tables_limit: int = 0):
    """
    Записывает информацию о таблицах.
    :param input_file_name: Имя фала с данными.
    :param sheet: Лист, на который выводить данные.
    :param start_line: Строка с которой надо начинить запись.
    :param tables_limit: Сколько таблиц выводить.
    """
    worksheet_name = 'Tables'
    table_df: DataFrame = read_data_frame(input_file_name, sheet_name=worksheet_name)
    info_data_frame(table_df, mode='short')
    if not table_df.empty:
        if 0 < tables_limit < len(table_df.index):
            table_df = table_df.loc[:tables_limit]
        row = start_line
        for table in table_df.to_records(index=False):
            row = _table_line_output(table, sheet, row=row) + 1
            # row = resource_output(sheet, df_res, row, chapter=table)
    else:
        output_message(f"пустой файл: {input_file_name!r}",
                       f"нет ни одной таблицы на листе {worksheet_name!r}.")
