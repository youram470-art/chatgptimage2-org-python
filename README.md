# chatgptimage2-org

Python metadata package for [chatgptimage2.org](https://chatgptimage2.org).

`chatgptimage2-org` exposes a small set of website metadata for the ChatGPT
Image 2 site. It keeps automation scripts aligned with the public URL, blog
content path, and Next.js application path.

## Installation

```bash
pip install chatgptimage2-org
```

## Usage

```python
from chatgptimage2_org import HOMEPAGE, get_site_info, hello

print(hello())
print(HOMEPAGE)
print(get_site_info())
```

## Site Metadata

- Website: https://chatgptimage2.org
- Local repository: `/Users/mac/Documents/code/chatgptimage`
- Content path: `content/blog`
- Next.js app path: `src/app`
- Source: https://github.com/youram470-art/chatgptimage2-org-python

## License

MIT
