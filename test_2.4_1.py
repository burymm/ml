import os
import os.path

found = []
dir_name = ''

for current_dir, dirs, files in os.walk('main'):
    for file in files:
        print(file[-3:])
        if file.rstrip()[-3:] == '.py' and current_dir not in found:
            found.append(current_dir)
    print(current_dir, dirs, files)
found.sort()
print('\n\n\n\n\n' + '\n'.join(found))