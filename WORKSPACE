load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


http_archive(
    name = "rules_python",
    sha256 = "a30abdfc7126d497a7698c29c46ea9901c6392d6ed315171a6df5ce433aa4502",
    strip_prefix = "rules_python-0.6.0",
    url = "https://github.com/bazelbuild/rules_python/archive/0.6.0.tar.gz",
)

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "85ffff62a4c22a74dbd98d05da6cf40f497344b3dbf1e1ab0a37ab2a1a6ca014",
    strip_prefix = "rules_docker-0.23.0",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.23.0/rules_docker-v0.23.0.tar.gz"],
)

load("@rules_python//python:pip.bzl", "pip_install")

# Create a central external repo, @my_deps, that contains Bazel targets for all the
# third-party packages specified in the requirements.txt file.
pip_install(
    name = "app",
    requirements = "//app:requirements.txt",
)


# OPTIONAL: Call this to override the default docker toolchain configuration.
# This call should be placed BEFORE the call to "container_repositories" below
# to actually override the default toolchain configuration.
# Note this is only required if you actually want to call
# docker_toolchain_configure with a custom attr; please read the toolchains
# docs in /toolchains/docker/ before blindly adding this to your WORKSPACE.
# BEGIN OPTIONAL segment:
load("@io_bazel_rules_docker//toolchains/docker:toolchain.bzl",
    docker_toolchain_configure="toolchain_configure"
)

docker_toolchain_configure(
  name = "docker_config",
  # OPTIONAL: Bazel target for the build_tar tool, must be compatible with build_tar.py
  # build_tar_target="<enter absolute path (i.e., must start with repo name @...//:...) to an executable build_tar target>",
  # OPTIONAL: Path to a directory which has a custom docker client config.json.
  # See https://docs.docker.com/engine/reference/commandline/cli/#configuration-files
  # for more details.
  # client_config="<enter absolute path to your docker config directory here>",
  # OPTIONAL: Path to the docker binary.
  # Should be set explicitly for remote execution.
  # docker_path="<enter absolute path to the docker binary (in the remote exec env) here>",
  # OPTIONAL: Path to the gzip binary.
  # gzip_path="<enter absolute path to the gzip binary (in the remote exec env) here>",
  # OPTIONAL: Bazel target for the gzip tool.
  # gzip_target="<enter absolute path (i.e., must start with repo name @...//:...) to an executable gzip target>",
  # OPTIONAL: Path to the xz binary.
  # Should be set explicitly for remote execution.
  #xz_path="<enter absolute path to the xz binary (in the remote exec env) here>",
  # OPTIONAL: Bazel target for the xz tool.
  # Either xz_path or xz_target should be set explicitly for remote execution.
  # xz_target="<enter absolute path (i.e., must start with repo name @...//:...) to an executable xz target>",
  # OPTIONAL: List of additional flags to pass to the docker command.
  # docker_flags = [
  #  "--tls",
  #  "--log-level=info",
  # ],

)
# End of OPTIONAL segment.

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")
load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

container_deps()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)


container_pull(
  name = "java_base",
  registry = "gcr.io",
  repository = "distroless/java",
  # 'tag' is also supported, but digest is encouraged for reproducibility.
  digest = "sha256:deadbeef",
)

container_repositories()

_py_image_repos()