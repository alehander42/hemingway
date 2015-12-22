from hemingway.interactive_replacer import InteractiveReplacer


class ShellReplacer(InteractiveReplacer)

    def suggestion_dialog(self, suggestion):
        print('Found %d repetitions of\n%s:' % (
            len(suggestion.call_sites),
            suggestion.node.dumps()))
        print('Refactor into\n%s\n?\n' % suggestion.function.dumps() +
              'type Y/Yes\tname (to change the name)\n')
