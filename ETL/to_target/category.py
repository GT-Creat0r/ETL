from ETL.library.Database import Database
from ETL.library.Logger import Logger
from ETL.library.Variables import Variables

TABLE_NAME = 'D_RETAIL_CTGRY_T'
TGT_DB_NAME = Variables.get_variable('DB_TGT')
TEMP_DB_NAME = Variables.get_variable('DB_TEMP')
truncate_query = f"""
TRUNCATE TABLE {TGT_DB_NAME}.{TABLE_NAME};
"""
insert_query = f"""
INSERT INTO {TGT_DB_NAME}.{TABLE_NAME} (CTGRY_ID, CTGRY_DESC, Row_INSRT_TMS, Row_UPDT_TMS)
        SELECT 
            ID, 
            CATEGORY_DESC,
            CURRENT_TIMESTAMP as row_insrt_tms,
            CURRENT_TIMESTAMP as row_updt_tms
FROM {TEMP_DB_NAME}.CATEGORY;
"""

def load_category_to_tgt():
    db = Database(Logger('test_logs'))
    db.execute_query(truncate_query)
    db.execute_query(insert_query)
    db.disconnect()