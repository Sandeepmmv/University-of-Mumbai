import networkx as nx
import matplotlib.pyplot as plt

family_tree = nx.DiGraph()

def male(person):
    return ("gender", "male")
def female(person):
    return ("gender", "female")
def parent(child, parent):
    return ("child", child, "parent", parent)
def father(child, father):
    return (male(father), parent(child, father))
def mother(child, mother):
    return (female(mother), parent(child, mother))
def grandfather(grandchild, grandfather):
   return (male(grandfather), parent(grandchild, parent(child, father)))
def grandmother(grandchild, grandmother):
    return (female(grandmother), parent(grandchild, parent(child, mother)))
def brother(person1, person2):
    return (male(person2), parent(person1, parent(child, parent2)))
def sister(person1, person2):
    return (female(person2), parent(person1, parent(child, parent2)))
def uncle(nephew_niece, uncle):
    return (male(uncle), brother(parent(nephew_niece, parent(child, parent2)), uncle))
def aunt(nephew_niece, aunt):
    return (female(aunt), sister(parent(nephew_niece, parent(child, parent2)), aunt))
def nephew_niece(nephew_niece, aunt_uncle):
    return (child(nephew_niece, parent(child, parent2)), aunt_uncle)
def cousin(cousin1, cousin2):
    return (child(cousin1, parent(child, parent2)), child(cousin2, parent(child, parent2)))

family_tree.add_edge("John", "Samantha")
family_tree.add_edge("John", "Robert")
family_tree.add_edge("Robert", "Ella")
family_tree.add_edge("Samantha", "Sophia")
family_tree.add_edge("Samantha", "Liam")
# Draw the family tree
pos = nx.spring_layout(family_tree, seed=42)
nx.draw(family_tree, pos, with_labels=True, node_size=500, node_color="skyblue", 
font_size=10, font_color="black")
plt.title("Family Tree")
plt.show()