# First, we need to add the new service and to reload systemd:
sudo ln -sf ~/Projects/projects/scripts/python/006_service/my_service.py /etc/systemd/system/my-service.service
sudo systemctl daemon-reload

# Then we can enable the service (this way it will be ran each time the system boots) and start it:
sudo systemctl enable my-service.service
sudo systemctl start my-service.service

# If my_service.py is configured to log information (and it should!), we can check the system logs with journalctl:
journalctl -u my-service.service

# Add an -f to the previous command if you want to follow the journal as it updates, just like with tail -f.

# If my_service.py is ran in a terminal, we can stop it by hitting Ctrl+C (registered as SIGINT):
python my_service.py
# python test_service.py
#    INFO | MyService instance created
#    INFO | Tick
#    INFO | Tick
#^C WARNING | Keyboard interrupt (SIGINT) received...
#    INFO | Cleaning up...
#    INFO | Named pipe removed
