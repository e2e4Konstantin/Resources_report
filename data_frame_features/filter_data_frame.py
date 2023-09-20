from pandas import DataFrame
from settings import its, ItemSet
from file_features.message import output_message_exit


def filter_data_frame(item_name: str, row_df: DataFrame) -> DataFrame | None:
    item: ItemSet = its[item_name]
    code = item.pattern
    column_name = item.column

    if column_name in row_df.columns:
        df = row_df[row_df[column_name].str.contains(pat=code, case=False, regex=True)]
        print(f"{its[item_name]}\nв df: {len(df.to_records(index=False).tolist())} позиций")
        return df
    else:
        output_message_exit(f"в dataframe нет колонки с таким названием:", column_name)
    return None

