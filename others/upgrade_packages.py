from subprocess import call

import pkg_resources

packages = (dist.project_name for dist in pkg_resources.working_set)
# [print(package) for package in packages]
[call('pip install --upgrade {}'.format(p), shell=True) for p in packages]
