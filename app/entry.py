import sys

from uvicorn.main import main

# Ugh -- see: https://github.com/bazelbuild/rules_python/issues/600
if __name__ == "__main__":
    sys.exit(main())
