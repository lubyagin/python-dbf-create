#!/usr/bin/python
# -*- coding: utf-8 -*-

from dbfpy import dbf

# Определяем набор полей файла. C — строка, N — число, D — дата, L — булево.
# Для строк нужно указать длину, для чисел — количество разрядов целой и дробной частей.
SCHEMA = (
    ("ID",         "N", 12, 0),
    ("NAME",       "C", 64   ),
    ("DATE",       "D"       ),
    ("FLAG",       "L"       ),
)

db = dbf.Dbf("dbfile.dbf", new=True)
db.addField(*SCHEMA)

# Обходим в цикле данные, которые необходимо записать в DBF.
# На каждом шаге цикла создается новая запись и заполняются ее поля.

rec = db.newRecord()
import datetime

rec["ID"] = 1
rec["NAME"] = u"Имя".encode("cp866")
rec["DATE"] = datetime.datetime.now()
rec["FLAG"] = True

# Сохранение записи.
rec.store()

db.close()
