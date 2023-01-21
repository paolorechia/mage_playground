import datetime as dt
from mage_ai.io.file import FileIO
from pandas import DataFrame
from software_jobs.utils

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loading
    """
    now = dt.now()
    filepath = 'remotive_
    FileIO().export(df, filepath)
