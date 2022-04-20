from setuptools import setup

DISTNAME = 'Files Tools'
DESCRIPTION = 'Set of scripts for automating tasks'
LONG_DESCRIPTION = open('README.md', encoding="utf8").read()
MAINTAINER = 'Silas João, Mikael Amaral, Arthur Henrique, Luiz Henrique e Ewerton Cordeiro'
URL = 'https://github.com/silasabs/FilesTool'
LICENSE = 'MIT'


def requirements(file):
    lineiter = (line.strip() for line in open(file))
    return [line for line in lineiter if line and not line.startswith("#")]


files = ["scripts/*"]

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    install_requires=requirements("./requirements.txt"),
    long_description=LONG_DESCRIPTION,
    packages=['scripts'],
    package_data={'scripts': files},
    scripts=["runner"],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    python_requires='>=3.9',
)
