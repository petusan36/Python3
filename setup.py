from setuptools import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='cashflows'
        version='0.0.3'
        description='Demo to python'
        long_description='This is a description of Demo to pytho project'
        classifiers=[
            'Development Status :: 3 Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Topic :: Office/Bussiness :: Financial',
        ],
        keywords='cashflows investments bonds depreciation loan irr',
        url='https://github.com/jdvelasq/demopy',
        author='Pedro Turriago Sanchez',
        author_email='pturriago@unal.edu.co',
        License=''
)
