from setuptools import setup

setup(
    name="AtlasBioinfoToolkits",
    version="0.1.0",
    scripts=["bin/bam2MaP"], 
    author="Haopeng Yu",
    author_email="hp.yu@outlook.com",
    description="A short description of your tool.",
    # long_description=open('README.md').read(),
    # long_description_content_type="text/markdown",
    url="https://github.com/atlasbioinfo/AtlasbioinfoSeqTools.git",
    classifiers=[
        # See https://pypi.org/classifiers/ for values
        "License :: OSI Approved :: Apache License"
    ],
)
