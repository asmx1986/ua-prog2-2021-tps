from listadeCuidadanos import etlist

class RevisionList():

    def __init__(self):
        self.revision_list = []

    def update_revision_list(self):
        for citizen in etlist.citizenlist:
            if len(citizen.quien_me_rechazo)==5:
                self.revision_list.append(citizen)
        return "Lista actualizada"

    def removecitizen(self,citizen):
        index = self.revision_list.index(citizen)
        del self.revision_list[index]


    def getlist(self):
        return self.revision_list


defualt_revision_list=RevisionList()
defualt_revision_list.revision_list.append(etlist.citizenlist[0])
