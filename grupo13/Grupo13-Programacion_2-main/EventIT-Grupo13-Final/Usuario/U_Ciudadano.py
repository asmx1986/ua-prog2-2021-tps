from Monitoreo.M_Solicitudes import Solicitud
from Monitoreo.Manipulacion_csv import writelist, getList, getValue


class Ciudadano:
    def __init__(self, name):
        self.name = name
        self.friends = self.getfriends()
        self.friend_request = self.getfriend_request()
        self.rejected_requests = self.getrejected_requests()

    def getfriends(self):
        return getList("ciudadano_a", 'Name', 'Friends', self.name)

    def getfriend_request(self):
        return getList("ciudadano_s", 'Name', 'Friend_request', self.name)

    def getrejected_requests(self):
        return getValue("ciudadano", "Name", 'Rejected_requests', self.name)

    def getname(self):
        return self.name

    def sendFriend_Request(self, receiver):
        friend_request = Solicitud(self, receiver)
        friend_request.send(self.name)

    def acceptFriend_Request(self, request):
        friends = self.getfriends()
        if not self.equalfriends(request, friends) and self.equalrequest(request):
            if friends == ['Nada que encontrar...']:
                writelist("ciudadano_a", 'Name', 'Friends', self.name, request, ['Nada que encontrar...'])
                writelist("ciudadano_a", 'Name', 'Friends', request, self.name, ['Nada que encontrar...'])
            else:
                new_friends = self.getfriends()
                new_friends.append(request)
                new_friends2 = Ciudadano(request).getfriends()
                new_friends2.append(self.name)
                writelist("ciudadano_a", 'Name', 'Friends', self.name, new_friends, self.getfriends())
                writelist("ciudadano_a", 'Name', 'Friends', request, new_friends2, Ciudadano(request).getfriends())
        self.delFriend_Request(request)

    def rejectFriend_Request(self, name):
        name_request = self.getfriend_request()
        for request in name_request:
            if request == name:
                rejected = Solicitud(self, Ciudadano(name))
                rejected.sumRejected_requests()
                self.delFriend_Request(name)

    def delFriend_Request(self, name):
        if self.equalrequest(name):
            if len(self.getfriend_request()) == 1:
                self.getfriend_request().remove(name)
                writelist("ciudadano_s", 'Name', 'Friend_request', self.name, ['Nada que encontrar...'], self.getfriend_request())
            else:
                new_request = self.getfriend_request()
                new_request.remove(name)
                writelist("ciudadano_s", 'Name', 'Friend_request', self.name, new_request, self.getfriend_request())
        else:
            print("La solicitud inexistente")

    def delFriend(self, name):
        if len(self.getfriends()) == 1:
            self.getfriends().remove(name)
            writelist("ciudadano_a", 'Name', 'Friends', self.name, ['Nada que encontrar...'], self.getfriends())
        else:
            new_request = self.getfriends()
            new_request.remove(name)
            writelist("ciudadano_a", 'Name', 'Friends', self.name, new_request, self.getfriends())

    @staticmethod
    def equalfriends(request, friends):
        for elements in friends:
            if elements == request:
                print("La solicitud ya fue aceptada con anterioridad")
                return True
        return False

    def equalrequest(self, request_name):
        request_list = self.getfriend_request()
        for elements in request_list:
            if elements == request_name:
                return True
        return False
