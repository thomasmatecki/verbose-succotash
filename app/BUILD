load("@app//:requirements.bzl", "entry_point", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@npm//tailwindcss:index.bzl", "tailwindcss")


tailwindcss(
    name="tailwind",
    args = [
        "-c", "$(location tailwind.config.js)",
        "-i", "$(location input.css)", 
        "--content", "$(location index.html)", 
        "-o" , "$(@D)/main.css",
    ],
    data = [
        "input.css",
        "index.html",
        "tailwind.config.js",
        "@npm//daisyui"
    ],
    output_dir = True
)

filegroup(
    name = "templates",
    srcs = glob(["templates/**/*.html"]),
)


py_binary(
    name = "api",
    srcs = [
        "entry.py",
        "main.py",
    ],
    args = [
        "main:app",
    ],
    main = "entry.py",
    deps = [
        requirement("fastapi"),
        requirement("uvicorn"),
        requirement("jinja2"),
    ],
    env = {
        "CSS_DIRECTORY": "$(location :tailwind)",
        "TEMPLATE_DIRECTORY": "app/templates"
    },
    data = [
        ":tailwind",
        ":templates"
    ] 
)

py3_image(
    name = "docker-api",
    srcs = [
        "entry.py",
        "main.py",
    ],
    args = [
        "--rm",
        "--",
        "main:app",
    ],
    main = "entry.py",
    layers = [
        requirement("fastapi"),
        requirement("uvicorn"),
    ],
)
