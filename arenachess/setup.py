from setuptools import setup, find_packages

setup(
    name="chessarena-client",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "python-chess>=1.999",
    ],
    entry_points={
        "console_scripts": [
            "chessarena=arenachess.cli:main",
        ],
    },
    author="yu432",
    author_email="yurii.a.potapov@gmail.com",
    description="A chess engines arena",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chessarena/chessarena-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)