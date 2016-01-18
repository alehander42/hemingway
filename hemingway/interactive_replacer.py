from hemingway.replacer import Replacer


class InteractiveReplacer(Replacer):
    '''Open for subclassing with hooks for interactive suggestion dialogs

    Provides method `suggestion_dialog` which is called with suggestion data
    and expects a {'accept': True/False, 'patches': {..}} result
    '''

    def replace_suggestion(self, suggestion):
        accept, patches = self.suggestion_dialog(suggestion)
        suggestion = copy(suggestion)
        if not accept:
            suggestion.args.update(patches)

        self.apply_suggestion(suggestion)
