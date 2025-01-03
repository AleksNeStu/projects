---
source: http://supervisord.org/ \
created: 2022-12-02T16:18:33 (UTC +01:00) \
tags: [] \
author: 
---

# Supervisor: A Process Control System — Supervisor 4.2.4 documentation
---

- [Introduction](http://supervisord.org/introduction.html)
- [Installing](http://supervisord.org/installing.html)
- [Running Supervisor](http://supervisord.org/running.html)
- [Configuration File](http://supervisord.org/configuration.html)
- [Subprocesses](http://supervisord.org/subprocess.html)
- [Logging](http://supervisord.org/logging.html)
- [Events](http://supervisord.org/events.html)
- [Extending Supervisor’s XML-RPC API](http://supervisord.org/xmlrpc.html)
- [Upgrading Supervisor 2 to 3](http://supervisord.org/upgrading.html)
- [Frequently Asked Questions](http://supervisord.org/faq.html)
- [Resources and Development](http://supervisord.org/development.html)
- [Glossary](http://supervisord.org/glossary.html)

- [XML-RPC API Documentation](http://supervisord.org/api.html)

- [Third Party Applications and Libraries](http://supervisord.org/plugins.html)

- [Changelog](http://supervisord.org/changes.html)

[Supervisor](http://supervisord.org/#)

- [Docs](http://supervisord.org/#) »
- Supervisor: A Process Control System
- [View page source](http://supervisord.org/_sources/index.txt)

___

Supervisor is a client/server system that allows its users to monitor and control a number of processes on UNIX-like
operating systems.

It shares some of the same goals of programs like [_launchd_](http://supervisord.org/glossary.html#term-launchd), [
_daemontools_](http://supervisord.org/glossary.html#term-daemontools), and [
_runit_](http://supervisord.org/glossary.html#term-runit). Unlike some of these programs, it is not meant to be run as a
substitute for init as “process id 1”. Instead it is meant to be used to control processes related to a project or a
customer, and is meant to start like any other program at boot time.

## Narrative Documentation[¶](http://supervisord.org/#narrative-documentation "Permalink to this headline")

- [Introduction](http://supervisord.org/introduction.html)
    - [Overview](http://supervisord.org/introduction.html#overview)
    - [Features](http://supervisord.org/introduction.html#features)
    - [Supervisor Components](http://supervisord.org/introduction.html#supervisor-components)
    - [Platform Requirements](http://supervisord.org/introduction.html#platform-requirements)
- [Installing](http://supervisord.org/installing.html)
    - [Installing to A System With Internet Access](http://supervisord.org/installing.html#installing-to-a-system-with-internet-access)
    - [Installing To A System Without Internet Access](http://supervisord.org/installing.html#installing-to-a-system-without-internet-access)
    - [Installing a Distribution Package](http://supervisord.org/installing.html#installing-a-distribution-package)
    - [Creating a Configuration File](http://supervisord.org/installing.html#creating-a-configuration-file)
- [Running Supervisor](http://supervisord.org/running.html)
    - [Adding a Program](http://supervisord.org/running.html#adding-a-program)
    - [Running **supervisord**](http://supervisord.org/running.html#running-supervisord)
    - [Running **supervisorctl**](http://supervisord.org/running.html#running-supervisorctl)
    - [Signals](http://supervisord.org/running.html#signals)
    - [Runtime Security](http://supervisord.org/running.html#runtime-security)
    - [Running **supervisord
      ** automatically on startup](http://supervisord.org/running.html#running-supervisord-automatically-on-startup)
- [Configuration File](http://supervisord.org/configuration.html)
    - [File Format](http://supervisord.org/configuration.html#file-format)
    - [\[unix\_http\_server\] Section Settings](http://supervisord.org/configuration.html#unix-http-server-section-settings)
    - [\[inet\_http\_server\] Section Settings](http://supervisord.org/configuration.html#inet-http-server-section-settings)
    - [\[supervisord\] Section Settings](http://supervisord.org/configuration.html#supervisord-section-settings)
    - [\[supervisorctl\] Section Settings](http://supervisord.org/configuration.html#supervisorctl-section-settings)
    - [\[program:x\] Section Settings](http://supervisord.org/configuration.html#program-x-section-settings)
    - [\[include\] Section Settings](http://supervisord.org/configuration.html#include-section-settings)
    - [\[group:x\] Section Settings](http://supervisord.org/configuration.html#group-x-section-settings)
    - [\[fcgi-program:x\] Section Settings](http://supervisord.org/configuration.html#fcgi-program-x-section-settings)
    - [\[eventlistener:x\] Section Settings](http://supervisord.org/configuration.html#eventlistener-x-section-settings)
    - [\[rpcinterface:x\] Section Settings](http://supervisord.org/configuration.html#rpcinterface-x-section-settings)
- [Subprocesses](http://supervisord.org/subprocess.html)
    - [Nondaemonizing of Subprocesses](http://supervisord.org/subprocess.html#nondaemonizing-of-subprocesses)
    - [**pidproxy** Program](http://supervisord.org/subprocess.html#pidproxy-program)
    - [Subprocess Environment](http://supervisord.org/subprocess.html#subprocess-environment)
    - [Process States](http://supervisord.org/subprocess.html#process-states)
- [Logging](http://supervisord.org/logging.html)
    - [Activity Log](http://supervisord.org/logging.html#activity-log)
    - [Child Process Logs](http://supervisord.org/logging.html#child-process-logs)
- [Events](http://supervisord.org/events.html)
    - [Event Listeners and Event Notifications](http://supervisord.org/events.html#event-listeners-and-event-notifications)
    - [Event Types](http://supervisord.org/events.html#event-types)
- [Extending Supervisor’s XML-RPC API](http://supervisord.org/xmlrpc.html)
    - [Configuring XML-RPC Interface Factories](http://supervisord.org/xmlrpc.html#configuring-xml-rpc-interface-factories)
- [Upgrading Supervisor 2 to 3](http://supervisord.org/upgrading.html)
- [Frequently Asked Questions](http://supervisord.org/faq.html)
- [Resources and Development](http://supervisord.org/development.html)
    - [Bug Tracker](http://supervisord.org/development.html#bug-tracker)
    - [Version Control Repository](http://supervisord.org/development.html#version-control-repository)
    - [Contributing](http://supervisord.org/development.html#contributing)
    - [Author Information](http://supervisord.org/development.html#author-information)
- [Glossary](http://supervisord.org/glossary.html)

## API Documentation[¶](http://supervisord.org/#api-documentation "Permalink to this headline")

- [XML-RPC API Documentation](http://supervisord.org/api.html)
    - [Status and Control](http://supervisord.org/api.html#status-and-control)
    - [Process Control](http://supervisord.org/api.html#process-control)
    - [Process Logging](http://supervisord.org/api.html#process-logging)
    - [System Methods](http://supervisord.org/api.html#system-methods)

## Plugins[¶](http://supervisord.org/#plugins "Permalink to this headline")

- [Third Party Applications and Libraries](http://supervisord.org/plugins.html)
    - [Dashboards and Tools for Multiple Supervisor Instances](http://supervisord.org/plugins.html#dashboards-and-tools-for-multiple-supervisor-instances)
    - [Third Party Plugins and Libraries for Supervisor](http://supervisord.org/plugins.html#third-party-plugins-and-libraries-for-supervisor)
    - [Libraries that integrate Third Party Applications with Supervisor](http://supervisord.org/plugins.html#libraries-that-integrate-third-party-applications-with-supervisor)

## Release History[¶](http://supervisord.org/#release-history "Permalink to this headline")

- [Changelog](http://supervisord.org/changes.html)
    - [4.2.4 (2021-12-30)](http://supervisord.org/changes.html#id1)
    - [4.2.3 (2021-12-27)](http://supervisord.org/changes.html#id2)
    - [4.2.2 (2021-02-26)](http://supervisord.org/changes.html#id3)
    - [4.2.1 (2020-08-20)](http://supervisord.org/changes.html#id4)
    - [4.2.0 (2020-04-30)](http://supervisord.org/changes.html#id5)
    - [4.1.0 (2019-10-19)](http://supervisord.org/changes.html#id6)
    - [4.0.4 (2019-07-15)](http://supervisord.org/changes.html#id7)
    - [4.0.3 (2019-05-22)](http://supervisord.org/changes.html#id8)
    - [4.0.2 (2019-04-17)](http://supervisord.org/changes.html#id9)
    - [4.0.1 (2019-04-10)](http://supervisord.org/changes.html#id10)
    - [4.0.0 (2019-04-05)](http://supervisord.org/changes.html#id11)
    - [3.4.0 (2019-04-05)](http://supervisord.org/changes.html#id12)
    - [3.3.5 (2018-12-22)](http://supervisord.org/changes.html#id13)
    - [3.3.4 (2018-02-15)](http://supervisord.org/changes.html#id14)
    - [3.3.3 (2017-07-24)](http://supervisord.org/changes.html#id15)
    - [3.3.2 (2017-06-03)](http://supervisord.org/changes.html#id16)
    - [3.3.1 (2016-08-02)](http://supervisord.org/changes.html#id17)
    - [3.3.0 (2016-05-14)](http://supervisord.org/changes.html#id18)
    - [3.2.4 (2017-07-24)](http://supervisord.org/changes.html#id19)
    - [3.2.3 (2016-03-19)](http://supervisord.org/changes.html#id20)
    - [3.2.2 (2016-03-04)](http://supervisord.org/changes.html#id21)
    - [3.2.1 (2016-02-06)](http://supervisord.org/changes.html#id22)
    - [3.2.0 (2015-11-30)](http://supervisord.org/changes.html#id23)
    - [3.1.4 (2017-07-24)](http://supervisord.org/changes.html#id24)
    - [3.1.3 (2014-10-28)](http://supervisord.org/changes.html#id25)
    - [3.1.2 (2014-09-07)](http://supervisord.org/changes.html#id26)
    - [3.1.1 (2014-08-11)](http://supervisord.org/changes.html#id27)
    - [3.1.0 (2014-07-29)](http://supervisord.org/changes.html#id28)
    - [3.0.1 (2017-07-24)](http://supervisord.org/changes.html#id29)
    - [3.0 (2013-07-30)](http://supervisord.org/changes.html#id30)
    - [3.0b2 (2013-05-28)](http://supervisord.org/changes.html#b2-2013-05-28)
    - [3.0b1 (2012-09-10)](http://supervisord.org/changes.html#b1-2012-09-10)
    - [3.0a12 (2011-12-06)](http://supervisord.org/changes.html#a12-2011-12-06)
    - [3.0a11 (2011-12-06)](http://supervisord.org/changes.html#a11-2011-12-06)
    - [3.0a10 (2011-03-30)](http://supervisord.org/changes.html#a10-2011-03-30)
    - [3.0a9 (2010-08-13)](http://supervisord.org/changes.html#a9-2010-08-13)
    - [3.0a8 (2010-01-20)](http://supervisord.org/changes.html#a8-2010-01-20)
    - [3.0a7 (2009-05-24)](http://supervisord.org/changes.html#a7-2009-05-24)
    - [3.0a6 (2008-04-07)](http://supervisord.org/changes.html#a6-2008-04-07)
    - [3.0a5 (2008-03-13)](http://supervisord.org/changes.html#a5-2008-03-13)
    - [3.0a4 (2008-01-30)](http://supervisord.org/changes.html#a4-2008-01-30)
    - [3.0a3 (2007-10-02)](http://supervisord.org/changes.html#a3-2007-10-02)
    - [3.0a2 (2007-08-24)](http://supervisord.org/changes.html#a2-2007-08-24)
    - [3.0a1 (2007-08-16)](http://supervisord.org/changes.html#a1-2007-08-16)
    - [2.2b1 (2007-03-31)](http://supervisord.org/changes.html#b1-2007-03-31)
    - [2.1 (2007-03-17)](http://supervisord.org/changes.html#id31)
    - [2.1b1 (2006-08-30)](http://supervisord.org/changes.html#b1-2006-08-30)
    - [2.0 (2006-08-30)](http://supervisord.org/changes.html#id32)
    - [2.0b1 (2006-07-12)](http://supervisord.org/changes.html#b1-2006-07-12)
    - [1.0.7 (2006-07-11)](http://supervisord.org/changes.html#id33)
    - [1.0.6 (2005-11-20)](http://supervisord.org/changes.html#id34)
    - [1.0.5 (2004-07-29)](http://supervisord.org/changes.html#id35)
    - [1.0.4 or “Alpha 4” (2004-06-30)](http://supervisord.org/changes.html#or-alpha-4-2004-06-30)
    - [1.0.3 or “Alpha 3” (2004-05-26)](http://supervisord.org/changes.html#or-alpha-3-2004-05-26)
    - [1.0.2 or “Alpha 2” (Unreleased)](http://supervisord.org/changes.html#or-alpha-2-unreleased)
    - [1.0.0 or “Alpha 1” (Unreleased)](http://supervisord.org/changes.html#or-alpha-1-unreleased)
