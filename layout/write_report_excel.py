from excel_features import ExcelFileControl

from layout.write_main_header import write_main_header
from layout.write_tables import write_tables


def write_report_excel(input_file_name: str, output_file_name: str):
    """ Записывает файл отчета. Готовит файл для вывода. """

    grid: bool = False
    output = ExcelFileControl(output_file_name)
    with output as ex:
        sheets_name = ["report", "stat"]
        ex.create_sheets(sheets_name)
        output_sheet = ex.get_sheet(sheets_name[0])
        ex.set_grid(sheets_name[0], grid=grid)
        write_main_header(output_sheet)

        write_tables(input_file_name, output_sheet, start_line=4)  #, tables_limit=3
