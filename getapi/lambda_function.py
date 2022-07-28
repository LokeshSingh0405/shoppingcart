import sys
import logging
#import rds_config
import pymysql
#rds settings
import json 
rds_host  = "shoppingcart.c4pojfvmsqfn.us-east-1.rds.amazonaws.com"
name = "admin"
password = "admin123"
db_name = "userdb"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, cursorclass=pymysql.cursors.DictCursor, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")
def lambda_handler(event, context):
    """
    This function fetches content from MySQL RDS instance
    
    """

    item_count = 0
    l=[]

    with conn.cursor() as cur:
        cur.execute("select * from User")
        for row in cur:
            l.append(row)
            item_count += 1
            logger.info(row)
    conn.commit()
    

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps(l)
    }