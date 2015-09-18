load("/tools/pypi_package", "pypi_package")

py_library(
    name = "tabletest",
    srcs = ["tabletest/__init__.py"],
    visibility = ["//visibility:public"],
    srcs_version = "PY2"
)

py_test(
    name = "tabletest_test",
    main = "tests/test_tabletest.py",
    srcs = [
      "tests/__init__.py",
      "tests/test_tabletest.py"
    ],
    deps = [
      ":tabletest"
    ],
    size = "small",
    default_python_version = "PY2",
    srcs_version = "PY2",
)

pypi_package(
    name = "tabletest_pkg",
    version = "1.0.4",
    description = "Unit testing module for table-like test, for Python 2.",
    long_description = "README.md",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords = "unittest test table testing",
    url = "http://github.com/horia141/tabletest",
    author = "Horia Coman",
    author_email = "horia141@gmail.com",
    license = "MIT",
    packages = [":tabletest"],
    test_suite = "nose.collector",
    tests_require = ["nose"],
)
