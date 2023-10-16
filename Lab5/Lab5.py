import psycopg2
import psycopg2.extras
import csv
import re

conn = psycopg2.connect(host="cc3201.dcc.uchile.cl",
                        database="cc3201",
                        user="cc3201",
                        password="j'<3_cc3201", 
                        port="5440")

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
        powerstats = row[2:8] # int, str, speed, dur, power, combat
        biography_notaliases = row[8:10] + row[11:15] # full name, alter egos, place of birth, first appearance, publisher, alignment
        biography_aliases = [row[10]] + row[27:46] # aliases 1 through 20
        appearance = row[15:23] # gender, race, height_in, height_cm, weight_lb, weight_kg, eye color, hair color
        work = row[23:25] # occupation, base
        connections = row[25:27] # group affiliation, relatives

    conn.commit()

conn.close()