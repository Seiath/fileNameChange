import os

class ChangeFileName:
    def __init__(self, directoryLocation, fileName, fileExtension, filenumber):
        self.directoryLocation = directoryLocation
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.fileNumber = filenumber
        
        self.change_file_name()
    
    def new_file_name(self):
        if self.fileNumber < 10:
            self.fileNames = self.fileName[:]
        elif self.fileNumber < 100:
            self.fileNames = self.fileName[:-1]
        else:
            self.fileName = self.fileName[:-2]
        return f'{self.directoryLocation}{self.fileNames}{self.fileNumber}{self.fileExtension}'

    def change_file_name(self):
        for file in os.listdir(self.directoryLocation):
            if file[-4:] == self.fileExtension:
                oldFile = f'{self.directoryLocation}{file}'
                os.rename(oldFile, self.new_file_name())
                self.fileNumber += 1
