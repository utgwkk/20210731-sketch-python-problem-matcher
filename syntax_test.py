# For Python 2 compatibility, we use [glob2](https://pypi.org/project/glob2/) library instead of built-in glob module.
from glob2 import iglob
import py_compile
import pytest

python_files = iglob('src/**/*.py', recursive=True)

@pytest.mark.parametrize("path", python_files)
def test_syntax(path):
    try:
        py_compile.compile(path, doraise=True)
    except py_compile.PyCompileError as ex:
        pytest.fail(ex.msg)

@pytest.mark.flaky(reruns=5)
def test_example():
    import random
    assert random.choice([True, False])
