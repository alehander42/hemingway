from hemingway.pattern import Pattern
from hemingway.suggestion import Suggestion
from hemingway.naming_engine import NamingEngine
from redbaron import Node


class RefactoringEngine:

    def __init__(self, tree, patterns):
        self.tree = tree
        self.patterns = patterns
        self.naming_engine = NamingEngine(self)

    def refactor(self):
        '''
        returns refactoring suggestions
        they are the best guesses where to put in the tree
        '''
        return map(self.refactor_pattern, self.patterns)

    def refactor_pattern(self, pattern):
        '''
        suggests how to refactor, what names to use and a
        place to put in the tree
        '''
        if pattern.is_expression:
            common_base = self.find_common_base(pattern)
            function = self.construct_function(pattern)
            matches = [self.refactor_into_call(
                instance, pattern, function.name) for instance in pattern.instances]
            return Suggestion(pattern, common_base, function, matches)
        else:
            return Suggestion(pattern, None, None, [])

    def find_common_base(self, pattern):
        ''' if in same class, return the class 
        elif in same hierarchy, return the lowest common parent 
        elif in same module, return the module
        else, invent a helpers module
        '''
        base = None
        for instance, next_instance in zip(pattern.instances[:-1], pattern.instances[1:]):
            if instance.path[-1] == next_instance.path[-1]:
                base = base or instance.path[-1]
            elif set(instance.path[-1].parents) & set(next_instance.path[-1].parents):
                common = list(
                    set(instance.path[-1].parents) & set(next_instance.path[-1].parents))[0]
                if base is None or base.level == 'class' and common in base.parents:
                    base = common
                elif base.level == 'class':
                    return

    # Node{}
    def refactor_into_call(self, instance, pattern, function_name):
        return {'type': 'call', 'function': function_name, 'args': instance.vars}

    # pattern:
    #   instances: [x = [<0> for <0> in <1> if even(<0>)]]
    #   node: [<0> for <0> in <1> if even(<0>)]
    #   args: <0>, <1>
    #   local: <1>
    #   inner: <0>
    def construct_function(self, pattern):
        function_arg_names = [self.naming_engine.var_name(
            pattern.node, l) for l in pattern.local]
        args = {'type': 'args',
                'args': [{'type': 'arg', 'name': name} for name in function_arg_names]}
        inner_names = [self.naming_engine.var_name(
            pattern.node, l) for l in pattern.inner]
        arg_names = [self.naming_engine.var_name(
            patter.node, a) for a in pattern.args]
        body = self.replace_names(pattern.node, arg_names)
        return {'type': 'function',
                'name': self.naming_engine.function_name(pattern),
                'args': args,
                'body': body}
