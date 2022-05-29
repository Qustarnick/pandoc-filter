"""
from panflute import *
import sys

all_headers = {}


def action(elem, doc):
    if type(elem) == Header:
        if stringify(elem) in all_headers.keys():
            if all_headers.get(stringify(elem)) == elem.level:
                sys.stderr.write("Repeated headers. Level: " + str(elem.level) + ", text: " + stringify(elem))
        else:
            all_headers[stringify(elem)] = elem.level

    if type(elem) == Header:
        if elem.level <= 3:
            title = [Str(stringify(elem).upper())]
            return Header(*title, level=elem.level)

    if type(elem) == Str:
        if str(elem.text).lower() == "bold":
            title = [Str(elem.text)]
            return Strong(*title)


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
"""

from panflute import *
import sys

headers = {}


def action(elem, doc):
    if isinstance(elem, Header):
        if stringify(elem) in headers and headers.get(stringify(elem)) == elem.level:
            sys.stderr.write("Repeated header: " + stringify(elem) + " (level " + str(elem.level) + ")\n")
        else:
            headers[stringify(elem)] = elem.level
        if elem.level <= 3:
            filler = [Str(stringify(elem).upper())]
            return Header(*filler, level=elem.level)
    if isinstance(elem, Str) and elem.text.lower() == "bold":
        return Strong(*[Str(elem.text)])


def main(doc=None):
    return run_filter(action, doc=doc)


if __name__ == '__main__':
    main()
