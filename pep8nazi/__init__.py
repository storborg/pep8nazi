import __builtin__
import sys
import os.path
import inspect
import collections
import pep8


orig_import = __import__


class PEP8Error(SyntaxError):
    pass


def check(filename):
    pep8.process_options(['-qq', filename])
    pep8.input_file(filename)
    return pep8.get_error_statistics(), pep8.get_warning_statistics()


def new_import(fullname, *args, **kwargs):
    ret = orig_import(fullname, *args, **kwargs)
    mod = sys.modules[fullname]
    if fullname == 'locale':
        # We need to whitelist this because it gets imported in the pep8
        # checking process, so otherwise it will loop and loop and loop...
        return ret

    filename = inspect.getsourcefile(mod)

    if filename.endswith('.pyc'):
        filename = filename[:-1]

    if os.path.exists(filename):
        error_stats, warning_stats = check(filename)
        if error_stats or warning_stats:
            raise PEP8Error("Cannot import %s due to PEP8 violations. "
                            "Sorry, what I mean is won't. COME ON!" %
                            fullname)
    return ret


__builtin__.__import__ = new_import
