import sys

import pytest


def test_simple():
    assert 1 == 2



# if using 'bazel test ...'
if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:]))
