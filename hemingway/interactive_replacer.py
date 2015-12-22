from hemingway.replacer import Replacer


class InteractiveReplacer(Replacer):
    '''Open for subclassing with hooks for interactive suggestion dialogs

    Provides method `suggestion_dialog` which is called with suggestion data
    and expects a {'accept': True/False, 'patches': {..}} result
    '''

    def replace_suggestion(self, suggestion):
        fix = self.suggestion_dialog(suggestion)
        suggestion = copy(suggestion)
        if not fix['accept']:
            for label, name in fix['patches']:
                suggestion.args[label] = name

        self.apply_suggestion(suggestion)
