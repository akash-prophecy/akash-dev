from setuptools import setup, find_packages
setup(
    name = 'test2',
    version = '1.0',
    packages = find_packages(include = ('test2*', )) + ['prophecy_config_instances.test2'],
    package_dir = {'prophecy_config_instances.test2' : 'configs/resources/test2'},
    package_data = {'prophecy_config_instances.test2' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.5'],
    entry_points = {
'console_scripts' : [
'main = test2.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
