# POS-to-Shopify

Imports sales from POS and syncs with Shopify CSV inventory.

## Features

* Prints which row was changed and total number of changes
* One-click solution after setup

## Installation

1) Create a SyncINV folder in C:\ and add the bat and py files to it

2) Edit syncData.bat and change the "C:\Program Files\Python37\python.exe" to wherever your python.exe is.

## Usage

1) Drop ddsMMDD.xls from POS and inventory_export_MMDD.csv from Shopify into SyncINV

2) Run syncData.bat

3) Export inventory_export_u.csv to Shopify

/!\ WARNING /!\ Program must be run THAT DAY since the MMDD dates are compared using the computer's date.

## Current Issues

* syncData.py is not very portable. User may have to edit lines 15 and 16 to fit their personal needs.
* Iterates twice over both excel files, leading to long computation times. Worsens the longer the excel files are.
