#!/usr/bin/python3.5

import os
import os.path
#from pathlib import Path
import subprocess
import modules.scanDir as sD
import modules.nakedMovies as nM

#reads the config-parameters from the config file
def ReadConfig(config_file, config_words):
  i = 0
    
  while i < len(config_words):
    config_word = config_words[i]
    content = SearchConfig(config_file, config_word)
    content = FormatConfigString(content)
    if i == 0:
      input_path = content
    if i == 1:
      output_path = content
    if i == 2:
      name_format = content
    if i == 3:
      database = content
    if i == 4:
      file_extensions = content

    i += 1

  return input_path, output_path, name_format, database, file_extensions
  
  
#searches the config file for each config-parameters and returns error if config-parameter is missing
def SearchConfig(config_file, config_word):
  
  config_content = ""
  
  #search for the config word
  with open(config_file) as f:
    for content in f: 
      if content.startswith(config_word):
        config_content = content
      else:
        continue 
  
  f.close()

  #if config word misses return error and exit program
  if len(config_content) == 0:
    print("no " + config_word + "in " + config_file + " found")
    print("program exit")
    exit()
  else:
    return config_content
  
#formats a string/line in the config.txt file for reading out the config-parameter
def FormatConfigString(string):
  content = string.rstrip()  #removes newline and whitespaces at the end of the string
  content = content.replace(" ", "") #removes all whitespace
  char = "="
  char_pos = content.find(char) + 1  # from the end of the string find the position of the char, +1 so that = is removed as well
  length_content = len(content)
  config_string = content[char_pos:length_content]  # remove file extension
  return config_string

#auto-detect, rename, move movies using filebot
def Filebot(input_path, output_path, name_format, database):

  name_format_filebot = "\"" + name_format + "\"" # add " at the start and end of name_format for filebot

  #start auto-detecting, renaming and moving of files
  print("Starting auto-detecting, renaming and moving files ...")
  subprocess.call([ "filebot", 
                    "-script",
                    "fn:renall",
                    input_path,
                    "-non-strict",
                    "--format",
                    name_format_filebot,
                    "--db",
                    database,
                    "--def",
                    "target=folder",
#                    "--action",  # uncomment both lines for debugging
#                    "test",      #
                    "--output",
                    output_path
                  ])
      

def main():

  config_file = "config.txt" # path of the config.txt file

  # list of parameters defined in the config_file
  config_words = ["input_path",
                 "output_path",
                 "name_format",
                 "database",
                 "file_extensions"
                ]
  
  # read config_file for defined config_words
  print("Reading parameters from " + config_file)
  input_path, output_path, name_format, database, file_extensions =  ReadConfig(config_file, config_words)
 
  #output config parameters
  print("Following parameters read from " + config_file + ":")
  print("Input dir: \t \t" + input_path) 
  print("Output dir: \t \t" + output_path)
  print("Filebot name format: \t" + name_format)
  print("Movie database: \t" + database)
  print("Movie extensions: \t" + file_extensions)
  print("\n \n")

  nM.PutNakedMoviesInFolders(input_path, file_extensions) #move movies which are not into subfolder to a subfolder
  Filebot(input_path, output_path, name_format, database) #auto-detect, rename, move movies


main()
