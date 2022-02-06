load("@app//:requirements.bzl", "entry_point", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

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

py_test(
    name = "test",
    srcs = [
        "test.py",
        "entry.py",
        "main.py",
    ],
    deps = [
        ":api",
        requirement("pytest"),
        requirement("curio")
    ],
)

py3_image(
    name = "docker_api",
    srcs = [
        "entry.py",
        "main.py",
    ],
    main = "entry.py",
    layers = [
        requirement("fastapi"),
        requirement("uvicorn"),
    ],
)
