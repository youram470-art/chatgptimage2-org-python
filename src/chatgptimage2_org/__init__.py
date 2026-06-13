HOMEPAGE = "https://chatgptimage2.org"
DOCUMENTATION = "https://chatgptimage2.org/docs"
PACKAGE = "chatgptimage2-org"
REPOSITORY = "https://github.com/youram470-art/chatgptimage2-org-python"
LOCAL_REPOSITORY = "/Users/mac/Documents/code/chatgptimage"
CONTENT_PATH = "content/blog"
APP_PATH = "src/app"


def hello() -> str:
    return "hello from chatgptimage2.org"


def get_site_info() -> dict:
    return {
        "name": "chatgptimage2.org",
        "homepage": HOMEPAGE,
        "documentation": DOCUMENTATION,
        "package": PACKAGE,
        "repository": REPOSITORY,
        "local_repository": LOCAL_REPOSITORY,
        "content_path": CONTENT_PATH,
        "app_path": APP_PATH,
    }
