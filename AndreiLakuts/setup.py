from setuptools import setup, find_packages

setup(
    name='rss_reader',
    version='1.3',
    packages=find_packages(),
    author='Andrei Lakuts',
    author_email='lakuts@mail.ru',
    description='Command-line RSS reader',
    python_requires='>=3.8',
    entry_points={
        'console_scripts':
            ['rss_reader = rss_reader:main_program']
    }
)
