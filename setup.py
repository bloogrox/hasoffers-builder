from distutils.core import setup

setup(
    name='hasoffers-builder',
    version='0.1.0',
    author='Aslan',
    author_email='bloogrox@gmail.com',
    packages=['hobuilder'],
    url='https://github.com/bloogrox/hasoffers-builder.git',
    description='Python client for Hasoffers API v3',
    install_requires=[
        "requests",
    ],
    dependency_links=[
        "git+https://github.com/bloogrox/http_build_query.git#egg=http_build_query"
    ],
)
