from setuptools import find_packages, setup




setup(
name='mlproject',
version='0.0.1',
author='yaal96',
author_email='yarikaleksandro@yandex.ru',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)