import os
class ChangeFileName:
    def __init__(self, directoryLocation, fileName, fileExtension):
        self.directoryLocation = directoryLocation
        self.fileName = fileName
        self.fileExtension = fileExtension
        self.fileNumber = 1
        for file in os.listdir(self.directoryLocation):
            self.fileNumber += 1
        lenFileNumber = int(len(str(self.fileNumber)))
        self.fileName = f"{self.fileName} {'0'*lenFileNumber}"

        self.fileNumber = 1
        self.change_file_name()
    
    def new_file_name(self):
        if self.fileNumber < 10:
            fileNames = self.fileName[:-1]
        elif self.fileNumber < 100:
            fileNames = self.fileName[:-2]
        else:
            self.fileName = self.fileName[:-3]
        return f'{self.directoryLocation}\\{fileNames}{self.fileNumber}{self.fileExtension}'

    def change_file_name(self):
        for file in os.listdir(self.directoryLocation):
            if file[-4:] == self.fileExtension:
                oldFile = f"{self.directoryLocation}\\{file}" 
                os.rename(oldFile, self.new_file_name())
                self.fileNumber += 1