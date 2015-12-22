class Suggestion:
    '''Forms a suggestion for the replacer classes

    Attributes:
        pattern (Pattern): the pattern that is supposed to be refactored
        component: the component that would contain `function`
        function: a function with the refactored pattern
        call_sites(list): all instances of the pattern which would 
                            contain `function` invocations
    '''

    def __init__(self, pattern, component, function, call_sites):
        self.pattern = pattern
        self.component = component
        self.function = function
        self.call_sites = call_sites
