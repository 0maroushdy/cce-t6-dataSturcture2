import os

class RBNode:
    def __init__(self, key):
        self.key = key          
        self.color = 'RED'       
        self.left = None         
        self.right = None        
        self.parent = None       

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = 'BLACK'  
        self.root = self.NIL      
        self.size = 0             

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        # bndawar 3ala el place el monacep llNode
        while current != self.NIL:
            parent = current
            if key == current.key:
                print("ERROR: Word already exists")
                return False  # 3ashan el Word already exists
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if not parent:
            self.root = new_node  # Hen elTree was empty and the inserted tree is the node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fix_insert(new_node)  # Fix any RBT violations
        self.size += 1
        return True

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if not y.parent:
            self.root = x
            #------------
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def fix_insert(self, z):
        while z.parent and z.parent.color == 'RED':
            if z.parent == z.parent.parent.left: # lw el parent bta3 z left child
                y = z.parent.parent.right  
                if y.color == 'RED': # Case: Uncle is red - recolor
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent 
                else:
                    if z == z.parent.right: # Case: Uncle is black and z is right child - rotate
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left  # init el uncle bta3 z
                if y.color == 'RED':
                    z.parent.color = 'BLACK' 
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent 
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'BLACK'  

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node == self.NIL or not node:
            return False 
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def get_black_height(self):
        node = self.root
        height = 0
        while node != self.NIL:
            if node.color == 'BLACK':
                height += 1
            node = node.left 
        return height

    def get_size(self):
        return self.size


class DictionaryApp:
    def __init__(self, file_path):
        self.tree = RedBlackTree()
        self.file_path = file_path
        self.load_dictionary()

    def load_dictionary(self):
        if not os.path.exists(self.file_path):
            print("ERROR: File does not exist!")
            return
        with open(self.file_path, 'r') as f:  
            for line in f:
                word = line.strip()
                if word:
                    self.tree.insert(word)

    def insert_word(self, word):
        word = word.strip()
        if not word:
            print("ERROR: Empty word cannot be inserted")
            return
            
        if self.tree.search(word):
            print("ERROR: Word already in the dictionary")
        else:
            success = self.tree.insert(word)
            if success:
                print(f'Inserted: {word}')
                with open(self.file_path, 'a') as f:  
                    f.write(word + '\n')
                
                print(f'Size: {self.tree.get_size()}')
                print(f'Height: {self.tree.get_height()}')
                print(f'Black Height: {self.tree.get_black_height()}')

    def lookup_word(self, word):
        word = word.strip()
        if not word:
            print("ERROR: Empty word cannot be looked up")
            return
        elif self.tree.search(word):
            print("YES, word exists")
        else:
            print("NO, word does not exist")

    def print_stat(self):
        print(f'Size: {self.tree.get_size()}')
        print(f'Height: {self.tree.get_height()}')
        print(f'Black Height: {self.tree.get_black_height()}')


app = DictionaryApp("Dictionary.txt")
print("\n ------------------- Dictionary App -------------------")
while True:
    print("Options: \n1- Insert Word  \n2- Look-up Word \n3- Print Statistics \n4- Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        word = input("Enter word to insert: ").strip()
        app.insert_word(word)
    elif choice == "2":
        word = input("Enter word to look up: ").strip()
        app.lookup_word(word)
    elif choice == "3":
        app.print_stat()
    elif choice == "4":
        break
    else:
        print("Invalid option.")
    print("/n--------------------------------------------------------")

