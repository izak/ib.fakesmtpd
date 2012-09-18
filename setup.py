from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ib.fakesmtpd',
    version=version,
    description="Patches for Plone that makes life easier with varnish",
    long_description=open("README.txt").read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='varnish languagetool caching cookie',
    author='Izak Burger',
    author_email='isburger@gmail.com',
    url='https://github.com/izak/ib.fakesmtpd',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
        [console_scripts]
        smtpd = ib.fakesmtpd:main
    """,
    )
