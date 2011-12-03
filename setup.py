from setuptools import setup


setup(name="pep8nazi",
      version='0.1',
      description="PEP8 Nazi: because really, you have no excuse.",
      long_description='Just say NO to non-PEP8 compliant code.',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='pep8',
      author='Scott Torborg',
      author_email='storborg@gmail.com',
      url='http://github.com/storborg/pep8nazi',
      license='MIT',
      packages=['pep8nazi'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
