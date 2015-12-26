import redbaron
from hemingway.similarity_constants import *


class SimilarityMapping:

    @classmethod
    def from_fst(cls, fst, treshhold=2):
        return cls().fst(fs, treshhold)

    def __init__(self):
        self.mapping = {}

    def fst(self, fst, treshhold=2):
        self.treshhold = treshhold
        self._convert_node(fst)
        return self.mapping

    def _convert_node(self, tree):
        if isinstance(tree, redbaron.Node):
            convert = '_convert_%s' % type(tree).__name__.lower()
            if hasattr(self, convert):
                getattr(self, convert)(tree)
            else:
                self._convert_default(node)
        elif isinstance(tree, list):
            map(self._convert_node, tree)
        else:
            self._convert_node(tree)

    def _convert_defnode(self, def_node):
        self.in_def = def_node.name
        self.path.append({'level': 'method', 'name': def_node.name})
        self._convert_block(def_node.value)

    def _convert_default(self, node):
        return (NODE_TYPES[type(node).__name__][:-4],)

    def _convert_classnode(self, class_node):
        self.in_class = class_node.name
        self.path.append({'level': 'class', 'name': class_node.name})
        self._convert_node(class_node.value)

    def _convert_block(self, nodes):
        # convert treshhold to upper_treshhold tuples
        # for now upper treshhold is the max function body cause we believe
        # users are not idiots and will use short functions
        for length in range(self.treshhold, len(nodes)):
            for start in range(len(nodes) - length):
                sub_nodes = nodes[start:start + length]
                next_value = start + 1
