import os
import re
import setuptools

NAME             = "mmd_twosample"
AUTHOR           = "Jacquelyn Shelton"
AUTHOR_EMAIL     = "jacquelyn.ann.shelton@gmail.com"
DESCRIPTION      = "Various kernel-based statistical hypothesis tests for the two-sample problem"
LICENSE          = "GPL"
KEYWORDS         = "statistical test"
URL              = "https://github.com/fatflake/" + NAME
README           = ".github/README.md"
CLASSIFIERS      = [
  "python3",
  "developmenstatus3",
  
]
INSTALL_REQUIRES = [
  "numpy",
  
]
ENTRY_POINTS = {
  
}
SCRIPTS = [
  
]

HERE = os.path.dirname(__file__)

def read(file):
  with open(os.path.join(HERE, file), "r") as fh:
    return fh.read()

VERSION = re.search(
  r'__version__ = [\'"]([^\'"]*)[\'"]',
  read(NAME.replace("-", "_") + "/__init__.py")
).group(1)

LONG_DESCRIPTION = read(README)

if __name__ == "__main__":
  setuptools.setup(
    name=NAME,
    version=VERSION,
    packages=setuptools.find_packages(),
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    scripts=SCRIPTS,
    include_package_data=True    
  )
