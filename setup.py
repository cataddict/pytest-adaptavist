from setuptools import setup

setup(name="pytest-adaptavist",
      description="pytest plugin for generating test execution results within Jira Test Management (tm4j)",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      use_scm_version=True,
      url="https://github.com/devolo/pytest-adaptavist",
      author="Stephan Steinberg, Markus Bong, Guido Schmitz",
      author_email="markus.bong@devolo.de, guido.schmitz@devolo.de",
      license="MIT",
      py_modules=["pytest_adaptavist"],
      packages=["pytest_adaptavist"],
      package_data={"pytest_pretty_terminal": ["py.typed"]},
      entry_points={"pytest11": ["adaptavist = pytest_adaptavist"]},
      platforms="any",
      python_requires=">=3.8",
      install_requires=["adaptavist>=2.0.0", "pytest>=5.4.0", "pytest-assume>=2.0.0", "pytest-metadata", "requests"],
      extras_require={
          "test": ["beautifulsoup4"]
      },
      setup_requires=["setuptools_scm"],
      keywords="python pytest adaptavist kanoah tm4j jira test testmanagement report",
      classifiers=[
          "Framework :: Pytest",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Quality Assurance",
          "Topic :: Software Development :: Testing",
          "Topic :: Utilities",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ])
