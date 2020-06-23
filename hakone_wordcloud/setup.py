import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='hakone_wordcloud_snkw',
    version='0.0.2',
    author='Ken Wakita',
    author_email='wakita@is.titech.ac.jp',
    description='A word cloud generation sample file for the Hakone Ekiden visualization project',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires = [
        'fonttools',
        'pandas',
        'xlrd',
        'XlsxWriter',
        'wordcloud @ https://github.com/amueller/word_cloud/archive/master.zip',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points = {
        'console_scripts': [
            'build_xlsx = hakone_wordcloud.build_xlsx:main',
            'hakone_wc = hakone_wordcloud.hakone_wc:main',
        ],
    },
    python_requires='>=3.6',
)
