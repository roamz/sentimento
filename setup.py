from setuptools import setup, find_packages

setup(
    name='sentimento',
    version='0.0.1',
    description="Quick and dirty sentiment analysis.",
    long_description=open("README.md").read(),
    url='http://github.com/theorm/sentimento',
    author='Roman Kalyakin',
    author_email='roman@kalyakin.com',
    packages=find_packages(exclude=('tests',)),
    package_data={'': ['*.md']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Database Engines/Servers',
    ],
    tests_require=[],
    install_requires=['nltk>=2.0.4'],
    test_suite = "nose.collector",
)
