from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pybotvac")
except PackageNotFoundError:  # package not installed
    __version__ = "unknown"
