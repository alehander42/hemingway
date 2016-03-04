#hemingway

*write drunk, edit sober* - Ernest Hemingway

## unfinished: work in progress 


a tool for automated/semi-automated refactoring and dry-ing of your code:

```bash
hemingway example.py
```

```
Found 1 duplication
```

Hemingway has two modes of operation:
  `automatic` which is fully automated and uses certain heuristics and conventions to
  refactor your not-so-dry code

  `interactive` which still find automatically similar code  asks the programmer for important decisions
  in the refactoring process

Example of `automatic` mode:

```bash
hemingway example.py -a #-a / --automatic is the default mode

Found 2 cases of similar code:

#1

e = t(x, 4) #2
f = z(x, 4) #3

Refactored <0>(<1>, 4) to

def call_with_4(function, arg):
	return function(arg, 4)

e = call_with_4(t, x)
f = call_with_4(z, x)

#2

e = [l for l in t if even(l)]
f = [m for m in z if even(m)]
x = [a + 4 for a in z if even(a)]

Refactored [<0> for <1> in <2> if even(<1>)] to
def filter_even_map(sequence, mapping):
	return [mapping(a) for a in sequence if even(a)]

e = filter_even_map(t, lambda l: l)
f = filter_even_map(z, lambda m: m)
x = filter_even_map(z, lambda a: a + 4)
```

Example of `interactive` mode
```bash
hemingway example.py -i #-i / --interactive can be setup as default in .hemingway.yaml
```

## configuration

you can setup a .hemingway.yaml file in the directory where you run it from
or in your home folder

```yaml
default_mode: automatic # can be interactive
aggresiveness: high     # can be medium or low
```

## how does it work

```python

Python AST ==Pattern Finder==> 
Patterns   ==RefactoringEngine==>
Refactoring Suggestions 
  ==AutomaticReplacer==> displays info and generates the refactored code
  ==InteractiveReplacer==> shows suggestions to the programmer with OK/do-that-instead dialogs
```

## license

MIT License, Alexander Ivanov, 2016

 