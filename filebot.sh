# move all movies, which are specified in the path AND which are not in a folder, 
# to a folder of the same name as the movie file -> important for the second script to work! 
# First run this script so that every movie is in a folder!!!
#filebot -script fn:renall "example/input_dir/" -non-strict --format "{fn}/{fn}" 

# DEBUG OF ABOVE
#filebot -script fn:renall "example/input_dir/" -non-strict --format "{fn}/{fn}" --action test --log Info

# Create new folder structure after name scheme: "FirstLetter/Year/MovieName" 
# i.e. The.Jungle.Book.2016.1080p.BluRay.DTS.x264-BDP -> J/2016/Jungle.Book ("The" gets ignored, don't know whether)
# and COPY file to output 
#filebot -script fn:renall "example/input_dir/" -non-strict --format "{n.acronym().getAt(0)}/{y}/{n.space('.')}" --db TheMovieDB --def target=folder --action copy --output "/example/output_dir/"

# Same as above but the file doesn't get copied it get's moved!
#filebot -script fn:renall "example/input_dir/" -non-strict --format "{n.acronym().getAt(0)}/{y}/{n.space('.')}" --db TheMovieDB --def target=folder --action copy --output "/example/output_dir/"

#DEBUG OF ABOVE
#filebot -script fn:renall ""example/input_dir/" -non-strict --format "{n.acronym().getAt(0)}/{y}/{n.space('.')}" --db TheMovieDB --def target=folder --output "/example/output_dir/" --action test --log Info


filebot -script fn:renall "example/input_dir/" -non-strict --format "{n.acronym().getAt(0).replaceAll('0', '#').replaceAll('1', '#').replaceAll('2', '#').replaceAll('3', '#').replaceAll('4', '#').replaceAll('5', '#').replaceAll('6', '#').replaceAll('7', '#').replaceAll('8', '#').replaceAll('9', '#')}/{y}/{n.space('.')}" --db TheMovieDB --def target=folder --output "example/output_dir/"


#.replaceAll(/\W|\d/, '#')
