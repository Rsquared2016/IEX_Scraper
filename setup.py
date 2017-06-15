from distutils.core import setup

setup(
    name='IEX_Scraper',
    version='0.1dev',
    packages=['scripts','data'],
    url='',
    license='MIT',
    author='Michael Hernandez',
    author_email='',
    description='A tool for pulling data from the IEX exchange API.',
    install_requires='requests',
    scripts="main.py",
    package_data={
        'data': ["*.db"],
        'cfg':["*.ini"]
    },
    include_package_data=True,
    zip_safe=False
)

