from setuptools import setup


setup(
    name="pycalc",
    version="1.0",
    description="Pure-python command-line calculator.",
    author="Anton Kliukin",
    author_email="anton_kliukin@epam.com",
    packages=["pycalc", "tests"],
    test_suite="tests",
    python_requires='>=3.6',
    entry_points={
          'console_scripts': [
              'pycalc = pycalc.main:main',
          ],
       }
    )
