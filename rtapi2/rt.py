from requests import get, post, put, delete


class Connector(object):
    def __init__(self, host="localhost", username="admin", password="password", token=False, ssl=False):
        self.username = username
        self.password = password
        self.host = host
        self.token = token
        self.ssl = ssl
        self.authHeader = {"Authorization": "token " + str(self.token)}
        self.jsonHeader = {"Content-Type": "application/json"}
        self.jsonAuthHeader = {"Authorization": "token " + str(self.token), "Content-Type": "application/json"}
        if ssl:
            self.restPath = "https://" + self.host + "/REST/2.0/"
        else:
            self.restPath = "http://" + self.host + "/REST/2.0/"
        if not self.token:
            self.credentials = {'user': self.username, 'pass': self.password}
        else:
            self.credentials = {'token': self.token}

    def makeRequest(self, type="get", path="", data=None):
        if self.token:
            if type.lower() == "get":
                r = get(self.restPath + path, headers=self.authHeader)
            elif type.lower() == "post":
                r = post(self.restPath + path, json=data, headers=self.jsonAuthHeader)
            elif type.lower() == "put":
                r = put(self.restPath + path, json=data, headers=self.jsonAuthHeader)
            elif type.lower() == "delete":
                r = delete(self.restPath + path, headers=self.authHeader)
            else:
                return False
        else:
            if type.lower() == "get":
                r = get(self.restPath + path, auth=(self.username, self.password))
            elif type.lower() == "post":
                r = post(self.restPath + path, json=data, auth=(self.username, self.password), headers=self.jsonHeader)
            elif type.lower() == "put":
                r = put(self.restPath + path, json=data, auth=(self.username, self.password), headers=self.jsonHeader)
            elif type.lower() == "delete":
                r = delete(self.restPath + path, auth=(self.username, self.password))
            else:
                return False
        try:
            return r.json()
        except:
            return r.text


    def getHelp(self):
        return self.makeRequest(type="get", path="")

    def getInfo(self):
        return self.makeRequest(type="get", path="rt")

    def searchTickets(self, ticketProperties):
        return self.makeRequest(type="post", path="tickets", data=ticketProperties)

    def createTicket(self, ticketProperties):
        return self.makeRequest(type="post", path="ticket", data=ticketProperties)

    def getTicketProperties(self, ticketID):
        return self.makeRequest(type="get", path="ticket/" + ticketID)

    def updateTicket(self, ticketProperties, ticketID):
        return self.makeRequest(type="put", path="ticket/" + ticketID, data=ticketProperties)

    def deleteTicket(self, ticketID):
        return self.makeRequest(type="delete", path="ticket/" + ticketID)

    def correspondTicket(self, ticketProperties, ticketID):
        return self.makeRequest(type="post", path="ticket/" + ticketID + "/correspond", data=ticketProperties)

    def commentTicket(self, ticketProperties, ticketID):
        return self.makeRequest(type="post", path="ticket/" + ticketID + "/comment", data=ticketProperties)

    def getTicketHistory(self, ticketID):
        return self.makeRequest(type="get", path="ticket/" + ticketID + "/history")

    def getQueueHistory(self, queueIDOrName):
        return self.makeRequest(type="get", path="queue/" + queueIDOrName + "/history")

    def getAssetHistory(self, assetID):
        return self.makeRequest(type="get", path="asset/" + assetID + "/history")

    def getUserHistory(self, userIDOrName):
        return self.makeRequest(type="get", path="user/" + userIDOrName + "/history")

    def getGroupHistory(self, groupID):
        return self.makeRequest(type="get", path="group/" + groupID + "/history")

    def searchTransactions(self, transactionProperties):
        return self.makeRequest(type="post", path="transactions", data=transactionProperties)

    def getTransaction(self, transactionID):
        return self.makeRequest(type="get", path="transaction/" + transactionID)

    def getTransactionAttachments(self, transactionID):
        return self.makeRequest(type="get", path="transaction/" + transactionID + "/attachments")

    def searchAttachments(self, attachmentProperties):
        return self.makeRequest(type="post", path="attachments", data=attachmentProperties)

    def getAttachment(self, attachmentID):
        return self.makeRequest(type="get", path="attachment/" + attachmentID)

    def getAllQueueInformation(self):
        return self.makeRequest(type="get", path="queues/all")

    def searchQueues(self, queueProperties):
        return self.makeRequest(type="post", path="queues", data=queueProperties)

    def createQueue(self, queueProperties):
        return self.makeRequest(type="post", path="queue", data=queueProperties)

    def getQueue(self, queueIDOrName):
        return self.makeRequest(type="get", path="queue/" + queueIDOrName)

    def updateQueue(self, queueProperties, queueIDOrName):
        return self.makeRequest(type="put", path="queue/" + queueIDOrName, data=queueProperties)

    def deleteQueue(self, queueIDOrName):
        return self.makeRequest(type="delete", path="queue/" + queueIDOrName)

    def searchAssets(self, assetProperties):
        return self.makeRequest(type="post", path="assets", data=assetProperties)

    def createAsset(self, assetProperties):
        return self.makeRequest(type="post", path="asset", data=assetProperties)

    def getAsset(self, assetID):
        return self.makeRequest(type="get", path="asset/" + assetID)

    def updateAsset(self, assetProperties, assetID):
        return self.makeRequest(type="put", path="asset/" + assetID, data=assetProperties)

    def deleteAsset(self, assetID):
        return self.makeRequest(type="delete", path="asset/" + assetID)

    def getAllCatalogInformation(self):
        return self.makeRequest(type="get", path="catalogs/all")

    def searchCatalogs(self, catalogProperties):
        return self.makeRequest(type="post", path="catalogs", data=catalogProperties)

    def createCatalog(self, catalogProperties):
        return self.makeRequest(type="post", path="catalog", data=catalogProperties)

    def getCatalog(self, catalogIDOrName):
        return self.makeRequest(type="get", path="catalog/" + catalogIDOrName)

    def updateCatalog(self, catalogProperties, catalogIDOrName):
        return self.makeRequest(type="put", path="catalog/" + catalogIDOrName, data=catalogProperties)

    def deleteCatalog(self, catalogIDOrName):
        return self.makeRequest(type="delete", path="catalog/" + catalogIDOrName)

    def searchUsers(self, userProperties):
        return self.makeRequest(type="post", path="users", data=userProperties)

    def createUser(self, userProperties):
        return self.makeRequest(type="post", path="user", data=userProperties)

    def getUser(self, userIDOrName):
        return self.makeRequest(type="get", path="user/" + userIDOrName)

    def updateUser(self, userProperties, userIDOrName):
        return self.makeRequest(type="put", path="user/" + userIDOrName, data=userProperties)

    def deleteUser(self, userIDOrName):
        return self.makeRequest(type="delete", path="user/" + userIDOrName)

    def searchGroups(self, groupProperties):
        return self.makeRequest(type="post", path="groups", data=groupProperties)

    def getGroup(self, groupID):
        return self.makeRequest(type="get", path="group/" + groupID)

    def searchCustomFields(self, customFieldProperties):
        return self.makeRequest(type="post", path="customfields", data=customFieldProperties)

    def getCustomField(self, customFieldID):
        return self.makeRequest(type="get", path="customfield/" + customFieldID)

    def searchCustomRoles(self, customRoleProperties):
        return self.makeRequest(type="post", path="customroles", data=customRoleProperties)

    def getCustomRole(self, customRoleID):
        return self.makeRequest(type="get", path="customrole/" + customRoleID)