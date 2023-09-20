
from excel_features import ExcelFileControl

from layout.write_main_header import write_main_header
from layout.write_tables import write_tables


def write_report_excel(input_file_name: str, output_file_name: str):
    """ Записывает файл отчета. """


    grid: bool = False
    output = ExcelFileControl(output_file_name)
    with output as ex:
        sheets_name = ["report", "stat"]
        ex.create_sheets(sheets_name)
        worksheet = ex.get_sheet(sheets_name[0])
        ex.set_grid(sheets_name[0], grid=grid)
        write_main_header(worksheet)

        write_tables(input_file_name, worksheet, start_line=4 ) # tables_limit=5




