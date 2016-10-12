import os
import shutil
# Scans Files in file_path, if files with file_extensions are not in subfolder, 
# then create subfolder with same name as file and move file into the subfolder
def PutNakedFilesInFolders(file_path):

  move_counter = 0 # counter for moved files

  # read .txt file with found files line by line, create folder and move files into folder
  with open(file_path) as f:
    for file_path in f:
      file_path = file_path.rstrip() # delete newline and whitespaces from the end of the string
      folder_path = CutOffFileExtension(file_path)
      os.makedirs(folder_path) # create folder with the same name as file
      shutil.move(file_path, folder_path) #move file into newly created folder
      move_counter += 1

  f.close()

  print("Files moved to folders: \t \t" + str(move_counter) + " files")
  

def CutOffFileExtension(file_path):
  char = "." 
  char_pos = file_path.rfind(char)  # from the end of the string find the position of the char
  folder_path = file_path[0:char_pos]  # remove file extension
  folder_path = folder_path + "/"
  return folder_path