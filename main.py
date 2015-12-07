
from HandleFiles import HandleFiles
from DbHelper import DbHelper

path = raw_input('HandleFiles in Path : ')

a = HandleFiles()
b = DbHelper()

b.create_table_on_db()
a.scan_for_files_with_extension(path)


file = a.get_file()

files = file.split(" - ")


for file in files:
    if not file: continue
    b.insert_value_in_table(file)
