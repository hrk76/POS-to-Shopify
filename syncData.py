import pandas as pd

storeSales = pd.read_excel(r'C:\SyncINV\dds.xls')
shopifyInventory = pd.read_csv(r'C:\SyncINV\inventory_export.csv')

changeCounter = 0

for storeRow in range(len(storeSales.index)):
    for shopifyRow in range(len(shopifyInventory.index)):

        if storeSales.loc[storeRow][0] == shopifyInventory.loc[shopifyRow][8]:
            shopifyInventory.iloc[shopifyRow,11] -= storeSales.iloc[storeRow,4]
            print("Row", shopifyRow + 2, "changed")
            changeCounter += 1

shopifyInventory.to_csv('C:\SyncINV\inventory_export_u.csv')

print(changeCounter, "changes made")
