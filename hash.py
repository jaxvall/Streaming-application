from linkedQFile import LinkedQ


class HashNode:
    def __init__(self, key, data, next=None):
        self.key = key
        self.data = data
        self.next = next

class KeyError(Exception):
    pass

class HashTable:
    def __init__(self, length):
        self.length = length * 2 + 1
        self.table = [0]*self.length
        self.counter = 0

    def __contains__(self, key):
        hash_value = hash_function(key)
        list_pos = int(hash_value) % (self.length)
        if self.table[list_pos] != 0:
            return True
        else:
            # raise KeyError("There is no key called " + key)
            return False

    def store(self, key, data):
        hash_value = hash_function(key)
        list_pos = int(hash_value) % (self.length)
        if self.table[list_pos] == 0:
            self.table[list_pos] = HashNode(key, data)
        elif self.table[list_pos] != 0:
            self.counter += 1
            print("counter",self.counter)
            store_node(key, self.table[list_pos], data)

    def get(self, key):
        hash_value = hash_function(key)
        list_pos = int(hash_value) % (self.length)
        if self.table[list_pos] != 0:
             object = node_seeker(key, self.table[list_pos])
             # print(object)
             return object

def node_seeker(key, item):
    if key == item.key:
        # print(item.data)
        return item.data
    return node_seeker(key, item.next)

def store_node(key, item, data):
    if item.next == None:
        # if counter != 0:
        # print(counter)
        item.next = HashNode(key, data)
        return
    # counter += 1
    store_node(key, item.next, data)

def hash_function(key):
    # value = "" # tom sträng
    # counter = 3
    # for tkn in key: #tar ett tecken i taget fån nyckeln
    #     value += str(ord(tkn)) # adderar sträng av teckenvärde till value-sträng
    # hash_list = list(value) #tar strängen och gör en lista av den
    # hash_value = 0
    # for i in range(len(hash_list // 3)): # loopar en gång per tecken delat med 3 TOG BORT DELAT MED 3 HELTAL
    #     part = ''.join(hash_list[i:i+3])
    #     hash_value += int(part) * counter
    #     counter += 17

    hash_value = 0
    counter = 2
    for tkn in key:
        hash_value += ord(tkn) * counter
        counter += 3

    return int(hash_value)
