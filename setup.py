from setuptools import setup

setup(
    name='slackbotr',
    description="Create unique slackbots",
    version="0.1.0",
    url="git@github.org:nsidc/slackbotr.git",
    author="National Snow and Ice Data Center",
    author_email="nsidc@nsidc.org",
    packages=['slackbotr'],
    include_package_data=True,
    install_requires=[
        'fastapi',
    ],
)
