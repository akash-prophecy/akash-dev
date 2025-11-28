from setuptools import setup, find_packages
setup(
    name = 'test-git',
    version = '1.0',
    packages = find_packages(include = ('testgit*', )) + ['prophecy_config_instances.testgit'],
    package_dir = {'prophecy_config_instances.testgit' : 'configs/resources/testgit'},
    package_data = {'prophecy_config_instances.testgit' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.5'],
    entry_points = {
'console_scripts' : [
'main = testgit.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
