# PythonFlaskSQLAlchemyTemplate
This Repo containst the default framework and skeleton for NetDevOps WebApps and APIs using Python/Flask/SQLAlchemy/Marshmallow. The repo contains a fully working sample application (after updating credentials). This ReadMe should contain documentation as to how to clone this code, break the link to this repo, and create a new repo for the new application. Instructions are also provided for basic application deployment on a linux system. 


## Cloning this repo

## Testing the existing application

## Rehoming the application to a new Repo

## Git Workflow Process for changes to your new application

## Making a Flask Application into a service using Systemd
This will allow the application to automatically start up after a system restart, and restart the application if it crashes or unloads for any reason. 

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
    
