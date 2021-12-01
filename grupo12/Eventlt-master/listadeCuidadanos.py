from citizen import ciudadano as creadordeciudadano
import pandas
import os

class CitizenList():

    def __init__ (self):
        self.citizenlist=[]
        self.BannedCitizenList=[]
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        i = 0
        while i != len(df['CUIL']):
            self.citizenlist.append(creadordeciudadano.init_citizen_creation(df['Name'][i], df['Surname'][i], df['age'][i], df['CUIL'][i], df['Phonenumber'][i], df['Zona'][i]))
            i += 1
            
    def addCitizen(self, citizen):
        self.citizenlist.append(citizen)
        
    def addBannedCitizen(self, citizen):
        self.BannedCitizenList.append(citizen)

    def remove_citizen(self,citizen):
        counter=0
        while counter<len(self.citizenlist):
            if citizen==self.citizenlist[counter]:
                del self.citizenlist[counter]
                return self.citizenlist
            else:
                counter=counter+1
    def removeBannedCitizen(self, citizen):
        i=0
        while i<len(self.BannedCitizenList):
            if citizen==self.BannedCitizenList[i]:
                del self.BannedCitizenList[i]
                return self.BannedCitizenList
            else:
                i += 1

    def getcl(self):
        return(self.citizenlist)

etlist = CitizenList()

