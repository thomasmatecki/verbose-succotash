load("@app//:requirements.bzl", "entry_point", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

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
    args = ["main:app"],
    deps = [
        requirement("fastapi"),
        requirement("uvicorn"),
    ],
)

py_image(
    name = "docker_api",
    srcs = [
        "entry.py",
        "main.py",
    ],
    main = "entry.py",
    args = ["main:app"],
    deps = [
        requirement("fastapi"),
        requirement("uvicorn"),
    ],
)
