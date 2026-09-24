from importlib.metadata import PackageNotFoundError, version

# The version is composed at build time (see _pickle_version.py at the repo
# root) as upstream's 0.0.22 plus a PEP 440 local segment,
# +pickle.<release>[.<branch>], and baked into the wheel's metadata. Read it
# back from there so an installed urdfpy reports exactly the version of the
# wheel it came from.
try:
    __version__ = version("urdfpy")
except PackageNotFoundError:
    # Imported straight from a source checkout that was never installed
    # (e.g. the Sphinx build puts the repo root on sys.path), so there is no
    # metadata to read. Same placeholder setuptools-scm uses in this case.
    __version__ = "0+unknown"
