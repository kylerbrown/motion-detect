from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
        encoding = kwargs.get('encoding', 'utf-8')
        sep = kwargs.get('sep', '\n')
        buf = []
        for filename in filenames:
                with io.open(filename, encoding=encoding) as f:
                        buf.append(f.read())
                        return sep.join(buf)

long_description = read('README.md')


class PyTest(TestCommand):
        def finalize_options(self):
                TestCommand.finalize_options(self)
                self.test_args = []
                self.test_suite = True

        def run_tests(self):
                import pytest
                errcode = pytest.main(self.test_args)
                sys.exit(errcode)

setup(
    name='motion-detect',
    scripts=['motion-detect'],
    url='http://github.com/kjbrown/motion-detect/',
    license='GPL License',
    author='Kyler Brown',
    version='0.1',
    tests_require=['pytest'],
    install_requires=['numpy',
                      'cv2'],
    cmdclass={'test': PyTest},
    author_email='kylerjbrown@gmail.com',
    description='realtime motion detection and video file analysis',
    long_description=long_description,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering'],
    extras_require={
        'testing': ['pytest'],
    }
)
