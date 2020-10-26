@echo off

:: Renames ddsMMDD.xls to dds.xls
ren dds%date:~-10,2%%date:~-7,2%.xls dds.xls

:: Renames inventory_export_MMDD.csv to inventory_export.csv
ren inventory_export_%date:~-10,2%%date:~-7,2%.csv inventory_export.csv

"C:\Program Files\Python37\python.exe" "C:\SyncINV\syncData.py"

PAUSE 