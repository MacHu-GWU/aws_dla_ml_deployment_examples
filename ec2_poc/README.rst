Deploy ML model to EC2
==============================================================================


How to replay this Example
------------------------------------------------------------------------------

First, launch a Amazon Linux2 EC2 instance, t2.medium is fine. And ssh into it.

1. install dependencies.

.. code-block:: bash

    # install git, so you can clone this repo
    sudo yum install git

    # install python3.8
    sudo yum install -y amazon-linux-extras
    sudo amazon-linux-extras enable python3.8
    sudo yum install python3.8
    sudo pip3.8 install virtualenv --upgrade

2. install virtualenv and dependencies:

.. code-block:: bash

    # create virtualenv
    virtualenv -p python3.8 venv

    # enter virtualenv
    source ./venv/bin/activate

    # cd to working directory
    cd /path-to/ec2_poc

    # install python dependencies
    pip install -r requirements.txt


3. train and build the model:

.. code-block:: bash

    # train and dump model to file (on local)
    python ./train_model.py

    # test the dumped model
    python ./test_model.py

    # test the dumped model
    python ./test_model.py

    # run ML service as a web app
    bash ./run_service.sh

    # mock the ML service consumption, mock a http request
    python ./consumer.py


How to deploy to Production
------------------------------------------------------------------------------


The Natual of a Web App
------------------------------------------------------------------------------


Method 1. Single Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow this tutorial: https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/

What is missing for a production server?

1. Proxy. Why Proxy is important for production::

    # without Proxy

    User --- Internet ---> Server ---> service.py
                                            |
            <-------------------------------+

    # with Proxy
    User --- Internet ---> Server ---> Proxy ---> service.py
                                        | |            |
            <---------------------------+ <------------+


Method 2. Highly Available Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow this tutorial: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

What is missing for a production server?

1. network, security
2. load balancer
3. auto scaling
4. version rolling
5. blue / green deployment


Other Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Lambda + API Gateway
    - Pro: fast development; no infrastructure management; easiest learning curve; easy deployment
    - Con: stateless, memory / run time limitation
2. ECS / EKS + Load Balancer
    - Pro: flexible, can adapt any runtime dependencies and external dependencies
    - Con: intermediate learning curve; additional work for deployment
3. SageMaker
    - Pro: fully automated pipeline for training, testing, tuning, deployment, Data Scientist friendly.
    - Con: intermediate learning curve;
