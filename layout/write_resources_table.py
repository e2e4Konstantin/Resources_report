import gc

from pandas import DataFrame, isna
import numpy

from openpyxl.worksheet import worksheet
from openpyxl.utils.cell import column_index_from_string

from data_frame_features.read_data_frame import read_data_frame
from data_frame_features.info_data_frame import info_data_frame
from data_frame_features.filter_data_frame import filter_data_frame
from file_features.message import output_message

from layout.set_cell_style import set_cell_style


def _resource_line_output(resource_info: numpy.record, sheet: worksheet, row: int) -> int:
    if resource_info:
        # x = resource_info.dtype.names[1:]
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(len(columns) - 1):
            sheet.cell(row=row, column=column_index_from_string(columns[i])).value = resource_info[columns[i+1]]
            set_cell_style(sheet, row, column_index_from_string(columns[i]), 'resource')
        sheet.row_dimensions[row].height = 12
        sheet.row_dimensions[row + 1].height = 12
        return row + 1
    return row


def



def write_resources_for_table(input_file_name: str, sheet: worksheet, start_line: int, table_code: str) -> int:
    """
    Записывает информацию о ресурсах для указанной таблицы.
    :param input_file_name: Имя фала с данными.
    :param sheet: Лист, на который надо выводить данные.
    :param start_line: Строка с которой надо начинить запись.
    :param table_code: Шифр таблицы.
    """
    resource_sheet_name = 'Resources'
    resources_df: DataFrame = read_data_frame(input_file_name, sheet_name=resource_sheet_name)
    column_name_code = "I"
    resources_df = filter_data_frame(resources_df, column_name_code, table_code)

    resource_sheet_name = 'Attributes'
    resources_df: DataFrame = read_data_frame(input_file_name, sheet_name=resource_sheet_name)
    column_name_code = "I"
    resources_df = filter_data_frame(resources_df, column_name_code, table_code)




    if not resources_df.empty:
        row = start_line
        for resource in resources_df.to_records(index=False):
            row = _resource_line_output(resource, sheet, row=row)
    else:
        output_message(f"пустой файл: {input_file_name!r}",
                       f"нет ни одного ресурса на листе {resource_sheet_name!r} для таблицы {table_code!r}.")
    del resources_df
    gc.collect()
    return row
