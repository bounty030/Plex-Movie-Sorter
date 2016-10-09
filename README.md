# Plex-Movie-Sorter
Program which sorts movies from A to Z into folders. Fine-tuned for plex-scappers.

#Description
The program auto-detects movies by using the program "Filebot". Filebot reads the name of the folder in which the movie file is located and then compares it with a database (by default it is TheMovieDB). This is crucial because that's the way the Plex-Scrappers do it and doing it this way ensures that the Plex-Scrappers will detect the movie as well. Files which can't bed auto-detected because of bad naming are left as they are! The movie-file is then moved to the following folder-structure:

firstLetter/year/nameOfMovie/movieFile

with:
firstLetter - first letter of the movie
year - year of the movie
nameOfMovie - name of the movie
movieFile - unchanged name of the movie file

#Dependencies
-Python3.5
-Filebot

#Install
No installation needed.

#Config
There is config-file located in the main path called "config.txt".
Parameters to define:

-Directory where the movie files are located
input_path = example/input_dir/

-Directory where the movie files are moved to
-if you don't want to move files to another directory then input_path = output_path
output_path = example/output_dir/

-Name scheme for renaming the files with Filebot
name_format = "{n.acronym().getAt(0)}/{y}/{n.space('.')}"

-Database used by Filebot to auto-detect movies
database = "TheMovieDB"

-Only files with defined extensions will be processed
file_extensions = ['avi', 'dat', 'mp4', 'mkv', 'vob', 'flv'] 

#Example
There is an example directory structure with dummy files located in "example/". The default configuration processes the dummy files located in "example/input_dir/". Explanation of what the programm does:

1. Detect files in "example/input_dir/" which end with one of the defined 'file_extensions' AND which are not located in a subfolder.

2. Create subfolders for those files and name subfolders after files

3. Move files to subfolders

Steps 1, 2 and 3 are only made to ensure that the auto-detection uses the name of the folder and not the name of the file itself. Just the same way the Plex-Scrappers work!

4. Auto-detect, create folder-structure, move file to folder-structure by using Filebot

The end result is the following:
Folder-structure is firstLetter/year/movie-file where firstLetter is the firstLetter of the name of the movie except if it starts with "The", "A", "An".

For example:
example/input_dir/The.Sword.of.Doom.1966.1080p.Criterion.Bluray.DTS.x264-GCJM.mkv -> example/output_dir/S/1966/The.Sword.of.Doom/The.Sword.of.Doom.1966.1080p.Criterion.Bluray.DTS.x264-GCJM.mkv


#Usage
run:
$ python movieSorter.py

Don't forget to adjust the config-file "config.txt" to your needs!

