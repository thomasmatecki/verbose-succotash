load("@app//:requirements.bzl", "entry_point", "requirement")

alias(
    name = "uvicorn",
    actual = entry_point("uvicorn"),
)

py_binary(
    name = "api",
    srcs = [
        "entry.py",
        "main.py",
    ],
    main = "entry.py",
    deps = [
        requirement("fastapi"),
        requirement("uvicorn"),
    ],
)
