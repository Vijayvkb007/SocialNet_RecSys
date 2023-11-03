import networkx as nx
from matplotlib import pyplot as plt

# creating set of users with connections
social_g = {
  'Aryan': [('Adya'), ('Vijay'), ('Ragha')],
  'Adya': [('Aryan'), ('Vijay'), ('Abhishek')], 
  'Abhay': [('Aryan'), ('Abhishek'), ('Anu')],
  'Abhishek': [('Adya'), ('Vijay')],
  'Akash': [('Balaji'), ('Ragha')],
  'Vijay': [('Abhay'), ('Adya'), ('Abhishek')],
  'Ragha': [('Aryan'), ('Abhay'), ('Vijay')],
  'Anu': [('Balaji'), ('Aryan')],
  'Balaji': [('Adya'), ('Aryan'), ('Abhay')],
  'Nigga': [('Aryan')],
}

# build a social network 
Social = nx.Graph()

for nodes in social_g:
    for node in social_g[nodes]:
        Social.add_edge(nodes, node)
        
Social.add_nodes_from(['Siddu', 'Sahil'])
Social.add_edges_from([('Vijay','Sahil'), ('Aryan', 'Sahil'), ('Adya','Sahil')])
Social.add_edge('Sahil','Siddu')
Social.add_edges_from([('Siddu','Vikram'),('Vikram','Tharun'),('Siddu','Tharun')])
print(Social.edges())

# FoFs : Friends of Friends (second degree friend circle)
def FoFs(user : str, Graph : nx.Graph) -> set:

    """
    This function calcuates the first degree mutual friends and will return set of those users.

    Returns:
        set: set of mutual friends
    """
    if user not in Graph.nodes():
        raise(Exception("No such user"))
    connection = list(Graph.neighbors(user)) # stores the list of neighbors
    mutconnlist = list(set(Graph.neighbors(x)) for x in connection) # stores the list of list of neigbors 
    
    # create a set to store all connections
    totalconn = set()
    for friends in mutconnlist:
        for indivdual in friends:
            totalconn.add(indivdual)
            
    # remove already known connections
    totalconn = totalconn - set(connection)
    totalconn.remove(user) # remove the user
    return totalconn

print(FoFs('Aryan', Social))


nx.draw_spring(Social, with_labels=True)
plt.show()