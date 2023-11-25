import setuptools
with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

#__version__ == "0.0.0"

REPO_NAME = 'Text-Summarizer-Project'
AUTHOR_USER_NAME = 'ShivamPranjale'
SRC_REPO = 'TextSummarizer'
AUTHOR_EMAIL = 'shivamv.pranjale@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    #version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for NLP App",
    long_description=long_description,
    long_description_conten="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where="src")
)