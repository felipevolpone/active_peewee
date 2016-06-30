from setuptools import setup, find_packages


def description():
    return """
    Improving the Peewee ORM with ideas from Rails ActiveRecord
    """

setup(
    name="active_peewee",
    version="0.0.1",
    author="Felipe Volpone",
    author_email="felipevolpone@gmail.com",
    description=description(),
    license="MIT",
    keywords="python orm peewee",
    url="http://github.com/felipevolpone/active_peewee",
    packages=find_packages(exclude=['tests']),
    install_requires=['peewee'],
    long_description="Check on github: http://github.com/felipevolpone/active_peewee",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ]
)
