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
