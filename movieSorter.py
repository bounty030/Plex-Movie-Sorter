#!/usr/bin/python3.5

import os
import os.path
import modules.config as config
import modules.scanDir as sD
import modules.filebot as fb

def main():

  config_file = "config.txt" # path of the config.txt file

  # list of parameters defined in the config_file
  config_words = ["input_path",
                 "output_path",
                 "name_format",
                 "database",
                 "file_extensions",
                 "filebot_mode"
                ]
  
  input_path, output_path, name_format, database, file_extensions, filebot_mode = config.ReadConfig(config_file, config_words)
  sD.ScanDir(file_extensions, input_path)
  fb.FileBotRename(filebot_mode, input_path, output_path, name_format, database) 
  #FilebotMove(input_path, output_path, name_format, database)  
  #FilebotCopy(input_path, output_path, name_format, database)


main()