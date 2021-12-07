1) Reset password
https://dev.mysql.com/doc/refman/5.7/en/resetting-permissions.html
https://stackoverflow.com/questions/33510184/how-to-change-the-mysql-root-account-password-on-centos7/34207996#34207996

What version of mySQL are you using? I''m using 5.7.10 and had the same problem with logging on as root

There is 2 issues - why can't I log in as root to start with, and why can I not use 'mysqld_safe` to start mySQL to reset the root password.

I have no answer to setting up the root password during installation, but here's what you do to reset the root password

Edit the initial root password on install can be found by running

grep 'temporary password' /var/log/mysqld.log
http://dev.mysql.com/doc/refman/5.7/en/linux-installation-yum-repo.html

systemd is now used to look after mySQL instead of mysqld_safe (which is why you get the -bash: mysqld_safe: command not found error - it's not installed)

The user table structure has changed.

So to reset the root password, you still start mySQL with --skip-grant-tables options and update the user table, but how you do it has changed.

1. Stop mysql:
systemctl stop mysqld

2. Set the mySQL environment option
systemctl set-environment MYSQLD_OPTS="--skip-grant-tables"

3. Start mysql usig the options you just set
systemctl start mysqld

4. Login as root
mysql -u root

5. Update the root user password with these mysql commands
mysql> UPDATE mysql.user SET authentication_string = PASSWORD('MyNewPassword') WHERE User = 'root' AND Host = 'localhost';
mysql> FLUSH PRIVILEGES;
mysql> quit


*** Edit ***
As mentioned my shokulei in the comments, for 5.7.6 and later, you should use
   mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
Or you'll get a warning

6. Stop mysql
systemctl stop mysqld

7. Unset the mySQL envitroment option so it starts normally next time
systemctl unset-environment MYSQLD_OPTS

8. Start mysql normally:
systemctl start mysqld

Try to login using your new password:
7. mysql -u root -p

2) Error ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
https://stackoverflow.com/questions/21944936/error-1045-28000-access-denied-for-user-rootlocalhost-using-password-y

3) time zone
https://phoenixnap.com/kb/change-mysql-time-zone#:~:text=Option%202%3A%20Edit%20the%20MySQL%20Configuration%20File,-MySQL%20settings%20can&text=Scroll%20down%20to%20the%20%5Bmysqld,00%20(GMT%20%2B8)
sudo nano /etc/mysql/my.cnf
default-time-zone = "+00:00"

SELECT @@global.time_zone;

4) cfg file
/etc/my.cnf
/etc/mysql/my.cnf
/var/lib/mysql/my.cnf
which mysqld
/usr/sbin/mysqld
/usr/sbin/mysqld --verbose --help | grep -A 1 "Default options"
/etc/mysql/my.cnf ~/.my.cnf /usr/etc/my.cnf

*Fedora MySQL server 5.2.7
$ /usr/bin/mysql --verbose --help | grep -A 1 "Default options"
Default options are read from the following files in the given order:
/etc/my.cnf /etc/mysql/my.cnf /usr/etc/my.cnf ~/.my.cnf

5) service
https://computingforgeeks.com/how-to-install-mysql-5-7-on-fedora/


6) Storage Engine
https://mariadb.com/kb/en/choosing-the-right-storage-engine/
   

7) Monitor
https://www.tecmint.com/mytop-mysql-mariadb-database-performance-monitoring-in-linux/
https://gist.github.com/jrsouth/7118611
https://docs.stackify.com/docs/what-is-stackify-retrace

   
8) MySQL - How to turn off ONLY_FULL_GROUP_BY?
error: ` incompatible with sql_mode=only_full_group_by`
https://tableplus.com/blog/2018/08/mysql-how-to-turn-off-only-full-group-by.html \
```sudo nano /etc/my.cnf```
```sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION```
```sudo systemctl restart mysqld.service```   