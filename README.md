# chatgptimage2-org

Python metadata and integration helper package for [chatgptimage2.org](https://chatgptimage2.org).

`chatgptimage2-org` provides a small, importable Python layer for ChatGPT Image 2 blog publishing, website metadata, and Python automation workflows. The
package is intentionally lightweight, but the published metadata is complete:
it exposes the production website URL, documentation URL, source repository,
local repository path, content path, and Next.js app path used by the site.

This package is useful as a stable integration point for scripts that generate
content, inspect website structure, publish MDX files, or attach site metadata
to automation output. It follows the same package-page pattern used by broader
SDK-style placeholder packages: clear installation instructions, concrete usage
examples, package metadata, and direct links back to the target website.

## Installation

Install from PyPI:

```bash
pip install chatgptimage2-org
```

Upgrade to the latest published version:

```bash
pip install --upgrade chatgptimage2-org
```

## Quick Start

```python
from chatgptimage2_org import HOMEPAGE, hello, get_site_info

print(hello())
print(HOMEPAGE)
print(get_site_info())
```

Expected output includes the public website URL:

```text
https://chatgptimage2.org
```

## Metadata API

The package exposes simple constants for direct imports:

```python
from chatgptimage2_org import (
    HOMEPAGE,
    DOCUMENTATION,
    PACKAGE,
    REPOSITORY,
    LOCAL_REPOSITORY,
    CONTENT_PATH,
    APP_PATH,
)
```

You can also retrieve everything at once:

```python
from chatgptimage2_org import get_site_info

site = get_site_info()

print(site["name"])
print(site["homepage"])
print(site["content_path"])
print(site["app_path"])
```

Returned metadata:

```python
{
    "name": "chatgptimage2.org",
    "homepage": "https://chatgptimage2.org",
    "documentation": "https://chatgptimage2.org/docs",
    "package": "chatgptimage2-org",
    "repository": "https://github.com/youram470-art/chatgptimage2-org-python",
    "local_repository": "/Users/mac/Documents/code/chatgptimage",
    "content_path": "content/blog",
    "app_path": "src/app",
}
```

## Automation Example

The metadata can be used in release scripts, blog generators, indexing tools, or
site maintenance commands:

```python
from pathlib import Path
from chatgptimage2_org import get_site_info

site = get_site_info()
content_dir = Path(site["local_repository"]) / site["content_path"]
app_dir = Path(site["local_repository"]) / site["app_path"]

print(f"Website: {site['homepage']}")
print(f"Content directory: {content_dir}")
print(f"Next.js app directory: {app_dir}")
```

## Use Cases

- Keep a Python package name reserved for ChatGPT Image 2 related tooling.
- Provide a clean PyPI page that points back to https://chatgptimage2.org.
- Share website metadata across scripts without duplicating hard-coded paths.
- Support ChatGPT Image 2 content publishing, blog metadata, and site integration scripts.
- Help publishing tools locate `content/blog` and `src/app` consistently.

## Project Layout

The related website project is organized around local content and Next.js app
routes:

```text
Local repository: /Users/mac/Documents/code/chatgptimage
Content path:     content/blog
Next.js app path: src/app
```

Use it when a Python tool needs to identify the ChatGPT Image 2 site, locate its blog content directory, or attach source and homepage links to generated publishing output.

## Links

- Website: https://chatgptimage2.org
- Documentation: https://chatgptimage2.org/docs
- Source: https://github.com/youram470-art/chatgptimage2-org-python
- PyPI: https://pypi.org/project/chatgptimage2-org/

## License

MIT
