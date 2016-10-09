import os
import os.path
import subprocess
import shutil
import modules.scanDir as sD

# Scans Files in input_path, if files with file_extensions are not in subfolder, 
# then create subfolder with same name as movie and move movie into the subfolder
def PutNakedMoviesInFolders(input_path, file_extensions):

  move_counter = 0 # counter for moved files

  # file extensions to search for
  file_extensions = ['avi', 'dat', 'mp4', 'mkv', 'vob', 'flv']

  found_movies_path = "dir.files.txt" # write the path of the naked movie files to 

  # search for files in input_path without looking into subfolders AND write all found files to scan_file_path
  sD.ScanDir('only', file_extensions, input_path, found_movies_path)

  # read .txt file with found movies line by line, create folder and move movies into folder
  with open(found_movies_path) as f:
    for movie_path in f:
      movie_path = movie_path.rstrip() # delete newline and whitespaces from the end of the string
      folder_path = CutOffFileExtension(movie_path)
      #print("Create directory: " + folder_path)
      os.makedirs(folder_path) # create folder with the same name as movie
      shutil.move(movie_path, folder_path) #move movie into newly created folder
      #print("move " + movie_path + "to " + folder_path)
      move_counter += 1

  f.close()

  print("Files moved to folders: " + str(move_counter) + " files")
  

def CutOffFileExtension(movie_path):
  char = "." 
  char_pos = movie_path.rfind(char)  # from the end of the string find the position of the char
  folder_path = movie_path[0:char_pos]  # remove file extension
  folder_path = folder_path + "/"
  return folder_path


#ONLY FOR DEBUGGING
#def main():
#  input_path = "/test/input/path"
#
#  PutNakedMoviesInFolders(input_path)

#main()
