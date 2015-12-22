class Pattern:
    '''Represents a pattern of repeated/similar code

    Attributes:
        node (Node): the node representing the code with
                         placeholders
        args ([Node]): the placeholders
        instances ([Node]): the original pattern instances in code
        local ([Node]): the local placeholders for expressions 
                            from the surrounding region
        inner ([Node]): the inner placeholders existing only in the pattern
    '''

    def __init__(self, node, args, instances):
        self.node = node
        self.args = args
        self.instances = instances
        self.local = [arg for args if not arg.is_inner]
        self.inner = [arg for args if arg.is_inner]
