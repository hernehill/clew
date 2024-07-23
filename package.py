name = "clew"

version = "0.10.0.hh.1.0.0"

authors = [
    "Martijn Berger",
]

description = """OpenCL wrapper"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_CLEW_ROOT = "{root}"
    env.CLEW_ROOT = "{root}"
    env.CLEW_LOCATION = "{root}"
    env.CLEW_INCLUDE_DIR = "{root}/include"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")


uuid = "repository.clew"
