import setuptools

setuptools.setup(
    name='kalenderwoche',
    version='0.1',
    url='https://snapcraft.io/kalenderwoche',
    license='MIT',
    author='lmoesle',
    author_email='lukas95m@yahoo.de',
    description='Show the kalenderwoche for a date',
    install_requires=['docopt==0.6.2'],
    scripts=['kalenderwoche.py'],
)
