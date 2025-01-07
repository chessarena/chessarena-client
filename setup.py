from setuptools import setup, find_packages

setup(
    name="chessarena-client",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "chess"],
    entry_points={
        "console_scripts": [
            "arenachess=arenachess.cli:main",
        ],
    },
)
