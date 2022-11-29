> Permissions 

Inotify Watches Limit 
https://youtrack.jetbrains.com/articles/IDEA-A-2/Inotify-Watches-Limit?_ga=2.156876731.161350735.1619884188-801908360.1618083116&_gac=1.161929678.1619361964.Cj0KCQjwppSEBhCGARIsANIs4p4HGgzDNdJeSo518OuhvuGHr0FqZoHxSkImDDH_MpheYQp0TB9X8p4aAmmBEALw_wcB \


> Del plugin manually

https://intellij-support.jetbrains.com/hc/en-us/articles/206544519
Configuration (idea.config.path): ~/.config/JetBrains/IntelliJIdea2020.3
Plugins (idea.plugins.path): ~/.local/share/JetBrains/IntelliJIdea2020.3
System (idea.system.path): ~/.cache/JetBrains/IntelliJIdea2020.3
Logs (idea.log.path): ~/.cache/JetBrains/IntelliJIdea2020.3/log

> Add FE plugins to PyCharm

https://intellij-support.jetbrains.com/hc/en-us/community/posts/205807379-PyCharm-vs-WebStorm
https://blog.jetbrains.com/webstorm/2020/05/plugins-for-webstorm-you-need-to-know-about/
https://stackoverflow.com/questions/55506761/what-is-the-difference-between-webstorm-phpstorm-pycharm-and-rubymine
https://www.jetbrains.com/help/pycharm/live-editing.html
https://www.jetbrains.com/help/pycharm/javascript-specific-guidelines.html
https://www.jetbrains.com/help/pycharm/javascript-specific-guidelines.html#ws_js_syntax_highlighting

1) PyCharm is not a strict superset of WebStorm. A number of plugins specific for Web development (XPathView, XSLT Debugger, NodeJS support, JsTestDriver integration) are bundled with WebStorm but not with PyCharm. Some of them (NodeJS for example) can be installed into PyCharm using the plugin manager.

In the future, we plan to keep the set of functionality in each particular product tailored for its target audience.

2) The only difference between PyCharm and Webstorm is the following plugins bundled with WebStorm:
   asp

CucumberJavaScript
Dart
EJS
Jade

LiveEdit

Meteor
NodeJS
QuirksMode

RefactorX

WebComponents
Yeoman
js-karma
jsp
node-remote-interpreter
spy-js
vuejs
w3validators

All of them you can install in Pycharm| Settings (Preferences for OS X)| Plugins| Install JetBrains Plugin...

3) PhpStorm = WebStorm + PHP + Database support

4) HELP https://www.youtube.com/watch?v=RlNEwBhckDA&ab_channel=JetBrainsTV

> Other

1) Store settings to remote (jetbrains or github) \
   https://www.jetbrains.com/help/pycharm/sharing-your-ide-settings.html#settings-repository


2) Compile Cython Extensions Error - Pycharm IDE \
   https://stackoverflow.com/questions/47257766/compile-cython-extensions-error-pycharm-ide
   https://www.jetbrains.com/help/pycharm/2017.3/cython-speedups.html
   https://stackoverflow.com/questions/43047284/how-to-install-python3-devel-on-red-hat-7
   

3) [Directories used by the IDE to store settings, caches, plugins and logs](https://intellij-support.jetbrains.com/hc/en-us/articles/206544519-Directories-used-by-the-IDE-to-store-settings-caches-plugins-and-logs)
   ```sh
   Configuration (idea.config.path): ~/.config/JetBrains/IntelliJIdea2022.2
   Plugins (idea.plugins.path): ~/.local/share/JetBrains/IntelliJIdea2022.2
   System (idea.system.path): ~/.cache/JetBrains/IntelliJIdea2022.2
   Logs (idea.log.path): ~/.cache/JetBrains/IntelliJIdea2022.2/log
   ```