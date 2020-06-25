# PythonFlaskSQLAlchemyTemplate
Default framework and skeleton for NetDevOps WebApps and APIs using Python/Flask/SQLAlchemy/Marshmallow



## Making a Flask Application into a service using Systemd

#### Create a Service Unit File

    cd /etc/systemd/system
    sudo vim <servicename>.service
 
#### Use the following as a template to define your service
Note: defining absolute paths are typically required. 

    [Unit]
    Description=Route Table Checkout Service
    After=network.target

    [Service]
    User=root
    WorkingDirectory=/var/www/html/Route_Validation_Flask_Prod
    ExecStart=/usr/bin/python3 /var/www/html/Route_Validation_Flask_Prod/route_diff.py
    Restart=always

    [Install]
    WantedBy=multi-user.target

#### Refresh Systemd configuration to see the new file

    sudo systemctl daemon-reload 
    
#### Start the application as a service
(Be sure the application is not already running!)

    sudo systemctl start <servicename>
    
#### Check the status of your service

    sudo systemctl status <servicename>
    
