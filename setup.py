from setuptools import setup, find_packages

setup(
    name='zeta-micro-client',
    packages=['zeta_micro_client'],
    version='0.2.9',
    author="Develper Junio",
    author_email='developer@junio.in',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    description="Zeta Microservice Service Client",
    license="MIT license",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "attrs==21.2.0",
        "certifi==2021.5.30",
        "charset-normalizer==2.0.4",
        "colorama==0.4.4",
        "idna==3.2",
        "iniconfig==1.1.1",
        "marshmallow==3.13.0",
        "packaging==21.0",
        "pluggy==0.13.1",
        "py==1.10.0",
        "pyaml==21.8.3",
        "pyparsing==2.4.7",
        "pytest==6.2.4",
        "PyYAML==5.4.1",
        "requests==2.26.0",
        "toml==0.10.2",
        "urllib3==1.26.6"
    ]
)
