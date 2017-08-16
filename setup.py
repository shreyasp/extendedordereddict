from setuptools import setup


setup(
    name='extendedordereddict',
    version='0.0.1',
    description='Extended Ordered Dict to insert, remove, & print in an order',
    author='Shreyas Patil',
    author_email='shreyaspatil87@gmail.com',
    packages=[
        'extendedordereddict'
    ],
    url='https://github.com/shreyasp/extendedordereddict',
    license='MIT',
    keywords=[
        'Ordereddict',
        'dict'
    ],
    install_requires=[
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose'
    ],
    python_requires='>3.5'
)
