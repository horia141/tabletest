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
