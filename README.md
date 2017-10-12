# RT Python Module

## Installation

`pip install rtapi2`

## Information
General Notes:
- All numbers should be given as strings
- Almost all data is returned in a dictionary
- Go to https://github.com/bestpractical/rt-extension-rest2 to view information on endpoints

## Requirements
- python2.7
- requests

## Methods
Available Methods:
- getHelp()
- getInfo()
- searchTickets(ticketProperties)
- createTicket(ticketProperties)
- getTicketProperties(ticketID)
- updateTicket(ticketProperties, ticketID)
- deleteTicket(ticketID)
- correspondTicket(ticketProperties, ticketID)
- commentTicket(ticketProperties, ticketID)
- getTicketHistory(ticketID)
- getQueueHistory(queueIDOrName)
- getAssetHistory(assetID)
- getUserHistory(userIDOrName)
- getGroupHistory(groupID)
- searchTransactions(transactionProperties)
- getTransaction(transactionID)
- getTransactionAttachments(transactionID)
- searchAttachments(attachmentProperties)
- getAttachment(attachmentID)
- getAllQueueInformation()
- searchQueues(queueProperties)
- createQueue(queueProperties)
- getQueue(queueIDOrName)
- updateQueue(queueProperties, queueIDOrName)
- deleteQueue(queueIDOrName)
- searchAssets(assetProperties)
- createAsset(assetProperties)
- getAsset(assetID)
- updateAsset(assetProperties, assetID)
- deleteAsset(assetID)
- getAllCatalogInformation()
- searchCatalogs(catalogProperties)
- createCatalog(catalogProperties)
- getCatalog(catalogIDOrName)
- updateCatalog(catalogProperties, catalogIDOrName)
- deleteCatalog(catalogIDOrName)
- searchUsers(userProperties)
- createUser(userProperties)
- getUser(userIDOrName)
- updateUser(userProperties, userIDOrName)
- deleteUser(userIDOrName)
- searchGroups(groupProperties)
- getGroup(groupID)
- searchCustomFields(customFieldProperties)
- getCustomField(customFieldID)
- searchCustomRoles(customRoleProperties)
- getCustomRole(customRoleID)

## Usage
```python
from rtapi2 import rt

#Supports basic auth
#connector = rt.Connector(host="localhost:8080", username="user", password="password", ssl=False)

#Supports new tokens!
connector = rt.Connector(host="localhost:8080", token="1234567", ssl=False)

properties = {"id": "ticket/new", "Queue": "General", "Requestor": "user@email.com", "Priority": "4", "Subject": "Test REST Module", "Text": "test"}

response = connector.createTicket(properties)
print response
```
