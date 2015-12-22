from hemingway.pattern import Pattern
import redbaron


class PatternFinder:

    def __init__(self, tree):
        self.tree = tree

    def analyze(self):
        '''
        analyzes the tree for repeated patterns
        and returns a list of Pattern objects 
        corresponding to all patterns with their tree instances
        two types of patterns: one-line(expressions) and multiline(block)
        '''
        self._patterns = []
        self.analyze_node(self.tree.data)
        return self._patterns
