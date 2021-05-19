import os

class ChangeFileName:
    def __init__(self, directoryLocation, fileName, fileExtension):
        self.directoryLocation = directoryLocation
        self.fileExtension = fileExtension

        #gets the number of files
        self.fileNumber = 0
        for file in os.listdir(self.directoryLocation):
            self.fileNumber += 1
        lenFileNumber = len(str(self.fileNumber))
        
        self.fileName = f'{fileName} {str(0) * lenFileNumber}' #file name
    
    def new_file_name(self):
        if self.fileNumber < 10:
            self.fileNames = self.fileName[:-1]
        elif self.fileNumber < 100:
            self.fileNames = self.fileName[:-2]
        else:
            self.fileNames = self.fileName[:-3]
        return f'{self.directoryLocation}{self.fileNames} {self.fileNumber}{self.fileExtension}'

    def change_file_name(self):
        for file in os.listdir(self.directoryLocation):
            if file[-4:] == self.fileExtension:
                oldFile = f'{self.directoryLocation}{file}'
                os.rename(oldFile, self.new_file_name())
                self.fileNumber += 1