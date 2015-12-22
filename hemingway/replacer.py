class Replacer:
	'''Applies refactoring suggestions to the original code

	Attributes:
	    tree (Node): the fst of the original code
	    suggestions ([Suggestion]): the suggestions
	'''

    def __init__(self, tree, suggestions):
        self.tree = tree
        self.suggestions = suggestions

    def replace(self):
        for suggestion in self.suggestions:
            self.replace_suggestion(suggestion)

        return self.tree.dumps()

    def replace_suggestion(self, suggestion):
        raise NotImplementedError("implement replace_suggestion")
