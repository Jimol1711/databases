import psycopg2
import psycopg2.extras
import csv
import re

conn = psycopg2.connect(host=" cc3201 .dcc . uchile .cl",
                        database=" cc3201 ",
                        user=" cc3201 ",
                        password="j'<3_cc3201 ", 
                        port=" 5440 ")

cursor = conn.cursor()

with open("Laboratorio_05_data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        id = row[0]
        name = row[1]
        powerstats = [row[2],row[3],row[4],row[5],row[6],row[7]] # int, str, speed, dur, power, combat
        biography_notaliases = [row[8],row[9],row[11],row[12],row[13],row[14]] # full name, alter egos, place of birth, first appearance, publisher, alignment


    conn.commit()

conn.close()