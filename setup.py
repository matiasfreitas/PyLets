from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='PyLets',
    url='https://github.com/matiasfreitasguimaraes/PyLets',
    author='Matias Freitas Guimarães',
    author_email='matiasfreitasguimaraes@gmail.com',
    # Needed to actually package something
    packages=['PyLets'],
    # Needed for dependencies
    install_requires=['numpy',"scipy","matplotlib", "plotly"],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='PyLets: Functions for wavelet Analysis',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)