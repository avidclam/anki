import pandas as pd
from .config import Config


ingest_columns = [
    'sign', 'article', 'left', 'word', 'meaning', 'right', 'stem', 'plural',
    'present', 'perfect', 'translation', 'reverse', 'example', 'topic'
]


def load_dataset(cfg: Config) -> pd.DataFrame:
    file_path = cfg.get_path('ingest.file_path')
    sep = cfg.get_path('ingest.sep')
    column_mapping = cfg.get_path('ingest.column_mapping', None)
    in_df = pd.read_csv(file_path, sep=sep, dtype='string', na_filter=False)
    df = in_df.map(str.strip)
    if column_mapping:
        df = df.rename(columns=column_mapping)
    else:
        df = df.iloc[:, :len(ingest_columns)]  # Limit columns
        df.columns = ingest_columns  # Rename columns
    return df