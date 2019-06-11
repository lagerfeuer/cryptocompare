from setuptools import setup

with open('README.rst', encoding="utf-8") as f:
    readme = f.read()

setup(
    name='cryptocompare',
    version='0.6.4',
    description='Wrapper for CryptoCompare.com',
    long_description=readme,
    url='https://github.com/lagerfeuer/cryptocompare',
    author='lagerfeuer',
    author_email='lukas.deutz@mailfence.com',
    keywords='crypto cryptocurrency wrapper cryptocompare',
    license='MIT',
    python_requires='>=3',
    packages=['cryptocompare'],
    classifiers=['Programming Language :: Python :: 3'],
    install_requires=['requests']
)
