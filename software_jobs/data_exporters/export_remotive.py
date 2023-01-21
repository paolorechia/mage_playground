import datetime as dt
from mage_ai.io.file import FileIO
from pandas import DataFrame
from software_jobs.utils.path_utils import get_today_remotive_path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to filesystem.

    Docs: https://docs.mage.ai/design/data-loa  ding
    """
    filepath = get_today_remotive_path()
    FileIO().export(df, filepath)


@test
def test_output():
    df = FileIO().load(get_today_remotive_path())
    assert len(df.index) > 5