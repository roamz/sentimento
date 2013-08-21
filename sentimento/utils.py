# -*- coding: utf-8 -*-


def apply_functions(arg, functions):
    return reduce(
        (lambda a, f: f(a)), 
        functions, 
        arg
    )
