import os
import sqlite3


class DataBase:
    def __extract_pt(strPt1, strPt2):
        x1 = int(strPt1.split()[0][1:-1])
        y1 = int(strPt1.split()[1][:-1])
        x2 = int(strPt2.split()[0][1:-1])
        y2 = int(strPt2.split()[1][:-1])
        return (x1, y1), (x2, y2)

    @staticmethod
    def first_con():
        path = "./db"
        isExist = os.path.exists(path)

        if not isExist:
            os.makedirs(path)

        connection = sqlite3.connect("./db/annotations.db")
        connection.execute(
            """CREATE TABLE IF NOT EXISTS 'ANNOTATIONS' (
                'FILE_PATH'	TEXT NOT NULL,
                'LABEL_ID'	INTEGER NOT NULL,
                'LABEL'	TEXT NOT NULL,
                'PT1'	BLOB NOT NULL,
                'PT2'	BLOB NOT NULL);"""
        )
        connection.close()

    @classmethod
    def pull_data(cls, filePath):
        connection = sqlite3.connect("./db/annotations.db")
        cursor = connection.execute(
            f"""SELECT * FROM ANNOTATIONS WHERE FILE_PATH = '{filePath}'"""
        )

        stagingMem = []
        for row in cursor:
            labelID = row[1]
            label = row[2]
            pt1, pt2 = cls.__extract_pt(row[3], row[4])
            stagingMem.append([labelID, label, pt1, pt2])

        connection.close()
        return stagingMem.copy()

    @staticmethod
    def sync_db(filePath, stagingMem):
        connection = sqlite3.connect("./db/annotations.db")
        connection.execute(
            f"""DELETE FROM ANNOTATIONS WHERE FILE_PATH = '{filePath}'"""
        )

        for annot in stagingMem:
            labelID = annot[0]
            label = annot[1]
            pt1 = annot[2]
            pt2 = annot[3]

            connection.execute(
                f"""INSERT INTO ANNOTATIONS(FILE_PATH,LABEL_ID,LABEL,PT1,PT2) 
                VALUES('{filePath}','{labelID}','{label}','{pt1}','{pt2}')"""
            )

        connection.commit()
        connection.close()

    @classmethod
    def pull_all_annot(cls):
        connection = sqlite3.connect("./db/annotations.db")
        cursor = connection.execute("SELECT * FROM ANNOTATIONS")

        stagingMem = []
        for row in cursor:
            filePath = row[0]
            labelID = row[1]
            label = row[2]
            pt1, pt2 = cls.__extract_pt(row[3], row[4])
            stagingMem.append([filePath, labelID, label, pt1, pt2])

        connection.close()
        return stagingMem.copy()
