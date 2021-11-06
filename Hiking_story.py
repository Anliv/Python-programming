#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define a graph node
class GraphNode:
    def __init__(self, adjacent, data):
        self.data = data
        self.adjacent = adjacent
        
    def is_leaf(self):
        return( len(self.adjacent) == 0 )
        
    def __str__(self):
        return( self.data )
      
# parse each line of the story file
def parse_line(line):
    line.strip()
    line = line.split("|")
    node_name = line[0]
    adjacent_nodes = line[1].split(',')
    text = line [2]
    # YOUR CODE HERE: parse "line" and populate three variables "node_name", "adjacent_nodes", and "text"
    #
    
    # add all except empty strings
    adjacent = []
    for a in adjacent_nodes:
        if a:
            adjacent.append(a.strip())

    return( node_name, adjacent, text )

# load the story from the raw-text file     
def load_story(filename):
    node_dict = {}
    file = open(filename, "r")    
    for l in file:
        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            node_name, adjacent_nodes, text = parse_line(l)   
            node = GraphNode(adjacent_nodes, text)
            node_dict[node_name] = node

    file.close()
    return( node_dict )

# play the game
def play_story(story_dict):    
    story_node = story_dict['START']
    print(story_node)

    while not story_node.is_leaf():
        choice = ord(input())-97
        # YOUR CODE HERE: get user input and convert ordinal (a,b,c) into an integer (0,1,2) called "choice"
        #
        story_node = story_dict[ story_node.adjacent[choice] ]
        print(story_node)

    print("THE END")

story_dict = load_story("3036363030_story.txt") # load story
play_story(story_dict) # play the game


# In[ ]:





# In[ ]:




