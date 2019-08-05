# get all AI project names
find -name '*?Project.txt' | xargs cat | sort | uniq > allProjects.txt
