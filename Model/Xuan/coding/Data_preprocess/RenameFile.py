import os


def renameFile(path):
    print('come into path:' + path)
    fileList = os.listdir(path)
    folderPath, folderName = os.path.split(path)
    i = 1000
    for file in fileList:
        filepath, filename = os.path.split(file)
        # print(filename.split('_')[1])
        oldfilename = path + os.sep + file
        newfilename = path + os.sep + folderName + '_' + str(i) + '.jpg'
        os.rename(oldfilename, newfilename)
        print(oldfilename + ' -> ' + newfilename)

        i += 1
    print("done")


# ----------------- rename files -------------------- #
path = '/Users/zhouguozhi/PyhtonFile/Data for project'
if os.path.exists(path):
    print('path found')
else:
    print('path not found')
for folders in os.listdir(path):
    # print(folders)
    folderPath = path + os.sep + folders
    for folders in os.listdir(folderPath):
        if '.DS' not in folders:
            imagespath = folderPath + os.sep + folders
            renameFile(imagespath)
# --------------------------------------------------- #