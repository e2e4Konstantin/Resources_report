import gc

from pandas import DataFrame, isna
from openpyxl.worksheet import worksheet
from openpyxl.utils.cell import column_index_from_string

from data_frame_features import read_data_frame, info_data_frame, filter_data_frame
from file_features.message import output_message

def write_resources_table(input_file_name: str, sheet: worksheet, start_line: int, table_code: str) -> int:
    """
    Записывает информацию о ресурсах для указанной таблицы.
    :param input_file_name: Имя фала с данными.
    :param sheet: Лист, на который выводить данные.
    :param start_line: Строка с которой надо начинить запись.
    :param table_code: Шифр таблицы.
    """
    worksheet_name = 'Resources'
    resources_df: DataFrame = read_data_frame(input_file_name, sheet_name=worksheet_name)
    info_data_frame(resources_df, mode='short')
    resources_df = filter_data_frame(resources_df, 'I', table_code)
    # (src_df: DataFrame, column_name: str, target: str)





    if not resources_df.empty:
        pass
        # if 0 < tables_limit < len(table_df.index):
        #     table_df = table_df.loc[:tables_limit]
        # row = start_line
        # for table in table_df.to_records(index=False):
        #     row = _table_line_output(table, sheet, row=row) + 1
        #     # row = ы(input_file_name, sheet, start_line=row, code=table['C'])
    else:
        output_message(f"пустой файл: {input_file_name!r}",
                       f"нет ни одного ресурса на листе {worksheet_name!r} для таблицы {table_code!r}.")
    del resources_df
    gc.collect()
