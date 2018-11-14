import re
import sys

assert_re = r"Assert\.([\w]+)\((.*?)(?:, ?([\w.()=> [\]]*))?\);?"

def main():
    write(read())

def read():
    with open(sys.argv[1]) as fp:
        return [m for m in re.finditer(assert_re, fp.read())]

def write(tests):
    factory = {
        "Equal": _equal,
        "Null": _null,
        "NotNull": _not_null,
        "NotEqual": _not_equal,
        "False": _false,
        "True": _true,
        "Single": _single,
        "Contains": _contains
    }

    with open('tests_fluent.txt', 'w') as fp:
        for match in tests:
            groups = match.groups()
            fp.write(factory[groups[0]](*groups[1:]))

def _not_null(subject, *args):
    return "{0}.Should().NotBeNull();\n".format(subject)

def _null(subject, *args):
    return "{0}.Should().BeNull();\n".format(subject)

def _equal(equal_to, subject, *args):
    return "{0}.Should().Be({1});\n".format(subject, equal_to)

def _not_equal(not_equal_to, subject, *args):
    return "{0}.Should().NotBe({1});\n".format(subject, not_equal_to)

def _false(subject, *args):
    return "{0}.Should().BeFalse();\n".format(subject)

def _true(subject, *args):
    return "{0}.Should().BeTrue();\n".format(subject)

def _single(subject, *args):
    return "{0}.Should().ContainSingle();\n".format(subject)

def _contains(substring, subject, *args):
    return "{0}.Should().Contain({1});\n".format(subject, substring)

if __name__ == '__main__':
    main()
