import re
from setuptools import find_packages, setup

def parse_requirements(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="gigaam",
    py_modules=["gigaam"],
    version="0.1.0",
    description="GigaAM: A package for audio modeling and ASR.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    author="GigaChat Team",
    url="https://github.com/salute-developers/GigaAM/",
    license="MIT",
    packages=find_packages(include=["gigaam"]),
    python_requires=">=3.10",
    install_requires=parse_requirements("requirements.txt"),
    extras_require={
        "longform": ["torch==2.8.*", "torchaudio==2.8.*", "pyannote.audio==4.0", "torchcodec==0.7", "numba>=0.62"],
        "tests": ["pytest", "pytest-cov", "scipy", "soundfile", "librosa"],
    },
    include_package_data=True,
)
