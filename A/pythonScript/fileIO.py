import os
import time



def findTxtFiles():
    
    fPath = 'C:\\A\\B'

    dirList = os.listdir(fPath)
    
    for file in dirList:
        # iterate thru files in directory
        if file.endswith(".txt"):
            comList = (os.path.join(fPath, file))
            # Get file's Last modification time stamp only in terms of seconds since epoch 
            modTimesinceEpoc = (os.path.getmtime(comList))
            # Convert seconds since epoch to readable timestamp
            modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            print(comList, modificationTime)


            
if __name__ == "__main__":
    findTxtFiles()
