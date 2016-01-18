from hemingway.replacer import Replacer


class AutomaticReplacer(Replacer):
    '''Applies all suggestions to the original tree

    Applies the default suggestion without asking the developer 
    for confirmation
    '''
    show_stdout = False
    
    def replace_suggestion(self, suggestion):
        self.apply_suggestion(suggestion)
