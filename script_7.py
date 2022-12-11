class Node:
    def __init__(self, name: str, type: str, parent) -> None:
        self.name = name
        self.type = type
        self.parent = parent
        self.children = []
        self.size = None
        
    def add_child(self, node):
        names = []
        for i in self.children:
            names.append(i.name)
        if not node.name in names:
            self.children.append(node)
        
    def get_children(self, node_name: str):
        for i in self.children:
            if i.name == node_name:
                return i


with open('input_7.txt', 'r') as f:
    lines = [line.rstrip() for line in f]

root_node = Node('/','dir', None)
lmlsvqsw = Node('lmlsvqsw','dir', root_node)
rlfgcqz = Node('rlfgcqz','dir', root_node)
sjq = Node('sjq','dir', root_node)
tpnspw = Node('tpnspw','dir', root_node)
hdwsmn = Node('hdwsmn','dir', root_node)
root_node.add_child(lmlsvqsw)
root_node.add_child(rlfgcqz)
root_node.add_child(sjq)
root_node.add_child(tpnspw)
root_node.add_child(hdwsmn)

cur_node = root_node
for i in range(len(lines)):
    line = lines[i]
    print(line)
    if '$' in line:
        command = line.split(' ')
        if command[1] == 'cd':
            if command[2] == '..':
                #if not root_node
                if cur_node != root_node:
                    cur_node = cur_node.parent
                else:
                    pass
            # cd into dir name
            else:
                dir_node = cur_node.get_children(command[2])
                cur_node = dir_node
        elif command[1] == 'ls':
            j = i + 1
            while j <= (len(lines)-1) and not '$' in lines[j]:
                #if dir
                if 'dir' in lines[j]:
                    dir_name = lines[j].split(' ')[1]
                    dir_node = Node(dir_name,'dir', cur_node)

                    cur_node.add_child(dir_node)
                #if file
                else:
                    file_name = lines[j].split(' ')[1]
                    file_node = Node(file_name,'file', cur_node)
                    file_node.size = int(lines[j].split(' ')[0])
                    cur_node.add_child(file_node)
                j += 1

def calculate_node(node: Node, close_node: int):
    
    if node.type == 'file':
        return node.size, close_node
    else:
        size_sum = 0
        close_list = []
        for child in node.children:
            size_toadd, close_node = calculate_node(child, close_node)
            close_list.append(close_node)
            size_sum += size_toadd
        close_node = min(close_list)
        node.size = size_sum
        if node.size + 21309880 >= 30000000 and node.size < close_node:
            close_node = node.size
        return size_sum, close_node


a, b = calculate_node(root_node, close_node = 70000000)
print(str(b))

total_need = 70000000 - a
print(str(total_need))
