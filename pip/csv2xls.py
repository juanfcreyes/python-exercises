import tablib 
import sys

if (len(sys.argv) < 3):
	raise Exception("Origin name and target name are required")

origin = sys.argv[1]
target = sys.argv[2]

with open(origin + ".csv", 'r') as fh:
    imported_data = tablib.Dataset().load(fh, headers=False)

with open(target + ".xls", 'wb') as r:
   r.write(bytearray(imported_data.export('xls')))