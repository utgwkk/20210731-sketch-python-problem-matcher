from glob import glob
import py_compile
import pytest

python_files = glob('*.py', recursive=True)

@pytest.mark.parametrize("path", python_files)
def test_syntax(path):
    try:
        py_compile.compile(path, doraise=True)
    except py_compile.PyCompileError as ex:
        pytest.fail(ex.msg)
