from graphviz import Digraph

# Creating the flowchart
flow = Digraph()
flow.attr(rankdir='LR')

# Nodes
flow.node('A', 'Financial Literacy')
flow.node('B', 'Banking Inclusion')
flow.node('C', 'Improved Financial Management')
flow.node('D', 'Enhanced Spending Habits')
flow.node('E', 'Economic Stability')

# Edges
flow.edge('A', 'C')
flow.edge('B', 'C')
flow.edge('C', 'D')
flow.edge('D', 'E')

# Display the flowchart
flow.render('flowchart', format='png', cleanup=True)
