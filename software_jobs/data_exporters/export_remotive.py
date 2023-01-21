import datetime as dt
from mage_ai.io.file import FileIO
from pandas import DataFrame
from software_jobs.utils.date_utils import get_today_string

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loa  ding
    """
    now = get_today_string()
    filepath = f'/data/{now}_remotive.json'
    FileIO().export(df, filepath)
