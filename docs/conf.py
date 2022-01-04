import packaging.version
from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = "Flask"
copyright = "2010 Pallets"
author = "Pallets"
release, version = get_version("Flask")

# General --------------------------------------------------------------

master_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
    "sphinx_issues",
    "sphinx_tabs.tabs",
]
autodoc_typehints = "description"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "werkzeug": ("https://werkzeug.palletsprojects.com/", None),
    "click": ("https://click.palletsprojects.com/", None),
    "jinja": ("https://jinja.palletsprojects.com/", None),
    "itsdangerous": ("https://itsdangerous.palletsprojects.com/", None),
    "sqlalchemy": ("https://docs.sqlalchemy.org/", None),
    "wtforms": ("https://wtforms.readthedocs.io/", None),
    "blinker": ("https://pythonhosted.org/blinker/", None),
}
issues_github_path = "pallets/flask"

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_theme_options = {"index_sidebar_logo": False}
html_context = {
    "project_links": [
        ProjectLink("حمایت مالی", "https://palletsprojects.com/donate"),
        ProjectLink("نسخه های منتشر شده در PyPi", "https://pypi.org/project/Flask/"),
        ProjectLink("سورس کد", "https://github.com/pallets/flask/"),
        ProjectLink("گزارش مشکلات", "https://github.com/pallets/flask/issues/"),
        ProjectLink("وب‌سایت", "https://palletsprojects.com/p/flask/"),
        ProjectLink("توییتر", "https://twitter.com/PalletsTeam"),
        ProjectLink("چت", "https://discord.gg/pallets"),
        ProjectLink(
            "سورس کد ترجمه مستنندات", "https://github.com/flaskcwg/flask-docs-fa"
        ),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_static_path = ["_static"]
html_favicon = "_static/flask-icon.png"
html_logo = "_static/flask-icon.png"
html_title = f"مستندات فلاسک ({version})"
html_show_sourcelink = False

# custom css ----------------------------------------------------------

html_css_files = [
    "css/custom.css",
]

# LaTeX ----------------------------------------------------------------

latex_documents = [(master_doc, f"Flask-{version}.tex", html_title, author, "manual")]

# Local Extensions -----------------------------------------------------


def github_link(name, rawtext, text, lineno, inliner, options=None, content=None):
    app = inliner.document.settings.env.app
    release = app.config.release
    base_url = "https://github.com/pallets/flask/tree/"

    if text.endswith(">"):
        words, text = text[:-1].rsplit("<", 1)
        words = words.strip()
    else:
        words = None

    if packaging.version.parse(release).is_devrelease:
        url = f"{base_url}main/{text}"
    else:
        url = f"{base_url}{release}/{text}"

    if words is None:
        words = url

    from docutils.nodes import reference
    from docutils.parsers.rst.roles import set_classes

    options = options or {}
    set_classes(options)
    node = reference(rawtext, words, refuri=url, **options)
    return [node], []


def setup(app):
    app.add_role("gh", github_link)


# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language
language = "fa"
"""https://www.sphinx-doc.org/en/master/usage/configuration.html\
        #confval-html_search_language
"""
html_search_language = "fa"
locale_dirs = ["locales"]  # path is example but recommended.
gettext_compact = False  # optional.
