import logging
import os
import subprocess
from datetime import datetime

from github import Github

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


current_date = datetime.today().strftime("%Y-%m-%d")
logging.info("Starting at %s", current_date)

g = Github(os.getenv("GITHUB_TOKEN"))

git_changed = subprocess.check_output(
    "git diff --name-only HEAD HEAD~1 | grep -e '^docs/locales/'", shell=True, text=True
)
po_changed = subprocess.check_output("potodo -e docs/", shell=True, text=True)

body = (
    "## git Changed po files\n\n"
    + "\n".join(f"- [ ] {line}" for line in git_changed.splitlines() if line.strip())
    + "\n".join(f"{line}" for line in po_changed.splitlines() if line.strip())
)
logging.info("body is generated")


repo = g.get_repo("flaskcwg/flask-docs-fa")
label = repo.get_label("translate: sync")

issue = repo.create_issue(
    title=f"Sync translation for upstream updates {current_date}",
    body=body,
    labels=[label],
)
logging.info("Issue created: %s", issue.html_url)


logging.info("Done")
