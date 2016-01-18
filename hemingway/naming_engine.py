OPNAMES = {'+': 'add', '-': 'substact',
           '*': 'multiply', '/': 'divide', '**': 'power'}


class NamingEngine:

    def __init__(self, tree):
        self.tree = tree
        self.helper_count = 0

    def function_name(self, pattern):
        if pattern.is_expression and pattern.node.type == 'listcomp':
            return 'map_%s' % self.extract_body_description(pattern)
        else:
            return self.new_helper_name()

    def extract_body_description(self, pattern):
        if hasattr(pattern.node, 'body'):
            if len(pattern.node.body) == 1:
                expr = pattern.node.body[0]
                if expr.type == 'call':
                    return expr.function
                elif expr.type == 'binop':
                    return OPNAMES[expr.op]
        return str(node.body.dumps()[:2])

    def new_helper_name(self):
        name = 'helper_%d' % self.helper_count
        self.helper_count += 1
        return name
