

import os



class HandleFiles:

    def scan_for_files_with_extension(self, path, ext):

        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith ('.{0}'.format(ext)):
                    with open("temp.txt", "a") as list_text_file:
                        list_text_file.write(" - {0}".format(name))



    def scan_for_files(self, path):

        for root, dirs, files in os.walk(path):
            for name in files:
                    with open("temp.txt", "a") as list_text_file:
                        list_text_file.write(" - {0}".format(name))


    def get_file(self):

        with open ("temp.txt", "r") as file:
            data = file.read()
            os.remove('temp.txt')
            return data
