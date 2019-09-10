import numpy as np

def myFunc(e):
    return e



# Info stored for each router
class Node(object):
    def __init__(self, name, n):
        self.name = name
        self.number = n
        self.neighbours = []
        self.routingTable = []  #----- Destination, Cost, Next Hop

abf = '''afefawfdsf'''

# Bellman Ford's Algorithm
class Algorithm(object):

    @staticmethod
    def shareRT(vertexList):

        print("---------------------\n\nRouting Tables being transmitted 1 by 1:")
        #UPDATE_HAPPENED = False

        while True:
            UPDATE_HAPPENED = False
            for receiver in vertexList:
                print("-----------------------------------------------")
                for sender in receiver.neighbours:
                    current_cost = 0
                    next_hop = '#'
                    for lol in receiver.routingTable:
                        if lol[0] == sender.name:
                            current_cost = lol[1]
                            next_hop = lol[2]
                    print(sender.name," sends its DV to ",receiver.name," , and is at distance ",current_cost," from it.")

                    for i in receiver.routingTable:
                        L1 = list(i)
                        for j in sender.routingTable:
                            L2 = list(j)
                            if (i[0] == j[0]) & ((j[1] + current_cost) < i[1]):
                                print(L1, "\t", " and ",end='')
                                print(L2, " ",end='')
                                L1[1] = L2[1]+current_cost
                                L1[2] = next_hop#changed from sender.name
                                receiver.routingTable.remove((i[0],i[1],i[2]))
                                i = tuple(L1)
                                receiver.routingTable.append(i)
                                print(" updates L1 to ",i)
                                UPDATE_HAPPENED = True
                            else:
                                continue
                        #i = tuple(L1)
                if UPDATE_HAPPENED == True:
                    print("\n\nUPDATED ",end='')
                    print(receiver.name, "'s Routing Table:")
                    receiver.routingTable.sort()
                    print(receiver.routingTable, sep='\n')

            if(UPDATE_HAPPENED == False):
                break
            
        print("STABLE STATE REACHED!")



###########################################################################################################################
vertexList = []
print("Enter number of routers:")
n = int(input())
for i in range(n):
    print("Enter label for router %d " % i)
    node = Node(input(), i)#
    vertexList.append(node)
    node.routingTable.append((node.name, 0, node.name))

for router in vertexList:
    for other in vertexList:
        if other.name != router.name:
            router.routingTable.append((other.name, 99, other.name))



print("Initiating....")

#-------------------Routers set up

print("Enter number of links:")
m = int(input())
for i in range(m):
    print("Source Name, Destination Name, Cost:")
    sourceLabel = Node(input(), 0)
    destLabel = Node(input(),0)#don't make another routing table, since will be replaced
    cost = int(input())

    for i in vertexList:
        if i.name == sourceLabel.name:
            sourceLabel = i
        if i.name == destLabel.name:
            destLabel = i

    for lol in sourceLabel.routingTable:
        if lol[0] == destLabel.name:
            earlier_cost = lol[1]

    if destLabel not in sourceLabel.neighbours:
        sourceLabel.neighbours.append(destLabel)
    if sourceLabel not in destLabel.neighbours:
        destLabel.neighbours.append(sourceLabel)

    sourceLabel.routingTable.remove((destLabel.name, earlier_cost, destLabel.name))
    sourceLabel.routingTable.append((destLabel.name, cost, destLabel.name))
    destLabel.routingTable.remove((sourceLabel.name, earlier_cost, sourceLabel.name))
    destLabel.routingTable.append((sourceLabel.name, cost, sourceLabel.name))


print("-----------------INITIALIZATION------------------------")
for i in vertexList:
    print(i.name,"'s Routing Table:")
    i.routingTable.sort(key=myFunc)
    for j in i.routingTable:
          print(j,"\t",end='')
    print()


algorithm = Algorithm()
algorithm.shareRT(vertexList)

while True:
    print("Update cost of some link? Y:N")
    opt = input()
    if opt == 'Y':
        print("Source Name, Destination Name, Cost:")
        sourceLabel = Node(input(), 0)
        destLabel = Node(input(), 0)  # don't make another routing table, since will be replaced
        cost = int(input())
        earlier_cost = 0
        for i in vertexList:
            if i.name == sourceLabel.name:
                sourceLabel = i
            if i.name == destLabel.name:
                destLabel = i

        for lol in sourceLabel.routingTable:
            if lol[0] == destLabel.name:
                earlier_cost = lol[1]

        print("Earlier cost from ",sourceLabel.name," to ",destLabel.name," was ",earlier_cost)
        sourceLabel.routingTable.remove((destLabel.name, earlier_cost, destLabel.name))
        sourceLabel.routingTable.append((destLabel.name, cost, destLabel.name))
        destLabel.routingTable.remove((sourceLabel.name, earlier_cost, sourceLabel.name))
        destLabel.routingTable.append((sourceLabel.name, cost, sourceLabel.name))
        algorithm.shareRT(vertexList)
    else:
        break
