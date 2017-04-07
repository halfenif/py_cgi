import dbms
import cgi
import os
import sys
import base64

constDBMS = './../../../PycharmProjects/bigpicture_to_sqlite/output_dbms/db_bigpicture.db'
constSQLSelect = 'SELECT rawdata FROM tb_item WHERE seq = ?'

constHContentType = "Content-type: image/jpeg;\n"
constNewLine = "<BR>"

constBItem = "%s"


def selectItem():
    #Get Parameter
    #arguments = cgi.FieldStorage()

    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect, (2240,))

    for item in cur.fetchall():
        print("item TYPE name is {0}".format(type(item["rawdata"])))

        encodebytes = base64.b64encode(item["rawdata"])
        #print(encodebytes)

        print("encodebytes TYPE name is {0}".format(type(encodebytes)))

        decodedbytes = encodebytes.decode()

        print("decodedbytes TYPE name is {0}".format(type(decodedbytes)))

        print(decodedbytes)

        #print(item["rawdata"])
        #sys.stdout.buffer.write(item["rawdata"])

        #File Write
        # with open("test.jpg", "wb") as output_file:
        #     output_file.write(item["rawdata"])
        #     output_file.close()



    return


if __name__ == '__main__':
    print(constHContentType)
    selectItem()
