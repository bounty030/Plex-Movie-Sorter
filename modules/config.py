  
def ReadConfig(config_file, config_words):

  i = 0
    
  print("Reading parameters from " + config_file)
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
      file_extensions_string = content
      file_extensions = content.split(",") #convert items seperated by "," to items of a list
    if i ==5:
      filebot_mode = content

    i += 1

  # read config_file for defined config_words
  print("Following parameters read from " + config_file + ":")
  print("Input dir: \t \t" + input_path) 
  print("Output dir: \t \t" + output_path)
  print("Filebot name format: \t" + name_format)
  print("Movie database: \t" + database)
  print("Movie extensions: \t" + file_extensions_string)
  print("Filebot mode: \t" + filebot_mode)
  print("\n \n")

  return input_path, output_path, name_format, database, file_extensions, filebot_mode
  
#search config file for config-parameter, if config-parameter found return it, else exit with error
def SearchConfig(config_file, config_word):
  
  config_content = ""
  
  with open(config_file) as f:
    for content in f: 
      if content.startswith(config_word):   #if config-parameter found
        config_content = content
      else:
        continue 
  
  f.close()

  # error handling in case config-word wasn't found
  if len(config_content) == 0:
    print("No \"" + config_word + "\" in " + config_file + " defined")
    print("Program exit")
    exit()
  else:
    return config_content
  

def FormatConfigString(string):
  content = string.rstrip()  #removes newline and whitespaces at the end of the string
  content = content.replace(" ", "") #removes all whitespace
  char = "="
  char_pos = content.find(char) + 1  # from the end of the string find the position of the char, +1 so that = is removed as well
  length_content = len(content)
  config_string = content[char_pos:length_content]  # remove file extension
  return config_string