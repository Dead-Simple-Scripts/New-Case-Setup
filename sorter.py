from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            new_name = filename
            extension = 'noname'
            try:
                extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                path = extensions_folders[extension]
            except Exception:
                        extension = 'noname'
            folder_destination_path = extensions_folders[extension]

            file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
            while file_exists:
                i += 1
                new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                new_name = new_name.split("/")[4]
                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
            src = folder_to_track + "/" + filename

            new_name = folder_destination_path + "/" + new_name
            os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "C:\\Analysis\\placeholder1\\uncat",
#Text
    '.txt' : "C:\\Analysis\\placeholder1\\text",
    '.odt ' : "C:\\Analysis\\placeholder1\\text",
    '.rtf': "C:\\Analysis\\placeholder1\\text",
    '.tex': "C:\\Analysis\\placeholder1\\text",
    '.wks ': "C:\\Analysis\\placeholder1\\text",
    '.wps': "C:\\Analysis\\placeholder1\\text",
    '.wpd': "C:\\Analysis\\placeholder1\\text",
#Word
    '.doc' : "C:\\Analysis\\placeholder1\\word",
    '.docx' : "C:\\Analysis\\placeholder1\\word",
#PDF
    '.pdf': "C:\\Analysis\\placeholder1\\pdf",
#Pictures
    '.ai': "C:\\Analysis\\placeholder1\\pictures",
    '.bmp': "C:\\Analysis\\placeholder1\\pictures",
    '.gif': "C:\\Analysis\\placeholder1\\pictures",
    '.ico': "C:\\Analysis\\placeholder1\\pictures",
    '.jpg': "C:\\Analysis\\placeholder1\\pictures",
    '.jpeg': "C:\\Analysis\\placeholder1\\pictures",
    '.png': "C:\\Analysis\\placeholder1\\pictures",
    '.ps': "C:\\Analysis\\placeholder1\\pictures",
    '.psd': "C:\\Analysis\\placeholder1\\pictures",
    '.svg': "C:\\Analysis\\placeholder1\\pictures",
    '.tif': "C:\\Analysis\\placeholder1\\pictures",
    '.tiff': "C:\\Analysis\\placeholder1\\pictures",
    '.CR2': "C:\\Analysis\\placeholder1\\pictures",
#Compressed
    '.7z': "C:\\Analysis\\placeholder1\\compressed",
    '.arj': "C:\\Analysis\\placeholder1\\compressed",
    '.deb': "C:\\Analysis\\placeholder1\\compressed",
    '.pkg': "C:\\Analysis\\placeholder1\\compressed",
    '.rar': "C:\\Analysis\\placeholder1\\compressed",
    '.rpm': "C:\\Analysis\\placeholder1\\compressed",
    '.tar.gz': "C:\\Analysis\\placeholder1\\compressed",
    '.z': "C:\\Analysis\\placeholder1\\compressed",
    '.zip': "C:\\Analysis\\placeholder1\\compressed",
#Image
    '.bin': "C:\\Analysis\\placeholder1\\image",
    '.dmg': "C:\\Analysis\\placeholder1\\image",
    '.iso': "C:\\Analysis\\placeholder1\\image",
    '.toast': "C:\\Analysis\\placeholder1\\image",
    '.vcd': "C:\\Analysis\\placeholder1\\image",
    '.raw': "C:\\Analysis\\placeholder1\\image",
    '.dmp': "C:\\Analysis\\placeholder1\\image",
    '.mem': "C:\\Analysis\\placeholder1\\image",
#Data
    '.csv': "C:\\Analysis\\placeholder1\\data",
    '.dat': "C:\\Analysis\\placeholder1\\data",
    '.db': "C:\\Analysis\\placeholder1\\data",
    '.dbf': "C:\\Analysis\\placeholder1\\data",
    '.mdb': "C:\\Analysis\\placeholder1\\data",
    '.sav': "C:\\Analysis\\placeholder1\\data",
    '.sql': "C:\\Analysis\\placeholder1\\data",
    '.tar': "C:\\Analysis\\placeholder1\\data",
    '.xml': "C:\\Analysis\\placeholder1\\data",
    '.json': "C:\\Analysis\\placeholder1\\data",
#logs
    '.log': "C:\\Analysis\\placeholder1\\logs",
    '.evtx': "C:\\Analysis\\placeholder1\\logs",
#Programming
    '.c': "C:\\Analysis\\placeholder1\\programming",
    '.class': "C:\\Analysis\\placeholder1\\programming",
    '.dart': "C:\\Analysis\\placeholder1\\programming",
    '.py': "C:\\Analysis\\placeholder1\\programming",
    '.sh': "C:\\Analysis\\placeholder1\\programming",
    '.swift': "C:\\Analysis\\placeholder1\\programming",
    '.html': "C:\\Analysis\\placeholder1\\programming",
    '.h': "C:\\Analysis\\placeholder1\\programming",
    '.bat': "C:\\Analysis\\placeholder1\\programming",
    '.ps1': "C:\\Analysis\\placeholder1\\programming",
#Spreadsheets
    '.ods' : "C:\\Analysis\\placeholder1\\spreadsheet",
    '.xlr' : "C:\\Analysis\\placeholder1\\spreadsheet",
    '.xls' : "C:\\Analysis\\placeholder1\\spreadsheet",
    '.xlsx' : "C:\\Analysis\\placeholder1\\spreadsheet",
}

folder_to_track = 'C:\\Users\\username\\Desktop\\placeholder1'
folder_destination = 'C:\\Analysis\\placeholder1'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
