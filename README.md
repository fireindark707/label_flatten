# Label-Flatten

Flatten hierarchical concepts or labels system to declarative sentences and labels.

A Python module.

## Example

### Input

Label/Concept Hierarchy

- 主餐 Main Meal 
  - 牛排 Steak
  - 炒羊肉 Stir-fried lamb

- 甜品 Dessert
  - 布丁 Pudding
  - 冰淇淋 Ice cream

Case Label: 牛排 Steak

### Outputs

它是牛排，對的。  
它不是牛排，錯的。  
它是主餐，對的。  
它不是主餐，錯的。  
它是炒羊肉，錯的。  
它不是炒羊肉，對的。  
它不是布丁，錯的。  
它不是布丁，對的。  
它是冰淇淋，錯的。  
它不是冰淇淋，對的。  
它是甜品，錯的。  
它不是甜品，對的。  

It's a steak, right.  
It's not a steak, wrong.  
It's the main meal, right.  
It's not the main meal, wrong.  
It is stir-fried lamb, wrong.  
It is not stir-fried lambb, right.  
It's not pudding, wrong.  
It's not pudding, right.  
It is ice cream, wrong.  
It's not ice cream, right.  
It is dessert, wrong.  
It's not dessert, right.  

> In this module, wrong is 0 and right is 1.

## Install

```
pip install label-flatten
```

## Usage
```python
from label_flatten import Tree,Node
import copy

pth = "example_data.json"
labels = ["辣子鸡丁"]


tree_template = Tree(pth)
for label in labels:
    new_tree = copy.deepcopy(tree_template)
    labeled_tree = new_tree.give_label(label)
    print(labeled_tree)
    sentences = labeled_tree.write(mode="all")
    for sen in sentences:
        print(sen)
```