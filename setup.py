from setuptools import find_packages, setup

setup(
    name='touchterrain',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Jinja2>=2.10.1',
        'Pillow>=6.0.0',
        'earthengine-api>=0.1.175',
        'Flask>=1.0.2',
        'google-api-python-client>=1.7.8',
        'vectormath>=0.2.2',
        'oauth2client>=4.1.3',
    ],
    extras_require={
        'server': [
            'gunicorn>=19.9.0',
        ],
    },
)