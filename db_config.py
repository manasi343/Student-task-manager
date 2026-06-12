import mysql.connector

def get_database_connection():

    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="2neVHHzmtXFu2aL.root",
        password="9iwaSofSBDwZVpAi",
        database="students_task_mng",
        port=4000
    )
    return connection