---
source: https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq \
created: 2022-12-02T14:59:43 (UTC +01:00) \
tags: [] \
author: 
---
# Using RabbitMQ — Celery 5.2.7 documentation
---
This document describes the current stable version of Celery (5.2). For development docs, [go here](http://docs.celeryproject.org/en/master/getting-started/backends-and-brokers/rabbitmq.html).

-   [Installation & Configuration](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installation-configuration)
    
-   [Installing the RabbitMQ Server](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installing-the-rabbitmq-server)
    
    -   [Setting up RabbitMQ](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#setting-up-rabbitmq)
        
    -   [Installing RabbitMQ on macOS](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installing-rabbitmq-on-macos)
        
        -   [Configuring the system host name](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#configuring-the-system-host-name)
            
        -   [Starting/Stopping the RabbitMQ server](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#starting-stopping-the-rabbitmq-server)
            

## [Installation & Configuration](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id2)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installation-configuration "Permalink to this headline")

RabbitMQ is the default broker so it doesn’t require any additional dependencies or initial configuration, other than the URL location of the broker instance you want to use:

```
broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'

```

For a description of broker URLs and a full list of the various broker configuration options available to Celery, see [Broker Settings](https://docs.celeryq.dev/en/stable/userguide/configuration.html#conf-broker-settings), and see below for setting up the username, password and vhost.

## [Installing the RabbitMQ Server](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id3)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installing-the-rabbitmq-server "Permalink to this headline")

See [Installing RabbitMQ](http://www.rabbitmq.com/install.html) over at RabbitMQ’s website. For macOS see [Installing RabbitMQ on macOS](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installing-rabbitmq-on-macos).

Note

If you’re getting nodedown errors after installing and using **rabbitmqctl** then this blog post can help you identify the source of the problem:

### [Setting up RabbitMQ](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id4)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#setting-up-rabbitmq "Permalink to this headline")

To use Celery we need to create a RabbitMQ user, a virtual host and allow that user access to that virtual host:

```
$ sudo rabbitmqctl add_user myuser mypassword

```

```
$ sudo rabbitmqctl add_vhost myvhost

```

```
$ sudo rabbitmqctl set_user_tags myuser mytag

```

```
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"

```

Substitute in appropriate values for `myuser`, `mypassword` and `myvhost` above.

See the RabbitMQ [Admin Guide](http://www.rabbitmq.com/admin-guide.html) for more information about [access control](http://www.rabbitmq.com/admin-guide.html#access-control).

### [Installing RabbitMQ on macOS](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id5)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#installing-rabbitmq-on-macos "Permalink to this headline")

The easiest way to install RabbitMQ on macOS is using [Homebrew](https://github.com/mxcl/homebrew/) the new and shiny package management system for macOS.

First, install Homebrew using the one-line command provided by the [Homebrew documentation](https://github.com/Homebrew/homebrew/wiki/Installation):

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

Finally, we can install RabbitMQ using **brew**:

After you’ve installed RabbitMQ with **brew** you need to add the following to your path to be able to start and stop the broker: add it to the start-up file for your shell (e.g., `.bash_profile` or `.profile`).

```
PATH=$PATH:/usr/local/sbin

```

#### [Configuring the system host name](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id6)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#configuring-the-system-host-name "Permalink to this headline")

If you’re using a DHCP server that’s giving you a random host name, you need to permanently configure the host name. This is because RabbitMQ uses the host name to communicate with nodes.

Use the **scutil** command to permanently set your host name:

```
$ sudo scutil --set HostName myhost.local

```

Then add that host name to `/etc/hosts` so it’s possible to resolve it back into an IP address:

```
127.0.0.1       localhost myhost myhost.local

```

If you start the **rabbitmq-server**, your rabbit node should now be rabbit@myhost, as verified by **rabbitmqctl**:

```
$ sudo rabbitmqctl status
Status of node rabbit@myhost ...
[{running_applications,[{rabbit,"RabbitMQ","1.7.1"},
                    {mnesia,"MNESIA  CXC 138 12","4.4.12"},
                    {os_mon,"CPO  CXC 138 46","2.2.4"},
                    {sasl,"SASL  CXC 138 11","2.1.8"},
                    {stdlib,"ERTS  CXC 138 10","1.16.4"},
                    {kernel,"ERTS  CXC 138 10","2.13.4"}]},
{nodes,[rabbit@myhost]},
{running_nodes,[rabbit@myhost]}]
...done.

```

This is especially important if your DHCP server gives you a host name starting with an IP address, (e.g., 23.10.112.31.comcast.net). In this case RabbitMQ will try to use rabbit@23: an illegal host name.

#### [Starting/Stopping the RabbitMQ server](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#id7)[¶](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#starting-stopping-the-rabbitmq-server "Permalink to this headline")

To start the server:

you can also run it in the background by adding the `-detached` option (note: only one dash):

```
$ sudo rabbitmq-server -detached

```

Never use **kill** (_kill(1)_) to stop the RabbitMQ server, but rather use the **rabbitmqctl** command:

When the server is running, you can continue reading [Setting up RabbitMQ](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#setting-up-rabbitmq).
