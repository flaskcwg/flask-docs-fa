<div align="center">

[![Tests](https://github.com/flaskcwg/flask-docs-fa/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/flaskcwg/flask-docs-fa/actions/workflows/tests.yaml)
[![Documentation Status](https://readthedocs.org/projects/flask-fa/badge/?version=latest)](https://flask-fa.readthedocs.io)
[![Discord Community](https://img.shields.io/discord/918444189400846336.svg?&logo=Discord&style=flat-square)](https://discord.gg/svFmgBXY9d)
[![Translation progress](https://jalkhov.github.io/docspro/badge/fa_progress.svg)](https://github.com/Jalkhov/docspro)
</div>

<div dir="rtl">

# ترجمه مستندات فلاسک(Flask)

## راهنمای مشارکت

### نصب

* روی دکمه [Fork](https://github.com/flaskcwg/flask-docs-fa/fork) برای گرفتن یک انشعاب از این مخزن کلیک کنید
* انشعاب مخزن را به صورت محلی شبیه سازی کنید [^1] (نام کاربری خود را با `{username}` جایگزین کنید):

</div>

```
$ git clone https://github.com/{username}/flask-docs-fa
$ cd flask-docs-fa
$ git remote add upstream https://github.com/flaskcwg/flask-docs-fa
```

<div dir="rtl">

* یک محیط مجازی ایجاد کنید و ملزومات را نصب کنید

برای Linux/macOS:

</div>

```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip setuptools
$ pip install -r requirements/dev.txt
$ pip install -e .
$ pre-commit install
```

<div dir="rtl">

برای Windows:

</div>

```
> python -m venv env
> env\Scripts\activate
> python -m pip install --upgrade pip setuptools
> pip install -r .\requirements\dev.txt
> pip install -e .
> pre-commit install
```

<div dir="rtl">

### نرم افزار های پیشنهادی برای ترجمه

همانطور که در زیر توضیح داده شده است، ترجمه ها با استفاده از فایل های .po انجام می شود. [POEdit](https://poedit.net/) یک نرم افزار خوب برای اینکار است. ( نباید با POEditor اشتباه گرفته شود.

### ترجمه

 لطفا قبل از شروع ترجمه یک [issue](https://git.io/JStRB) با نام ترجمه بخش درخواستی خودتان ایجاد کنید.

* پس از آن که در issue درخواست ترجمه شما پذیرفته شد، یک شاخه جدید به صورت محلی ایجاد کنید (حتما نام شاخه را بروزرسانی کنید. , به عنوان مثال, translate-cli ):

#### ابزار های پیشنهادی ترجمه

شما میتونید از ابزار های زیر برای ترجمه استفاده کنید:

* مترجم گوگل: [Google Translate](https://translate.google.com/)
* مترجم ترگمان: [Targoman](https://targoman.ir/)

> __**نکته**__ لطفا در هنگام ارسال pr، ماشینی بودن یا نبودن ترجمه را ذکر کنید.

</div>

```
$ git fetch upstream
$ git checkout -b your-branch-name upstream/main
```

<div dir="rtl">

* فایل های `.po` در دایرکتوری `docs/locales/fa/LC_MESSAGES` ترجمه کنید.

> اگر از یک نرم افزار ترجمه استفاده میکنید نیازی نیست سینتکس نمونه های زیر را بررسی کنید.

نمونه‌ای از یکی از این فایل‌ها، از `docs/.../index.po` ، در زیر آورده شده است.

</div>

```po
#: ../../index.rst:4
msgid "Welcome to Flask"
msgstr "<اینجا را با ترجمه پر کنید.>"
```

<div dir="rtl">

یک مورد دیگر msgid که یک متن چند خطی است و حاوی سینتکس[^5] reStructuredText است:

</div>

```po
#: ../../index.rst:11
msgid ""
"Welcome to Flask's documentation. Get started with :doc:`installation` "
"and then get an overview with the :doc:`quickstart`."
msgstr ""
"اینجا را با ترجمه پر کنید. اینجا را با ترجمه پر کنید. :doc:`installation`"
"اینجا را با ترجمه پر کنید. اینجا را با ترجمه پر کنید. :doc:`quickstart`."
```

<div dir="rtl">

لطفا مراقب باشید که نماد reST را نقض نکنید. [^6]
اکثر [ادیتور های po](https://www.gnu.org/software/trans-coord/manual/web-trans/html_node/PO-Editors.html) میتوانند به شما کمک کنند.

* فصل را به عنوان تمام شده علامت بزنید (چک باکس را با "x" پر کنید):

```
- [x] مثال @نام‌کاربری_شما نام شما
```

* اگر اولین مترجم هستید، `FIRST AUTHOR <EMAIL@ADDRESS>` را در بالای فایل های `.po` با نام و ایمیل خود جایگزین کنید.
* مقدار فیلد «Last-Translator» را در بالای فایل «.po» به‌روزرسانی کنید. (اگر از نرم افزاری مانند poedit استفاده میکنید به اینکار نیازی نیست)
* تغییرات را کامیت کنید:

</div>

```
$ git add docs/locales/fa/LC_MESSAGES/example.po README.md
$ git commit -m "Translate docs/example"
```

<div dir="rtl">

* اسناد [^7] را بسازید و تغییرات را بررسی [^8] کنید:

در Linux یا macOS:

</div>

```
$ cd docs
$ make html
```

<div dir="rtl">

در ویندوز:

</div>

```
> cd docs
> .\make.bat html
```

<div dir="rtl">

`flask-docs-fa/docs/_build/html/index.html` را باز کنید تا اسناد را ببنید.

* اگر همه چیز همانطور که انتظار می رود کار می کند، تغییرات را به GitHub پوش کنید:

</div>

```
$ git push origin your-branch-name
```

<div dir="rtl">

* صفحه اصلی مخزن انشعاب خود را باز کنید، اعلانی در مورد آن خواهید دید شعبه جدید برای ایجاد PR، روی دکمه «Compare & pull request» کلیک کنید.
* سپس PR خود را به Isuse ای که برای ترجمه نوشته اید لینک کنید. برای راحتی میتوانید در PR #شماره_issue را بنویسید.
* هماهنگ کننده ترجمه به زودی PR شما را بررسی خواهد کرد. متشکرم!

## فهرست کارهای ترجمه

مطمئن شوید که هر بار فقط یک فصل را علامت گذاری کنید، در صورت اتمام فصل اول، یکی دیگر را علامت بزنید تا PR ایجاد شود. مگر اینکه فصل طولانی باشد، ممکن است تکلیف[^9] را بازنشانی کنیم.(اگر تا ده روز دیگر ترجمه را تمام نکنید.)

### ترجمه لوگوی فلاسک

</div>

* [X] flask-logo.png [@MDK84](https://github.com/mdk84) MDK

### docs/

* [x] advanced_foreword [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] async-await
* [ ] becomingbig
* [ ] blueprints
* [ ] changes
* [ ] cli
* [ ] config
* [ ] contributing
* [X] debugging [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] design
* [ ] errorhandling
* [X] extensiondev [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [x] extensions [@mdk84](https://github.com/mdk84) MDK
* [x] foreword [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] htmlfaq
* [x] index [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [x] installation [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [X] logging [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [X] quickstart [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] reqcontext
* [ ] security
* [ ] server
* [ ] shell
* [ ] signals
* [X] templating [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] testing
* [ ] views

### docs/tutorial/ [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh

* [x] blog
* [x] database
* [x] deploy
* [x] factory
* [x] index
* [x] install
* [x] layout
* [x] next
* [x] static
* [x] templates
* [X] tests
* [x] views

### docs/deploying/

* [ ] asgi
* [ ] cgi
* [ ] fastcgi
* [ ] index
* [ ] mod_wsgi
* [ ] uwsgi
* [ ] wsgi-standalone

### docs/patterns/ [@mmdbalkhi](https://github.com/mmdbalkhi/)  Komeil Parseh

* [X] appdispatch [@mmdbalkhi](https://github.com/mmdbalkhi/)  Komeil Parseh)
* [X] appfactories
* [ ] caching
* [ ] celery
* [ ] deferredcallbacks
* [ ] distribute
* [ ] fabric
* [ ] favicon
* [ ] fileuploads
* [ ] flashing
* [X] index [@mmdbalkhi](https://github.com/mmdbalkhi/)  Komeil Parseh
* [ ] jquery
* [ ] lazyloading
* [ ] methodoverrides
* [ ] mongoengine
* [X] packages [@mmdbalkhi](https://github.com/mmdbalkhi/)  Komeil Parseh
* [ ] requestchecksum
* [ ] singlepageapplications
* [ ] sqlalchemy
* [ ] sqlite3
* [ ] streaming
* [ ] subclassing
* [ ] templateinheritance
* [ ] urlprocessors [@mmdbalkhi](https://github.com/mmdbalkhi/)  Komeil Parseh
* [ ] viewdecorators
* [ ] wtforms

## docs/api

* [ ] L0~L1000
* [ ] L1000~L1500
* [ ] L1500~L2000
* [ ] L2000~L2500
* [ ] L2500~L3000
* [ ] L3000~L3500
* [ ] L3500~L4000
* [ ] L4000~L4500
* [ ] L4500~L5000
* [ ] L5000~L5500
* [ ] L5500~L6000
* [ ] L6000~L6500

</div>

## یاداشت ها و پی نوشت

[^1]: Clone your fork repository locally
[^2]: self-assignment
[^3]: ToDo
[^4]: مخفف Pull request
[^5]: Syntax
[^6]: Please be careful not to break reST notation
[^7]: docs/documents
[^8]: preview
[^9]: assignment

[discord server](https://discord.gg/svFmgBXY9d)

</div>
