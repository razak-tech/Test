import Organize_moveis
import Rename_movies
import pyfiglet

name = pyfiglet.figlet_format("Badass Movie")
print(name)


directory = ""
Rename_movies.main()

answer = input("Do you want to organize movies (Yes/No) ? : ").strip().lower()

if answer == "yes":
    Organize_moveis.organize_movies(directory)
else:
    print("Done ✅")

# TASKS:
# make choices 1 rename 2 orgenize 3 bothe 4 exit
# the Same path 
# when no file do not ask for orgenize 
# remove exit ....
