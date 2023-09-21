from file_features import handle_location

from layout import write_report_excel


def get_source_location(point_number: int, data_file_number: int):
    location = {1: "home", 2: "office"}

    data_place = {
        'office':   r"C:\Users\kazak.ke\Documents\Задачи\5_Fixed_Templates_07-09-2023\output",
        'home':     r"F:\Kazak\GoogleDrive\1_KK\Job_CNAC\1_targets\SRC\11-09-2023\output_1"
    }
    source_data = {
        1: {"file_name": r"Статистика_1_13 Оборудование_output.xlsx", "sheet_name": "Tables"},
        2: {"file_name": r"Статистика_1_13 Ресурсы_output.xlsx", "sheet_name": "Tables"}
    }
    return (data_place[location[point_number]],
            source_data[data_file_number]["file_name"],
            source_data[data_file_number]["sheet_name"])


if __name__ == "__main__":

    path, file, sheet = get_source_location(point_number=2, data_file_number=2)
    input_file, output_file = handle_location(data_path=path, data_file=file)
    # print(f"файл с данными: {input_file!r}\nназвание листа: {sheet!r}\nфайл результата: {output_file!r}\n")

    write_report_excel(input_file, output_file)





