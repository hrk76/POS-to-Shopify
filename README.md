# POS-to-Shopify

Imports sales from POS and syncs with Shopify CSV inventory.

# Usage

1) Create a SyncINV folder in C:\ and add the bat and py files to it

2) Edit syncData.bat and change the "C:\Program Files\Python37\python.exe" to wherever your python.exe is.

3) Drop ddsMMDD.xls from POS and inventory_export_MMDD.csv from Shopify into SyncINV

4) Run syncData.bat

5) Export inventory_export_u.csv to Shopify
