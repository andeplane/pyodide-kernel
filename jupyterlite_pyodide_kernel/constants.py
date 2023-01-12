"""Well-known (and otherwise) constants used by JupyterLite"""

### pyolite-specific values, will move to separate repo
#: the key for PyPI-compatible API responses pointing to wheels
PIPLITE_URLS = "pipliteUrls"
#: the schema for piplite-compatible wheel index
PIPLITE_INDEX_SCHEMA = "piplite.schema.v0.json"
#: where we put wheels, for now
PYPI_WHEELS = "pypi"
#: the plugin id for the pyolite kernel
PYOLITE_PLUGIN_ID = "@jupyterlite/pyolite-kernel-extension:kernel"

#: where we put wheels, for now
PYODIDE_URL = "pyodideUrl"

#: where we put pyodide, for now
PYODIDE = "pyodide"
PYODIDE_JS = "pyodide.js"
PYODIDE_REPODATA = "repodata.json"
