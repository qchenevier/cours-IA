
### 2018-04-04T14:09:55+02:00

Learning DevOps:

- Linux / Sysadmin:
    - linux basics (folders organization / main commands)
    - bashrc & aliases
    - CLI tool in python (docopt, argparse, ...)

- Code velocity tooling:
    - git: managing versions of a software repository
    - gitlab/github: cloning, code review & pull requests
    - atom + hydrogen
    - atom + git

- Code quality:
    - clean code & DRY
    - pylint & code quality metrics
    - atom + pylint
    - method chaining in pandas & pyspark

- Remote dev
    - ssh + ssh tunneling
    - atom + hydrogen + remote kernel
    - nohup: launching a software as a service
    - atom + remote sftp
    - boto3 + S3

- Infrastructure automation: ansible:
    - network:
        - VPC
        - subnets
        - keys
        - security groups
    - computing:
        - AMI
        - EC2 launch
        - installing & launching software
    - storage:
        - S3
        - propagating aws credentials to EC2
        - EFS

- Test-driven development
    - process
    - pytest
    - pytest + pyspark

### 2018-08-03T11:33:10+02:00

Full Stack:

baseline:
- git workflow (pull, branch, push, pull/merge request)
- pip env / conda env
- pytest & testing workflow
- REST API: flask-rest, falcon
- docker
- gitlab-CI
- clean code: code découplé, lisible et maintenable
- programmation fonctionnelle, stateless
- front: reactJS
- kubernetes

bonus:
- front: VueJS
- workflow avec datastore: S3, boto3

Se renseigner sur nix.

### 2019-03-08T10:32:51+01:00

code/build/test/deploy:

- code:
  - atom / vscode
  - pylint, isort, black
  - git
  - zsh
- build:
  - luigi / make
- test:
  - pytest with pandas
  - pytest with pyspark (facultatif)
- deploy
  - docker
  - gitlab-ci


Outils:
- code
- build
- test
- deploy

### ...

  # code

  ## IDE
  #### [atom](https://atom.io/)


  #### [vscode](https://code.visualstudio.com/)
  #### [pylint](https://www.pylint.org/)

  ## tools
  #### [isort](https://github.com/timothycrosley/isort)
  #### [black](https://github.com/ambv/black)

  # build
  #### [dvc](http://dvc.org)
  #### [luigi](https://github.com/spotify/luigi)

  # test
  #### [pytest](https://pytest.org/)
  #### [pytest on pyspark](https://blog.sicara.com/learn-test-pyspark-project-example-tutorial-d01d190c716b)

  # deploy
  #### [docker](https://www.docker.com/)
