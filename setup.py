from setuptools import setup, find_packages
setup(
    name='tourbillon-nginx',
    version='0.1',
    packages=find_packages(),
    install_requires=['aiohttp==0.17.2'],
    zip_safe=False,
    namespace_packages=['tourbillon']
)
