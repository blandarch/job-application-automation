# Pylint

### Introduction

Pylint provides a comprehensive analysis of the code, highlighting potential issues and suggesting improvements. It helps maintain a consistent coding style and ensures that the code follows industry standards. By running Pylint as part of the Github workflow, we can catch and address any code quality issues early in the development process.

### Running Pylint and its behaviour when running within the Framework

The file named `.pylintrc` is used to store various configurations that specify the rules to be enforced when checking the adherence to best practices in Python files. It plays a crucial role in ensuring that every Python file undergoes thorough checking to maintain the highest standards of code quality and consistency.

Within the framework, there are two `.pylintrc` files that are called when running pylint twice. The first file is located inside `pylint/config/.pylintrc` and it handles the configuration that should be applied to all Python files within the framework. The second file, on the other hand, is located inside `pylint/testconfig/.pylintrc` and it handles the configuration specific to the testing part of the framework. It typically checks the syntax of method names, among other things.

*Note: Inside `pylint/testconfig/.pylintrc`, it ignores checking of all `test_helpers.py`, since the method naming convention for test_helpers should not start with the prefix `test_`, as configured in the pylint/testconfig/.pylintrc file. Other methods within the test folder that is not within test_helpers.py should adhere to the prefix `test_` method naming convention.*

To verify pylint within your local machine, run the following methods:

```bash
pylint --rcfile=./pylint/config/.pylintrc $(git ls-files '*.py') # handles the first run where it checks the entirety of the code in the framework
pylint --rcfile=./pylint/testconfig/.pylintrc $(git ls-files './*/test/*.py')# handles the second run where it checks the test folder inside the framework
```

The same run is also being handled inside the `pylint.yml` file inside `.github/workflows` directory. 

### Best Practices in Adding/Customising `.pylintrc` files

1. To customise code quality that can be implemented for the entirety of the framework, use `pylint/config/.pylintrc` file and implement customisations inside that file only.
2. To customise code quality that can be implemented for the testing part of the framework, use `pylint/testconfig/.pylintrc` file and implement customisations inside that file only.
3. Check documentation [here](https://docs.pylint.org) to know how to edit .pylintrc files.
4. To make an entirely new `.pylintrc` file:
    1. Run `pylint --generate-rcfile > ./pylint/<customName>config/.pylintrc` . The `<customName>` is something that you can name all you want, as long as there is config suffix at the end.
    2. It will come with pre-configured settings inside the `.pylintrc` file. Check the link at step 3 to know what settings to override.
    3. Once you’re done editing the newly created `.pylintrc` file, go to `.github/workflows/pylint.yml` to add the run of your pylint configurations with the newly-configured `.pylintrc` file.
        1. Under the last line of the code, add the following:

        ```bash
        - name: Analysing Python File # The step title that will appear on Github.
        run: |
          pylint --rcfile=./pylint/<customName>config/.pylintrc $(git ls-files 'path/to/python/file.py')

          # customName => the customName of the config folder file you made.
          # path/to/python/file.py => the path to the python file you want to test. You can substitute with with a regex format to test list of python files that will satisfy the regex line.
        ```