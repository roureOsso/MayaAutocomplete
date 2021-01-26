# MayaAutocomplete
**MayaAutocomplete** will provide you with a properly built auto-complete to help you while coding inside Maya. These one will suggest the available mayaCommands and the available arguments for the command being used.

You can download an **"AutoComplete"** already _buit_ for you or build your own.

## What does MayaAutocomplete?
**MayaAutocomplete** will parse the official Maya documentation to generate a new `__init__.py`.  
Some doc versions can be downloaded during runtime, but you will be asked to use an already downloaded one.  

All is done using vanilla python.<br /><br />


## Usage  
Some auto-completes for the Maya major versions are ready to be downloaded and configured into your IDE.

Build your own autocomplete:
1. Download the latest release or simply download the **"built.py"**.
2. Run this file in your system console, use any python version above 2.7 or the maya interpreter it self.
3. Only the **"DocDownload"** _ready_ can be downloaded and built during run-time.
4. If your version is not ready, download the documentation from the [official site](https://knowledge.autodesk.com/support/maya/troubleshooting/caas/downloads/content/download-install-maya-product-help.html) and unzip it to a new folder.
5. Follow the instructions. At the end you can ask for more detailed information on how to proceed with the new file.
6. A new `__init__.py` file will be created or overridden.<br /><br />


What to do with an autoCompelte `__init__.py` file:
1. Download the corresponding [maya devkit](https://www.autodesk.com/developer-network/platform-technologies/maya).
2. You can delete everything except this folder: **\devkitBase\devkit\other\pymel\extras\completion\py**
3. Open **py\maya\cmds**
4. Replace the `__init__.py` file located here.<br /><br />


#### Status

[![PythonCompatibilities](https://img.shields.io/badge/python-2.7%20%7C%203.x-blue)](https://www.python.org/downloads/)


| Maya Version | Availability
|:----------|:-----
| 2020.4 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2020.3 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2020.2 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2020.1 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2020 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-brightgreen)](autoCompleteVersions/2020py) [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2019.3 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2019.2 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2019.1 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2019 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-brightgreen)](autoCompleteVersions/2019py) [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2018.7 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2018.6 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2018.5 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2018.4 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2018.3 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2018.2 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2018.1 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2018 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-brightgreen)](autoCompleteVersions/2018py) [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2017.5 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2017.4 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2017.3 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2017.2 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2017.1 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-red)]()
| 2017 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
| 2016 | [![AC status](https://img.shields.io/badge/AutoComplete-Built-red)]() [![AC status](https://img.shields.io/badge/DocDownload-Ready-brightgreen)]()
