<div dir="rtl">

# ترجمه مستندات فلاسک(Flask)

## راهنمای مشارکت

### نصب

* روی  دکمه [Fork](https://github.com/mmdbalkhi/flask-docs-fa/fork) برای گرفتن یک انشعاب از این مخزن کلیک کنید
* انشعاب مخزن را به صورت محلی شبیه سازی کنید [^1] (نام کاربری خود را با `{username}`  جایگزین کنید):

</div>

```
$ git clone https://github.com/{username}/flask-docs-fa
$ cd flask-docs-mmdbalkhi
$ git remote add upstream https://github.com/mmdbalkhi/flask-docs-fa
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

###  واگذاری[^2]
* [این فایل](https://github.com/mmdbalkhi/flask-docs-mmdbalkhi/edit/main/README.md) را باز کنید
* «فهرست کار[^3] های  ترجمه» را پیدا کنید, فصلی را که میخواهید علامت بزنید.

```
- [ ] مثال @نام‌کاربری_شما اسم شما
```

میتوانید نام کاربری را به نمایه گیت‌هاب خودتان پیوند دهید.:

```
- [ ] مثال [@نام‌کاربری_شما](https://github.com/your_username) نام شما
```

> __**نکته**__: ترجیحا کامیت ها و واگذاری های لیست کار ها را انگلیسی بنویسید.

* یک کامیت بنویسید(به عنوان مثال "تخصیص مثال به @نام‌کاربری_شما") سپس روی دکمه "Propose changes" کلیک کنید تا یک PR [^4] ساخته شود.

### نرم افزار های پیشنهادی برای ترجمه

همانطور که در زیر توضیح داده شده است، ترجمه ها با استفاده از فایل های .po انجام می شود.
[POEdit](https://poedit.net/) یک نرم افزار خوب برای اینکار است. ( نباید با POEditor اشتباه گرفته شود.

### ترجمه

* وقتی  که  PR واگذاری شده ادغام شد  یک شاخه جدید به صورت محلی ایجاد کنید
(حتما نام شاخه را بروزرسانی کنید. , به عنوان مثال, `translate-cli` ):

</div>

```
$ git fetch upstream
$ git checkout -b your-branch-name upstream/main
```

<div dir="rtl">

* فایل های `.po`  در   دایرکتوری `docs/locales/fa/LC_MESSAGES`  ترجمه کنید.

نمونه‌ای از یکی از این فایل‌ها، از `docs/.../index.po` ، در زیر آورده شده است.

</div>

```po
#: ../../index.rst:4
msgid "Welcome to Flask"
msgstr "<FILL HERE BY TARGET LANGUAGE>"
```

<div dir="rtl">

یک مورد دیگر msgid که یک متن چند خطی است و حاوی  سینتکس[^5] reStructuredText است:

</div>

```po
#: ../../index.rst:11
msgid ""
"Welcome to Flask's documentation. Get started with :doc:`installation` "
"and then get an overview with the :doc:`quickstart`."
msgstr ""
"FILL HERE BY TARGET LANGUAGE FILL HERE BY TARGET LANGUAGE :doc:`installation` "
"FILL HERE BY TARGET LANGUAGE :doc:`quickstart`."
```

<div dir="rtl">

لطفا مراقب باشید که نماد reST را نقض نکنید. [^6]
اکثر [ادیتور های po](https://www.gnu.org/software/trans-coord/manual/web-trans/html_node/PO-Editors.html) میتوانند به شما کمک کنند.

* فصل را به عنوان تمام شده علامت بزنید (چک باکس را با "x" پر کنید):

```
- [x] مثال @نام‌کاربری_شما نام شما
```

* اگر اولین مترجم هستید،   `FIRST AUTHOR <EMAIL@ADDRESS>` را در بالای فایل های `.po` کامنت کنید.
* مقدار فیلد «Last-Translator» را در بالای فایل «.po» به‌روزرسانی کنید.
* تغییرات را کامیت کنید.:

</div>

```
$ git add docs/locales/fa/LC_MESSAGES/example.po README.md
$ git commit -m "Translate docs/example"
```

<div dir="rtl">

*اسناد [^7] را بسازید و تغییرات  را بررسی [^8] کنید:

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

* صفحه اصلی مخزن انشعاب خود را باز کنید، اعلانی در مورد آن خواهید دید
شعبه جدید برای ایجاد PR، روی دکمه «Compare & pull request» کلیک کنید.
* هماهنگ کننده ترجمه به زودی PR شما را بررسی خواهد کرد. متشکرم!

## فهرست کارهای ترجمه

مطمئن شوید که هر بار فقط یک فصل را علامت گذاری کنید، در صورت اتمام فصل اول، یکی دیگر را علامت بزنید
تا PR ایجاد شود. مگر اینکه فصل طولانی باشد، ممکن است تکلیف[^9] را بازنشانی کنیم.(اگر تا ده روز دیگر ترجمه را تمام نکنید.)

</div>

### docs/

* [X] advanced_foreword [@mmdbalkhi](https://github.com/mmdbalkhi/)  Mohamad Balkhi
* [ ] appcontext
* [ ] async-await
* [ ] becomingbig
* [ ] blueprints
* [ ] changes
* [ ] cli
* [ ] config
* [ ] contributing
* [ ] debugging
* [ ] design
* [ ] errorhandling
* [ ] extensiondev
* [ ] extensions
* [X] foreword [@mmdbalkhi](https://github.com/mmdbalkhi/)  Mohamad Balkhi
* [ ] htmlfaq
* [X] index [@mmdbalkhi](https://github.com/mmdbalkhi/) Mohamad Balkhi
* [X] installation [@mmdbalkhi](https://github.com/mmdbalkhi/)  Mohamad Balkhi
* [ ] logging
* [ ] quickstart [@mmdbalkhi](https://github.com/mmdbalkhi/)  Mohamad Balkhi
* [ ] reqcontext
* [ ] security
* [ ] server
* [ ] shell
* [ ] signals
* [ ] templating
* [ ] testing
* [ ] views

### docs/tutorial/ [@mmdbalkhi](https://github.com/mmdbalkhi/)  Mohamad Balkhi

* [ ] blog
* [ ] database
* [ ] deploy
* [ ] factory
* [ ] index
* [ ] install
* [ ] layout
* [ ] next
* [ ] static
* [ ] templates
* [ ] tests
* [ ] views

### docs/deploying/

* [ ] asgi
* [ ] cgi
* [ ] fastcgi
* [ ] index
* [ ] mod_wsgi
* [ ] uwsgi
* [ ] wsgi-standalone

### docs/patterns/

* [ ] appdispatch
* [ ] appfactories
* [ ] caching
* [ ] celery
* [ ] deferredcallbacks
* [ ] distribute
* [ ] fabric
* [ ] favicon
* [ ] fileuploads
* [ ] flashing
* [ ] index
* [ ] jquery
* [ ] lazyloading
* [ ] methodoverrides
* [ ] mongoengine
* [ ] packages
* [ ] requestchecksum
* [ ] singlepageapplications
* [ ] sqlalchemy
* [ ] sqlite3
* [ ] streaming
* [ ] subclassing
* [ ] templateinheritance
* [ ] urlprocessors
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

[^1]:  Clone your fork repository locally
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
