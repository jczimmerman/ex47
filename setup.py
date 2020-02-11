import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="ex47"
    version="0.0.1",
    author="Joseph Zimmerman",
    author_email="joeyzimmerman17@gmail.com",
    url="https://github.com/jczimmerman/ex47",
    description="Practicing my unit tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
