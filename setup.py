import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-admin-left-menu',
    version='0.1',
    include_package_data=True,
    license='BSD License',
    description='A simple left menu for DjangoAdmin',
    long_description=long_description,
    long_description_context_type='text/markdown',
    url='https://github.com/ChanMo/django-admin-left-menu',
    author='ChanMo',
    author_email='chan.mo@outlook.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
