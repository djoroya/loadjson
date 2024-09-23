from setuptools import setup, find_packages

setup(
    name="loadsavejson",
    version="0.1.0",
    description="Este proyecto proporciona funciones para guardar y cargar diccionarios que contienen matrices de NumPy y DataFrames de Pandas en archivos JSON",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Deyviss Jesús Oroya Villalta",
    author_email="djoroya@gmail.com",
    url="https://github.com/djoroya/loadjson",
    packages=find_packages(),
    proyect_urls={
        "Source Code": "https://github.com/djoroya/loadjson",
        "Bug Tracker": "https://github.com/djoroya/loadjson/issues",
    },
    install_requires=[
        # Dependencias de la librería
        "numpy",
        "pandas",
    ],
    python_requires='>=3.6',
)
