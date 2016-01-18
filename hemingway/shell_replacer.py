from hemingway.interactive_replacer import InteractiveReplacer
import re

class ShellReplacer(InteractiveReplacer)
    
    YES_REGEX = re.compile(r'[Yy]([Ee][Ss])?')

    def suggestion_dialog(self, suggestion):
        print('Found %d repetitions of\n%s:' % (
            len(suggestion.call_sites),
            suggestion.node.dumps()))
        print('Refactor into\n%s\n?\n' % suggestion.function.dumps() +
              'type Y/Yes\tname (to change the name)\n')
        responce = input()
        if self.is_yes(responce):
            return True, []
        else:
            return False, {'name': responce}

    def is_yes(self, responce):
        return re.match(responce) is not None
