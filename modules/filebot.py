import subprocess
#start auto-detecting, renaming and testing of files
def FilebotRenameTest(input_path, output_path, name_format, database):
 
  print("Starting auto-detecting, testing and moving files ...")
  subprocess.call([ "filebot", 
                    "-script",
                    "fn:renall",
                    input_path,
                    "-non-strict",
                    "--format",
                    name_format,
                    "--action",  
                    "test",      
                    "--db",
                    database,
                    "--def",
                    "target=folder",

                    "--output",
                    output_path
                  ])

#start auto-detecting, renaming and moving of files
def FilebotRenameMove(input_path, output_path, name_format, database):  

  subprocess.call([ "filebot", 
                    "-script",
                    "fn:renall",
                    input_path,
                    "-non-strict",
                    "--format",
                    name_format,
                    "--db",
                    database,
                    "--def",
                    "target=folder",
#                    "--action",  # uncomment both lines for debugging
#                    "test",      #
                    "--output",
                    output_path
                  ])

#start auto-detecting, renaming and copying of files
def FilebotRenameCopy(input_path, output_path, name_format, database):

  
  print("Starting auto-detecting, renaming and moving files ...")
  subprocess.call([ "filebot", 
                    "-script",
                    "fn:renall",
                    input_path,
                    "-non-strict",
                    "--format",
                    name_format,
                    "--action",
                    "copy",
                    "--db",
                    database,
                    "--def",
                    "target=folder",
                    "--output",
                    output_path
                  ])  


def FileBotRename(arg, input_path, output_path, name_format, database):

  name_format_filebot = "\"" + name_format + "\"" # add " at the start and end of name_format for filebot

  filebot_counter = 0

  with open("logs/files.in.folders.stripped.txt") as f:
    for folder_path in f:
      folder_path = folder_path.rstrip()  #removes newline and whitespaces at the end of the string
      if arg == 'test':
        print("Starting Filebot Test: auto-detecting, renaming and moving files ...")
        FilebotRenameTest(folder_path, output_path, name_format_filebot, database)

      if arg == 'move':
        print("Starting Filebot: auto-detecting, renaming and moving files ...")
        FilebotRenameMove(folder_path, output_path, name_format_filebot, database)

      if arg == 'copy':
        print("Starting Filebot: auto-detecting, renaming and copying files ...")
        FilebotRenameCopy(folder_path, output_path, name_format_filebot, database)

      i += 1
      print("Processed " + folder_path )
      print("Files processed: " + str(i))


