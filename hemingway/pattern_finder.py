from hemingway.pattern import Pattern
import redbaron


class PatternFinder:
    '''Finds similar code subtrees and abstracts them into patterns

    How?
    Constructs a hash with tuples representing simplified subblock structure
    as keys and subblock objects capturing nodes and context 

    Example:
        e = []
        for f in e:
            e.append(x(f))
        xz = 'V'

    With treshold 2, our similarity hash will contain:

    ((ASSIGNMENT, VAR_0, EMPTY_LIST),
     (FOR, VAR_0, VAR_1, (METHOD_CALL, VAR_0, VAR_2))):
        SubBlock([Node(e = []), Node(for f..)], context..)

    ((FOR, VAR_0, VAR_1, (METHOD_CALL, VAR_0, VAR_2)),
     (ASSIGNMENT, VAR_2, NUMBER)):
        SubBlock([Node(for f..), Node(xz = 'V')], context..)

    etc..,

    The important things:
      * Certain details are ignored: var names don't matter, what matters is
        if you use the same var name in different places in the same subblock,
        that info remains, they are just represented as var_0, var_1..
      * For now, only same-number-of-expressions sub blocks are matched,
        but that's mostly for ease of initial implementation

    That implementation is based on ideas from Ira Baxter & Andrew Yahin's
    "Clone Detection Using Abstract Syntax Trees", http://research.microsoft.com/en-us/um/people/leonardo/icsm98.pdf

    Attributes:
        tree: a redbaron fst of the original code
        _patterns ([Pattern]): a list of the patterns found
    '''

    def __init__(self, tree):
        self.tree = tree

    def analyze(self):
        '''
        analyzes the tree for repeated patterns
        and returns a list of Pattern objects
        corresponding to all patterns with their tree instances
        two types of patterns: one - line(expressions) and multiline(block)
        '''
        self._patterns = []
        self.analyze_node(self.tree.data)
        return self._patterns

    def analyze_node(self, node):
        if
