import json
class Template:
    def __init__(self, templates):
        self.pos = templates["pos"]
        self.neg = templates["neg"]
    
    def to_dict(self):
        return {"pos": self.pos, "neg": self.neg}

class Node:
    end = False
    children = []
    def __init__(self, concept_name, templates, parent, children, labeled=0):
        self.concept_name = concept_name
        self.template = Template(templates)
        self.parent = parent
        self.children = children if children else []
        self.labeled = labeled

    def to_dict(self):
        """
        Return the tree structure as a dict
        """
        return {
            "concept_name": self.concept_name,
            "template": self.template.to_dict(),
            "labeled": self.labeled,
            "children": [child.to_dict() for child in self.children]
        }

    def __str__(self):
        """
        Print the tree structure with json format
        """
        self_dict = self.to_dict()
        return json.dumps(self_dict, indent=4, ensure_ascii=False)

    def write(self):
        """
        Write some semantic sentences with labels
        """
        label_decision = 1 if self.labeled else 0
        return [
            (self.template.pos.format(self.concept_name), label_decision),
            (self.template.neg.format(self.concept_name), 1-label_decision)
        ]