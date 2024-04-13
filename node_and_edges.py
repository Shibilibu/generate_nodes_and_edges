def generate_node_and_edges(email):
    
    #convert the email to a numerical value by using ord()
    email_value = sum(ord(char) for char in email)
    
    #generate random number of nodes based on email values
    num_nodes = (email_value % 7) + 4
    
    #Generate random nodes
    nodes =[]
    for i in range(num_nodes):
        nod_name = chr(65 +(email_value + i)% 26) + chr(65 +(email_value + i + 1)%26)
        nodes.append(nod_name)
    edges =[]
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if (email_value + i+j)%2==0: #add edge between node i and j only if their
                edge ={"from": nodes[i], "to": nodes[j], "cost": round((email_value +i+j)%10+1,2)}
                edges.append(edge)
    return nodes,edges
#input email
email = "abc@email.com"

#Generate nodes and edges
nodes , edges = generate_node_and_edges(email)

print("Nodes:",nodes)
print("Edges:")
for edge in edges:
    print(edge)
         
    