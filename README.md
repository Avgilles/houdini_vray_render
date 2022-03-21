# Python Project Manager on houdini

![demo](/preview/preview.gif)

This custom panel can allow to open diferent scene in houdini.
To use this tool, clone this repo in your script path in houdini :

This an example :  
C:/Users/Gilles AVRAAM/Documents/houdini19.0/scripts/python

* Change in the code your real houdini path in the variable "**scriptPath**"

Then create a new panel interface and paste the following code :

```python
from importlib import reload
from projectManager import project

reload(project)

def onCreateInterface():
    return project.onCreateInterface()
```