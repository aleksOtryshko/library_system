from setuptools import setup, find_packages

setup(
    name="library_system",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Добавьте зависимости, если они есть
    entry_points={
        'console_scripts': [
            'library-cli = application.cli:CLI',  # Укажите команду для запуска CLI
        ],
    },
)

