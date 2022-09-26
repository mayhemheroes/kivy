#!/usr/bin/python3
import atheris
import sys
import pdb

with atheris.instrument_imports():
    from kivy.lang import Parser, ParserException
    from kivy.factory import FactoryException


@atheris.instrument_func
def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    parse_str = fdp.ConsumeUnicode(atheris.ALL_REMAINING)

    try:
        Parser(content=parse_str, filename=None)
    except (FactoryException, ParserException):
        return
    except AttributeError as e:
        if 'First letter' not in str(e):
            raise
    except Exception as e:
        if 'non-rules' not in str(e):
            raise


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
