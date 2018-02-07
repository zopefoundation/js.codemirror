from setuptools import setup, find_packages
import os


version = '5.34.0'


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'codemirror', 'test_codemirror.rst')
    + '\n' +
    read('CHANGES.rst'))


setup(
    name='js.codemirror',
    version=version,
    description="Fanstatic packaging for CodeMirror in-browser editor.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    license='ZPL 2.1',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'codemirror = js.codemirror:library',
        ],
    },
)
