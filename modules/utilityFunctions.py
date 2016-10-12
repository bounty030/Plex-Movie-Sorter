# -*- coding: utf-8 -*-

def StripFilename(input_file, output_file):

  g = open(output_file, "w")  

  with open(input_file) as f:
    for content in f: 
      content = content.rstrip()
      char = "/"
      char_pos = content.rfind(char) +1   # from the end of the string find the position of the char, +1 so that = is removed as well
      stripped_content = content[0:char_pos]
      g.write(stripped_content + "\n")

  print("Stripped file-paths from folders " + "-> " + output_file)
  f.close()
  g.close()