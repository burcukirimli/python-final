# -*- coding: utf-8 -*-
import pymysql.cursors
db = pymysql.connect(
    host ="localhost",
    user = "admin",
    password ="",
    db="ymk_trf_db",
    charset="utf8",
    cursorclass =pymysql.cursors.DictCursor)


baglanti = db.cursor()
baglanti.execute('SELECT * FROM yemek')
yemekler = baglanti.fetchall()

for i in yemekler:
    print("Yemek Ad: " + i['yemek_adi'] + " *** " + "Malzemeler: " + i['malzeme_adi'] + "Tarif: " + " *** " + i['tarif_adi'])








