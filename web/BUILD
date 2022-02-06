load("@build_bazel_rules_nodejs//:index.bzl", "nodejs_binary", "npm_package_bin")
load("@npm//tailwindcss:index.bzl", "tailwindcss")

tailwindcss(
    name="tailwind"
)


nodejs_binary(
    name = "bar",
    entry_point = "tailwindcss",
    data = [
      "@npm//tailwindcss",
      "@npm//daisyui",
    ]
)

filegroup(
    name = "entry_file",
    srcs = ["main.js"],

)

nodejs_binary(
    name = "my_binary",
    entry_point = ":entry_file",
)
#npm_package_bin(
#    name = "tailwind",
#    args = [
#        "-i", "src/input.css", 
#        "-o", "./dist/output.css" 
#    ],
#    outs = [
#        "dist/output.css"
#    ],
#    chdir = "web/",
#    data = [
#        "src/index.html",
#        "src/input.css"
#    ],
#    package = "tailwindcss",
#)
#

#nodejs_binary(
#    name = "runtails",
#    data = [
#            "@npm//:node_modules",
#        ] + glob(["src/**"]),
#    entry_point = "@npm//:node_modules/tailwindcss/lib/cli.js",
#)