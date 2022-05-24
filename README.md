<div align="center">

[![Documentation Status](https://readthedocs.org/projects/flask-fa/badge/?version=latest)](https://flask-fa.readthedocs.io)
[![Discord Community](https://img.shields.io/discord/918444189400846336.svg?&logo=Discord&style=flat-square)](https://discord.gg/svFmgBXY9d)
[![Translation progress](https://jalkhov.github.io/docspro/badge/fa_progress.svg)](https://github.com/Jalkhov/docspro)

</div>

# ترجمه مستندات فلاسک(Flask)

## راهنمای مشارکت

### نصب

* روی دکمه [Fork](https://github.com/flaskcwg/flask-docs-fa/fork) برای گرفتن یک فورک از این مخزن کلیک کنید
* فورک خودتان را کلون کنید. ( `{username}` را با نام کاربری خودتان جایگزین کنید )

```
$ git clone https://github.com/{username}/flask-docs-fa
$ cd flask-docs-fa
$ git remote add upstream https://github.com/flaskcwg/flask-docs-fa
```

* یک محیط مجازی ایجاد کنید و پیش نیاز ها را نصب کنید

برای Linux/macOS:

```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install --upgrade pip setuptools wheel
$ pip install -r requirements/dev.txt
$ pip install -e .
$ pre-commit install
```

برای Windows:

```
> python -m venv env
> env\Scripts\activate
> python -m pip install --upgrade pip setuptools
> pip install -r .\requirements\dev.txt
> pip install -e .
> pre-commit install
```

### ترجمه

لطفا قبل از شروع ترجمه یک [issue](https://git.io/JStRB) با نام ترجمه بخش درخواستی خودتان ایجاد کنید.

سپس یک برنچ با نام بخشی({name} را با نام برنچ خودتان جایگزین کنید) که میخواهید ترجمه کنید ایجاد کنید:

```
$ git fetch upstream
$ git checkout -b {name} upstream/main
```

و تغییرات خود را در اینجا انجام دهید.

#### نرم افزار های پیشنهادی برای ترجمه

<div dir="rtl">

* [POEdit](https://poedit.net/)
پیشنهاد اصلی ما POEdit است و خیلی از مترجمان از آن استفاده میکنند!

* [lokalize](https://apps.kde.org/lokalize/)
نرم افزاری دیگر از KDE که شاید بخواهید از آن استفاده کنید.

مطمئنا نرم افزار های دیگری نیز برای ویرایش فایل های `po` وجود دارد. برخی از آن برنامه ها را میتوانید از [اینجا](https://alternativeto.net/software/better-po-editor/) بیابید

> __**نکته:**__ استفاده از نرم افزار برای ترجمه الزامی نیست و میتوانید از یک ویرایشگر متن هم استفاده کنید

</div>

#### ابزار های پیشنهادی ترجمه

شما میتونید از ابزار های زیر برای ترجمه استفاده کنید:

* مترجم گوگل: [Google Translate](https://translate.google.com/)
* مترجم ترگمان: [Targoman](https://targoman.ir/)

#### شروع ترجمه

فایل های ترجمه در `docs/locales/fa/LC_MESSAGES` قرار دارد. فایل انتخابی خود با با نرم افزار مورد علاقه خودتان باز کنید و ترجمه را شروع کنید.

اگر از نرم افزار ها برای ترجمه نمیخواهید استفاده کنید، موارد زیر برای شماست:

* فایل .po را اینگونه ترجمه کنید:

```po
#: ../../index.rst:4
msgid "Welcome to Flask"
msgstr "<اینجا را با ترجمه پر کنید.>"
```

البته دقت کنید که بعضی از موارد نباید ترجمه شوند مثل ``` :doc:`installation` ``` و  در مثال زیر ``` :doc:`quickstart` ```:

```po
#: ../../index.rst:11
msgid ""
"Welcome to Flask's documentation. Get started with :doc:`installation` "
"and then get an overview with the :doc:`quickstart`."
msgstr ""
"اینجا را با ترجمه پر کنید. اینجا را با ترجمه پر کنید. :doc:`installation`"
"اینجا را با ترجمه پر کنید. اینجا را با ترجمه پر کنید. :doc:`quickstart`."
```

این راهنما شاید بتواند کمک کند: [راهنما](https://www.gnu.org/software/trans-coord/manual/web-trans/html_node/PO-Editors.html)

#### اتمام ترجمه

* اگر اولین مترجم هستید، `FIRST AUTHOR <EMAIL@ADDRESS>` را در بالای فایل های `.po` با نام و ایمیل خود جایگزین کنید.
* مقدار فیلد «Last-Translator» را در بالای فایل «.po» به‌روزرسانی کنید. (اگر از نرم افزاری مانند poedit استفاده میکنید به اینکار نیازی نیست)
* اگر ترجمه بخشی را تمام کردید در فایل `README.md`، بخش را به عنوان تکمیل شده علامت بزنید به عنوان مثال:

```
- [x] example [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
```

تغییرات را کامیت کنید:

```
$ git add docs/locales/fa/LC_MESSAGES/example.po README.md
$ git commit -m "Translated docs/example.po"
```

##### بررسی و تست

برای ساختن مستندات کار های زیر را انجام دهید:

* در Unix/Linux از دستورات زیر استفاده کنید:

```
$ cd docs
$ make dirhtml
$ python -m http.server --directory _build/dirhtml
```

در ویندوز:

```
> cd docs
> .\make.bat dirhtml
> python -m http.server --directory _build\dirhtml
```

سپس در مرورگر خود این آدرس را باز کنید تا تغییرات را مشاهده کنید:

* <http://127.0.0.1:8000>

اگر همه چیز خوب باشد تغییرات خودتان را پوش کنید({name} را با نام برنچ خودتان جایگزین کنید).

```
$ git push origin {name}
```

#### ایجاد یک PR

* به فورک خود بروید. یک اعلانی خواهید دید. روی `Compare & pull request` کلیک کنید تا یک PR ایجاد کنید.
* اطلاعات درخواست شده در PR را تکمیل کنید
* ممنونم! PR شما را بررسی خواهیم کرد.

## فهرست کارهای ترجمه

### ترجمه لوگوی فلاسک

* [X] flask-logo.png [@MDK84](https://github.com/mdk84) MDK

### docs/

* [x] advanced_foreword [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] async-await
* [ ] blueprints
* [ ] changes
* [ ] cli
* [ ] config
* [X] contributing [@mdk84](https://github.com/mdk84) MDK
* [X] debugging [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
* [ ] design
* [X] errorhandling [@mmdbalkhi](https://github.com/mmdbalkhi/) Komeil Parseh
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
* [x] shell [@ja74d](https://github.com/ja74d) Javad Pournosrat
* [ ] signals
* [X] templating [@mmdbalkhi](https://github.com/mmdbalkhi/) komeil parseh
* [X] testing [@mmdbalkhi](https://github.com/mmdbalkhi/) komeil parseh
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
