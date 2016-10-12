#Created on 08.10.2016

import os
import os.path
import modules.moveFilesToFolders as mFTF
import modules.utilityFunctions as uF

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
          print(filepath)
          file_counter += 1      
          print(str(file_counter))
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


# main function
def ScanDir(search_extensions, directory):

  global file_counter
  file_counter = 0 # counter for detected files with defined extensions

  #log files
  log_path = "logs/" # path to log files
  log_naked_files = log_path + "files.not.in.folders.txt"
  log_folder_files = log_path + "files.in.folders.txt"

  f_naked_files = open(log_naked_files, "w")
  f_folder_files = open(log_folder_files, "w")

  #Scan directory for files which are not in folders
  ScanDirForFiles(directory, f_naked_files, search_extensions)
  print("Files which are not in folders: \t" + str(file_counter) + " files " + "-> " + log_naked_files) #print number of detected files

   
  f_naked_files.close() #Close log_file for function below
  mFTF.PutNakedFilesInFolders(log_naked_files) #Move files which are not in folders to a folder with the same name as the file

 
  # Scan directory for all files, only files which are in subfolders are remaining
  file_counter = 0 #reset file_counter
  ScanDirForAllFiles(directory, f_folder_files, search_extensions)
  print("Files which are in folders: \t \t" + str(file_counter) + " files " + "-> " + log_folder_files) #print number of detected files
  print("Number of files to be processed: \t" + str(file_counter) + " files")
  f_folder_files.close()
  
  uF.StripFilename(log_folder_files, "logs/files.in.folders.stripped.txt")
  
