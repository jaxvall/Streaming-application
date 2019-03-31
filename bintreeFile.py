class DoubleNode:
    def __init__(self,  key, data):
        self.key = key
        self.data = data
        self.right = None
        self.left = None

class Bintree:
    def __init__(self):
        self.root = None

    def __contains__(self, word):
        # True om word finns i trädet, False annars
        return finns(self.root, word)

    def put(self, new_word, object):
        # Sorterar in newword i trädet
        if self.root == None:
            self.root = putta(self.root, new_word, object)
        else:
            putta(self.root, new_word, object)

    def get(self, word):
        x = get_word(self.root, word)
        return x

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

def putta(node, word, object):
    if node == None:
        node = DoubleNode(word, object)
        return node

    else:
        list = []
        list.append(word)
        list.append(node.key)
        list.sort()
        new_word = list.index(word) #de här är antingen 0 eller 1 OBS
        old_word = list.index(node.key)

        if new_word > old_word and node.right != None:
            putta(node.right, word, object)
        elif new_word > old_word and node.right == None:
            node.right = DoubleNode(word, object)
        elif new_word < old_word and node.left != None:
            putta(node.left, word, object)
        elif new_word < old_word and node.left == None:
            node.left = DoubleNode(word, object)
        elif new_word == old_word:
            print(word, "already in tree!")

def finns(node, word):
    if node == None:
        return False

    if node.key == word:
        return True
    elif node.key > word:
        return finns(node.left, word)
    elif node.key < word:
        return finns(node.right, word)

def get_word(node, word):

    if node.key == word:
        return node.data
    elif node.key > word:
        return get_word(node.left, word)
    elif node.key < word:
        return get_word(node.right, word)

def skriv(node):
    if node != None:
        skriv(node.left)
        print(node.key)
        skriv(node.right)

if __name__ == "__main__":
    tree = Bintree()

    tree.put("a", 1)
    tree.put("b", 2)
    tree.put("q", 3)
    tree.put("s", 4)
    print("a" in tree)
    print('q' in tree)
    print(tree.get('q'))
