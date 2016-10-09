#Created on 08.10.2016

import os
import os.path

# Scan directory with all subfolders for files which are defined in array "search_extensions"
def ScanDirForAllFiles(directory, f, search_extensions):

  global file_counter

  # Get the absolute path of the directory parameter
  directory = os.path.abspath(directory)
 
  # Get a list of files in directory
  directory_files = os.listdir(directory)
 
  # Traverse through all detected files/folders
  for filename in directory_files:
    filepath = os.path.join(directory, filename) #concatenate directory-path with file/folder-name
    # Check if it's a normal file or directory
    if os.path.isfile(filepath):
      for search_extension in search_extensions:
        # if file doesn't end with extension continue
        if not filepath.endswith(search_extension):
          continue
        # if file does end with extension write to .txt-file
        else:
          f.write(filepath + "\n")
          file_counter += 1      

    elif os.path.isdir(filepath):
      # We got a directory, enter into it for further processing
      ScanDirForAllFiles(filepath, f, search_extensions)



# Scan directory (no subfolders) for files whith extensions which are defined in "search_extensions" 
# Creates a file called "dir.files.txt" in the directory from where the program is executed
def ScanDirForFiles(directory, f, search_extensions):

  global file_counter

  # Get the absolute path of the directory parameter
  directory = os.path.abspath(directory)

  # Get a list of files/folders in movie_directory
  directory_files = os.listdir(directory)
  
  # Traverse through all detected files/folders
  for filename in directory_files:
    filepath = os.path.join(directory, filename) #concatenate directory-path with file/folder-name
    # Check if it's a subfolder or a file with an extension
    if os.path.isfile(filepath):
      for search_extension in search_extensions:
        # if file doesn't end with extension continue
        if not filepath.endswith(search_extension):
          continue
        # if file does end with extension write to .txt-file
        else:
          f.write(filepath + "\n") # write detected file to .txt file
          file_counter += 1


# Handling function
def ScanDir(function, search_extensions, directory, log_path):
  global file_counter
  file_counter = 0 # counter for detected files with defined extensions

  f = open(log_path, "w")

  # scan directory only for files which are not in subfolders 
  if function == 'only':
    ScanDirForFiles(directory, f, search_extensions)
   # print(str(file_counter) + " files which are not in a folder detected and written to " + log_path) #print number of detected files
    print("Files which are not in folders: " + str(file_counter) + " files \t" + "(see " + log_path + ")" ) #print number of detected files
  # scan directory for all files
  if function == 'all':
    ScanDirForAllFiles(directory, f, search_extensions)
    print("Files which are not in folders: " + str(file_counter) + " files \t" + "(see " + log_path + ")" ) #print number of detected files
  
  f.close()


# For debugging only!!!!!!!!!!!!!
#def main():
#  directory = "/path/to/movie-files"
#  search_extensions = ['avi', 'dat', 'mp4', 'mkv', 'vob', 'flv']
  
#  ScanDir('all', search_extensions, directory)
#  ScanDir('only', search_extensions, directory)
  
#main()
