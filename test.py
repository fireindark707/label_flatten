from label_flatten import Tree,Node
import copy

pth = "labor_theme.json"
labels = ["劳动事件"]


tree_template = Tree(pth)
for label in labels:
    new_tree = copy.deepcopy(tree_template)
    labeled_tree = new_tree.give_label(label)
    print(labeled_tree)
    sentences = labeled_tree.write(mode="all")
    for sen in sentences:
        print(sen)
    break