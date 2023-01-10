import pandas as pd

def conn_pool_to_google_spreadsheet(sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&id={sheet_id}&gid=1682433394'


def test_conn_pool_to_google_is_ok():

    sheet_id= '1mbyk0OfajYo2owwcmVTXuVGIIVeHj4eINZldPiSNNoU'
    url = conn_pool_to_google_spreadsheet(sheet_id=sheet_id)

    df = pd.read_csv(url, encoding='utf8')

    assert len(df) != 0
