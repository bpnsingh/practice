from typing import List, Tuple, Dict, Union

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        answers = []
        locationToServerMapping = {}  # each pair corresponds to : ( location, serverID )
        serverToKeyMappings = {}  # each pair corresponds to : ( serverID, [usernames] )

        def userHash(username: str, hashKey: int) -> int:
            p = hashKey
            n = 360
            hashCode = 0
            p_pow = 1
            for i in range(len(username)):
                character = username[i]
                hashCode = (hashCode + (ord(character) - ord('A') + 1) * p_pow) % n
                p_pow = (p_pow * p) % n
            return hashCode

        def assignRequest(keyname: str, hashKey: int) -> int:
            if not locationToServerMapping:
                return -1
            keyLocation = userHash(keyname, hashKey)
            it = locationToServerMapping.get(keyLocation)
            if not it:
                it = locationToServerMapping.get(0)
            serverID = it
            serverToKeyMappings[serverID].append(keyname)
            return keyLocation

        def findRequestsToServe(serverLocation: int, hashKey: int):
            if not serverToKeyMappings:
                return
            it = locationToServerMapping.get(serverLocation + 1)
            if not it:
                it = locationToServerMapping.get(0)
            serverID = it
            keynames = serverToKeyMappings[serverID]
            serverToKeyMappings[serverID] = []
            for keyname in keynames:
                assignRequest(keyname, hashKey)

        def addServer(serverID: str, hashKey: int) -> int:
            firstLocation = userHash(serverID, hashKey)
            locationToServerMapping[firstLocation] = serverID
            findRequestsToServe(firstLocation, hashKey)
            return len(serverToKeyMappings[serverID])

        def removeServer(serverID: str, hashKey: int) -> int:
            for key, value in locationToServerMapping.items():
                if value == serverID:
                    locationToServerMapping.pop(key)
                    break
            keynamesToReassign = serverToKeyMappings.pop(serverID)
            for keyname in keynamesToReassign:
                assignRequest(keyname, hashKey)
            return len(keynamesToReassign)

        def performOperation(A: str, B: str, C: int):
            if A == "ADD":
                serverID = B
                answers.append(addServer(serverID, C))
            elif A == "REMOVE":
                serverID = B
                answers.append(removeServer(serverID, C))
            elif A == "ASSIGN":
                keyname = B
                answers.append(assignRequest(keyname, C))

        for action,location,code in zip(A,B,C):
            performOperation(action,location,code)
        return  answers


scaler = Solution()
A = ['ADD', 'ASSIGN', 'ADD', 'ASSIGN', 'REMOVE', 'ASSIGN']
B = ['INDIA', 'NWFJ', 'RUSSIA', 'OYVL', 'INDIA', 'IGAX']
C = [7, 3, 5, 13, 23, 17]

print (scaler.solve(A,B,C))