# Flask Docs Translation


## Contributing Guide


### Installation

- Click the "Fork" button to fork this repository on GitHub.
- Clone your fork repository locally (replace `{username}` with your username):

```
$ git clone https://github.com/{username}/flask-docs-<UPDATE THIS>
$ cd flask-docs-<UPDATE THIS>
$ git remote add upstream https://github.com/<UPDATE THIS>/flask-docs-<UPDATE THIS>
```

- Create a virtual environment and install requirements:

For Linux/macOS:

```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip setuptools
$ pip install -r requirements/dev.txt
$ pip install -e .
$ pre-commit install
```

For Windows:

```
> python -m venv env
> env\Scripts\activate
> python -m pip install --upgrade pip setuptools
> pip install -r .\requirements\dev.txt
> pip install -e .
> pre-commit install
```


### Self-Assignment

- Open <https://github.com/<UPDATE THIS>/flask-docs-<UPDATE THIS>/edit/main/README.md>.
- Find the "Translation To-do List" section, mark the chapter you want to
translate in following format:

```
- [ ] example @your_username Your Name
```

You can link the username to your GitHub profile:

```
- [ ] example [@your_username](https://github.com/your_username) Your Name
```

- Leave a commit message (e.g., "Assign example to @your_username"), then click the
"Propose changes" button to create a PR.

### Recommended Translation software

As explained below, translations are done using .po files. One good editor is
[POEdit](https://poedit.net/) (not to be confused with POEditor)

### Translation

- When the self-assignment PR is merged, create a new branch locally
(be sure to update the example branch name, for example, `translate-cli`):

```
$ git fetch upstream
$ git checkout -b your-branch-name upstream/main
```

- Translate the `.po` file in the `docs/locales/<LANG>/LC_MESSAGES` directory.

An example of one such file, from docs/.../index.po, is given below.

```po
#: ../../index.rst:4
msgid "Welcome to Flask"
msgstr "<FILL HERE BY TARGET LANGUAGE>"
```

Another case, msgid is multi-line text and contains reStructuredText syntax:

```po
#: ../../index.rst:11
msgid ""
"Welcome to Flask's documentation. Get started with :doc:`installation` "
"and then get an overview with the :doc:`quickstart`."
msgstr ""
"FILL HERE BY TARGET LANGUAGE FILL HERE BY TARGET LANGUAGE :doc:`installation` "
"FILL HERE BY TARGET LANGUAGE :doc:`quickstart`."
```

Please be careful not to break reST notation. Most
[po-editors](https://www.gnu.org/software/trans-coord/manual/web-trans/html_node/PO-Editors.html) will help you with that.

- Mark the chapter as finished (fill the checkbox with "x"):

```
- [x] example @your_username Your Name
```

- If you are the first translator, update the `FIRST AUTHOR <EMAIL@ADDRESS>` comment at the top of the `.po` file.
- Update the `Last-Translator` field value at the top of the `.po` file.
- Commit the changes:

```
$ git add docs/locales/<LANG>/LC_MESSAGES/example.po README.md
$ git commit -m "Translate docs/example"
```

- Build the docs and preview the changes:

For Linux/macOS:

```
$ cd docs
$ make html
```

For Windows:

```
> cd docs
> .\make.bat html
```

Open `{project_location}/docs/_build/html/index.html` in your browser to view the docs.

- If everything is working as expected, push the changes to GitHub:

```
$ git push origin your-branch-name
```

- Open the home page of your forked repository, you will see a notice about
the new branch. Click the "Compare & pull request" button to create a PR.
- The translation coordinator will review your PR very soon. Thank you!


## Translation To-do List

Be sure only mark one chapter at a time, mark another one when the former
PR is created. Unless it's a long chapter, we may reset the assignment
if you doesn't finish the translation in ten days.


### docs/

- [ ] advanced_foreword (reserved)
- [ ] appcontext
- [ ] async-await
- [ ] becomingbig
- [ ] blueprints
- [ ] changes
- [ ] cli
- [ ] config
- [ ] contributing
- [ ] debugging
- [ ] design
- [ ] errorhandling
- [ ] extensiondev
- [ ] extensions
- [ ] foreword (reserved)
- [ ] htmlfaq
- [ ] index (reserved)
- [ ] installation (reserved)
- [ ] logging
- [ ] quickstart (reserved)
- [ ] reqcontext
- [ ] security
- [ ] server
- [ ] shell
- [ ] signals
- [ ] templating
- [ ] testing
- [ ] views


### docs/tutorial/ (reserved)

- [ ] blog
- [ ] database
- [ ] deploy
- [ ] factory
- [ ] index
- [ ] install
- [ ] layout
- [ ] next
- [ ] static
- [ ] templates
- [ ] tests
- [ ] views


### docs/deploying/

- [ ] asgi
- [ ] cgi
- [ ] fastcgi
- [ ] index
- [ ] mod_wsgi
- [ ] uwsgi
- [ ] wsgi-standalone


### docs/patterns/

- [ ] appdispatch
- [ ] appfactories
- [ ] caching
- [ ] celery
- [ ] deferredcallbacks
- [ ] distribute
- [ ] fabric
- [ ] favicon
- [ ] fileuploads
- [ ] flashing
- [ ] index
- [ ] jquery
- [ ] lazyloading
- [ ] methodoverrides
- [ ] mongoengine
- [ ] packages
- [ ] requestchecksum
- [ ] singlepageapplications
- [ ] sqlalchemy
- [ ] sqlite3
- [ ] streaming
- [ ] subclassing
- [ ] templateinheritance
- [ ] urlprocessors
- [ ] viewdecorators
- [ ] wtforms


## docs/api

- [ ] L0~L1000
- [ ] L1000~L1500
- [ ] L1500~L2000
- [ ] L2000~L2500
- [ ] L2500~L3000
- [ ] L3000~L3500
- [ ] L3500~L4000
- [ ] L4000~L4500
- [ ] L4500~L5000
- [ ] L5000~L5500
- [ ] L5500~L6000
- [ ] L6000~L6500
