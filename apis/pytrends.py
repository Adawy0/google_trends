import os
from sqlalchemy import create_engine
import pandas as pd
#import the libraries                     
from pytrends.request import TrendReq

from .models import HistoricalInterestDataFrame, InterestByRegion

class GoogleTrends:
    """
    class define functionality of google trends requests
    """
    _pytrend = None
    _conn_string = None
    _connection = None

    def __init__(self):
        self._pytrend = TrendReq()
        self._conn_string = 'postgresql://{}:{}@{}/{}'.format(
            os.environ.get('POSTGRES_DB_USER'),
            os.environ.get('POSTGRES_DB_PASSWORD'),
            os.environ.get('POSTGRES_DB_HOST'),
            os.environ.get('POSTGRES_DB_NAME')
        )
        engine = create_engine(self._conn_string, echo = False)
        self._connection = engine.connect()

    def get_historical_interest(self, kw_list):
        try:
            historicaldf = self._pytrend.get_historical_interest(kw_list, year_start=2020, month_start=10, day_start=1, year_end=2021, month_end=10, day_end=1)
            historicaldf.insert(0, 'id', range(0, 0 + len(historicaldf)))
            historicaldf.to_sql(HistoricalInterestDataFrame._meta.db_table, self._connection, if_exists= 'replace')
            return historicaldf
        except Exception as e:
            raise Exception(e)

    def interest_by_region(self ,kw_list):
        try:
            self._pytrend.build_payload(kw_list=kw_list)
            df = self._pytrend.interest_by_region()
            df.insert(0, 'id', range(0, 0 + len(df)))
            df.to_sql(InterestByRegion._meta.db_table, self._connection, if_exists= 'replace')
            return df
        except Exception as e:
            raise Exception(e)
        