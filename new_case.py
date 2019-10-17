import os
import shutil
import sys
import fileinput
import re


#enter case name to be used as file name
case_name = input("Enter case name: ")

#Copy case template to Analysis directory
os.chdir("C:\\Analysis\\scripts\\new_case_setup")
shutil.copytree("new_case_template","C:\\Analysis\\tempcasename")


#Make case directory on desktop
os.chdir("C:\\Users\\username\\Desktop")
os.mkdir(case_name)

#case name find\ replace in sort script
os.chdir("C:\\Analysis\\tempcasename")
sort_script = "sorter.py"
for line in fileinput.input(sort_script, inplace=1):
    folder_replace = re.sub('placeholder1',case_name,line.rstrip(),flags=re.I)
    print(folder_replace)

#bat file find\ replace to run sort script from desktop
bat = "4desktop.bat"
for line in fileinput.input(bat, inplace=1):
    bat_replace = re.sub('placeholder2',case_name,line.rstrip(),flags=re.I)
    print(bat_replace)

#move Bat file to Desktop
tmp_dir = "C:\\Analysis\\tempcasename"
desktop_dir = "C:\\Users\\username\\Desktop"

for root, dirs, files in os.walk((os.path.normpath(tmp_dir)), topdown=False):
    for name in files:
        if name.endswith('.bat'):
            SourceFolder = os.path.join(root,name)
            shutil.copy2(SourceFolder, desktop_dir) #copies file to target folder

#Rename Bat file
os.chdir("C:\\Users\\username\\Desktop")
os.rename("4desktop.bat",case_name + ".bat")

#Rename temp case folder to user supplied case name
os.chdir("C:\\Analysis")
os.rename("tempcasename",case_name)

exit()
