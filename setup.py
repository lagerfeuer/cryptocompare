from setuptools import setup

setup(
        name='cryptocompare',
        version='0.1',
        description='Wrapper for CryptoCompare.com',
        url='https://github.com/lagerfeuer/cryptocompare',
        author='lagerfeuer',
        author_email='lukas.deutz@tuta.io',
        keywords='crypto cryptocurrency wrapper cryptocompare',
        license='MIT',
        python_requires='>=3',
        packages=['cryptocompare'],
        classifiers=['Programming Language :: Python :: 3'],
        install_requires=['requests']
        )
