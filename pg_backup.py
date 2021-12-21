# import psycopg2
# import sys
# from psycopg2 import sql
#
# connection = psycopg2.connect(user="doadmin",
#                               password="u81v0mi6yh4c7h4u",
#                               host="yogiassociatesdb-do-user-4783558-0.a.db.ondigitalocean.com",
#                               port="25060",
#                               database="ya_database")
# cursor = connection.cursor()
# print(connection.get_dsn_parameters(), "\n")
# col_names_str = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE "
# col_names_str += "table_name = '{}';".format('panel_contacts')
# columns = []
# # print the SQL string
# print("\ncol_names_str:", col_names_str)
# sql_object = sql.SQL(
#     # pass SQL statement to sql.SQL() method
#     col_names_str
# ).format(
#     # pass the identifier to the Identifier() method
#     sql.Identifier('panel_codes')
# )
# # execute the SQL string to get list with col names in a tuple
# cursor.execute(sql_object)
#
# # get the tuple element from the liast
# col_names = (cursor.fetchall())
#
# # print list of tuples with column names
# # print("\ncol_names:", col_names)
# # iterate list of tuples and grab first element
# for tup in col_names:
#     # append the col name string to the list
#     columns += [tup[0]]
#
# print(columns)
#


# !python

import subprocess
import os
import glob
import time

# change these as appropriate for your platform/environment :
USER = "doadmin"
PASS = "u81v0mi6yh4c7h4u"
HOST = "yogiassociatesdb-do-user-4783558-0.a.db.ondigitalocean.com"
DB = "ya_database"
port = "25060"
command = "PGPASSWORD=j9xwaimz5o4ujvue pg_dump -U doadmin -h prdb-do-user-4783558-0.b.db.ondigitalocean.com -p 25060 -d ya_database --file /Users/junaidtariq/PycharmProjects/TeeserAct/07-10-2021.sql"
os.system(command)


# lscra6gncje824j app key
# phg7moy3snp4pci app secret key
# liifgMMYRkUAAAAAAAAAAQnhEnwjFsWmp_ZiAOgXp4cxA6fpYN5nkP8vHK-Fvuhp access token


# username = doadmin
# password = j9xwaimz5o4ujvue hide
# host = prdb-do-user-4783558-0.b.db.ondigitalocean.com
# port = 25060
# database = defaultdb
# sslmode = require