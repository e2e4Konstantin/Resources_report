import argparse
import pathlib


def get_arguments() -> str:
    """ Получает из командной строки имя файла с данными и проверяет его наличие"""
    parser = argparse.ArgumentParser(prog="pars", description="разбор файла с расценками на группы",
                                     epilog=f"Спасибо что используете 'pars':)")
    parser.add_argument("data_file")
    args = parser.parse_args()
    # print(args)
    file = pathlib.Path(args.data_file)
    # print(file.name, file.cwd(), file.absolute(), type(file.absolute()))
    if not file.exists():
        print(f"файл: {file.name!r} не найден.")
        raise SystemExit(1)
    return str(file.absolute())
