from hemingway.automatic_replacer import AutomaticReplacer


class AutomaticShellReplacer(AutomaticReplacer):
    '''Applies all suggestions to the original tree

    Applies the default suggestion without asking the developer 
    for confirmation, but shows info on stdout
    '''

    show_stdout = True
