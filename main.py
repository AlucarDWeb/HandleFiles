
from HandleFiles import HandleFiles
from DbHelper import DbHelper

path = raw_input('HandleFiles in Path : ')
ext = raw_input('Format: ' )


a = HandleFiles()
b = DbHelper()

b.create_table_on_db()

if not ext:

    a.scan_for_files(path)

else:
    a.scan_for_files_with_extension(path,ext)


file = a.get_file()

files = file.split(" - ")


for file in files:
    if not file: continue
    b.insert_value_in_table(file)
