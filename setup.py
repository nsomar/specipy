from setuptools import setup

setup(
    name='specipy',
    version='1.0',
    packages=['specipy', 'bin'],
    url='https://github.com/oarrabi/specipy',
    license='MIT',
    author='omarsubhiabdelhafith',
    author_email='o.arrabi@me.com',
    description='',
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'specipy=bin.specipy_cli:parse',
        ],
    },
)
