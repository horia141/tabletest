from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='tabletest',
    version='0.0.1',
    description='Unit testing module for table-like test, for Python 2.',
    long_description=readme(),
    classifiers = [
        'Development Status :: 4 - Beta'
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='unittest test table testing',
    url='http://github.com/horia141/tabletest',
    author='Horia Coman',
    author_email='horia141@gmail.com',
    license='MIT',
    packages=[
        'tabletest',
    ],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
