from setuptools import setup


def get_version():
    with open("version") as version_file:
        return version_file.read()


def get_requirements():
    with open("requirements.txt") as requirements_file:
        return [
            dependency.strip()
            for dependency in requirements_file
            if dependency.strip()
        ]


extras_require = {"dev": ["pre-commit"]}

setup_requires = [
    "flake8",
]

setup(
    name="service_api",
    version=get_version(),
    packages=["service_api"],
    include_package_data=True,
    install_requires=get_requirements(),
    setup_requires=setup_requires,
    extras_require=extras_require,
    package_dir={"service_api": "service_api"},
    entry_points={
        "paste.app_factory": [
            "service_api=service_api.server:serve",
        ]
    },
)
