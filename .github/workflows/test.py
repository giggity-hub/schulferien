# f = open("demo.txt", "a")
# f.write("sheeeeesh\n")
import os
# print(os.listdir('Schulferien'))


directory = 'Schulferien'
for year in os.listdir('Schulferien'):
    year_directory = os.path.join(directory, year)

    for bundesland in os.listdir(year_directory):
        print(bundesland)
    # print(os.path.join(directory, filename))

    # https://stackoverflow.com/questions/57921401/push-to-origin-from-github-action/58393457#58393457