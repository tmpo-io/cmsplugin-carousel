from setuptools import setup, find_packages

from cmsplugin_carousel import __version__

setup(
    name="cmsplugin-carousel",
    version=__version__,
    url='http://github.com/tmpo-io/cmsplugin-carousel',
    license='BSD',
    description="Carousel for django-cms with filer imager",
    long_description=open('README.rst').read(),
    author='Oriol Collell',
    author_email='o@tmpo.io',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.8",
        "django-cms >= 3.2",
        "django-sekizai >= 0.4.2",
        "easy_thumbnails >= 1.0",
        "django-filer >= 1.0.0",
        "cmsplugin-filer==1.0.1",
        "django-appconf",
    ],
    include_package_data=True,
    zip_safe=False,
)
