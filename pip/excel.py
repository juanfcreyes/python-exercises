import tablib 
# create a dataset
data = tablib.Dataset()
# Add rows
data.append(["A", 1])
data.append(["B", 2])
data.append(["C", 3])

print(data)
# save as csv
with open('test.csv', 'wb') as f:
    f.write(bytearray(data.export('csv').encode('utf8')))

# save as Excel
with open('test.xls', 'wb') as f:
    f.write(bytearray(data.export('xls')))

# save as Excel 07+
with open('test.xlsx', 'wb') as f:
    f.write(bytearray(data.export('xlsx')))

sheet1 = tablib.Dataset()
sheet1.append(["A1", 1])
sheet1.append(["A2", 2])

sheet2 = tablib.Dataset()
sheet2.append(["B1", 1])
sheet2.append(["B2", 2])


book = tablib.Databook([sheet1, sheet2])
with open('book.xlsx', 'wb') as f:
    f.write(book.xlsx)
