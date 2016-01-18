import hemingway.pattern_finder 
import hemingway.refactoring_engine
import redbaron

def suggest_refactorings(source):
    fst = redbaron.RedBaron(source)
    patterns = hemingway.pattern_finder.PatternFinder(fst).analyze()
    hemingway.refactoring_engine.RefactoringEngine(fst, patterns)
