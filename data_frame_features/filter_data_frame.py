from pandas import DataFrame
from file_features.message import output_message_exit, output_message


def filter_data_frame(src_df: DataFrame, column_name: str, target: str) -> DataFrame:
    if not src_df.empty:
        if column_name in src_df.columns:
            df = src_df[src_df[column_name].str.contains(pat=target, case=False, regex=False)]
            print(f"{target}\nв df: {len(df.to_records(index=False).tolist())} позиций")
            return df
        else:
            output_message_exit(f"в DataFrame нет колонки с названием:", column_name)
    else:
        output_message(f"в DataFrame нет данных:", f"{src_df.info(verbose=False, memory_usage='deep', show_counts=True)}")
    return src_df


