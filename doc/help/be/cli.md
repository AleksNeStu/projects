1) import, dump
mysql -u username -p < data-dump.sql
mysqldump -u username -p database_name > data-dump.sql

-export\
mysqldump -u root -p --opt --all-databases > alldb.sql
mysqldump -u root -p --all-databases --skip-lock-tables > alldb.sql

-import\
mysql -u root -p < alldb.sql


2) Run a single MySQL query from the command line \
   https://electrictoolbox.com/run-single-mysql-query-command-line/ \
   mysql -u root -p somedb -e "select * from mytable

3) Watch queries
https://stackoverflow.com/questions/6913803/auto-refreshing-mysql-query-on-linux-commandline
https://www.commandlinefu.com/commands/view/768/monitor-the-queries-being-run-by-mysql  
https://gist.github.com/jrsouth/7118611

4) Full path to he file
readlink -f init

5) Permissions
https://www.computernetworkingnotes.com/rhce-study-guide/how-to-change-default-umask-permission-in-linux.html
Without any change in default umask permissions, all files created by user root will get 644 (666 - 022)
permissions and all directories will get 755 (777-022) permissions.

6) Reload terminal
exec bash
exec zsh

7) Repo
sudo dnf config-manager --disable mysql80-community
sudo dnf config-manager --enable mysql57-community

8) Services
https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
sudo systemctl start application.service
sudo systemctl restart application.service
sudo systemctl reload application.service
sudo systemctl reload-or-restart application.service

sudo systemctl enable application.service
systemctl status application.service
systemctl is-active application.service
systemctl is-enabled application.service
systemctl is-failed application.service

systemctl list-units

systemctl list-units --type=service


9) Run program
https://www.tecmint.com/run-linux-command-process-in-background-detach-process/#:~:text=How%20to%20Start%20a%20Linux,the%20background%20as%20a%20job.

Detach a Linux Processes From Controlling Terminal\
```firefox </dev/null &>/dev/null & ```

10) Fedora xorg
https://www.tecmint.com/configure-xorg-as-default-gnome-session/
https://docs.fedoraproject.org/en-US/quick-docs/configuring-xorg-as-default-gnome-session/

11) VeraCrypte
https://superuser.com/questions/1115813/cannot-mount-veracrypt-partition-on-linux-mint-metadata-kept-in-windows-cache

12) Add timestamp to filename
https://crunchify.com/shell-script-append-timestamp-to-file-name/
https://stackoverflow.com/questions/8228047/adding-timestamp-to-a-filename-with-mv-in-bash/32452472

mysqldump -u root -p --all-databases --skip-lock-tables > dbs_backup_$(date "+%Y.%m.%d-%H.%M.%S").sql
