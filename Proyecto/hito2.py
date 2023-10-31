import psycopg2
import psycopg2.extras
import csv

try:
    conn = psycopg2.connect (host ="localhost",
                             database ="proyecto_cc3201",
                             user ="postgres",
                             password ="0123456789", 
                             port ="5432")
    
    cursor = conn.cursor()
except:
    print("No connection")

with open("MoviesOnStreamingPlatforms_updated.csv", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    i = 0
    for row in reader:
        i+=1
        if i==1:
            continue
        print(row)

    conn.commit()

conn.close()
