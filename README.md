# ironJS
*an iron python module to serve Javascript Applications in pyRevit*

## How?
* uses cefpython3 (chromium library) and thus a Python35 subprocess (cefpython3 doesn't support iron python)

## Initial Setup
*if you are developing on pyWeWork or pyWeWork-Dev, this has been setup already!*
* place ironJS and a copy of Python35 in a lib folder so pyRevit sees the libraries
* make sure **python_path** is set correctly (pointing to Python35) in **__init__.py**
* your copy of Python35 must have the cefpython3 library in site-packages!

## Developing an App
* clone [the base app](https://github.com/grantdfoster/javascript-app-template) to begin your Javascript project!
* after building your app, copy the following files to your pyRevit tool
```
dist
    build.js
    build.js.map
index.html
```

## Run an App
*in your pyRevit tool script...*
``` python
import ironJS
ironJS.run(app=path_to_index.html, port=1111, endpoint='')
```

## Note:
* because this library uses a python subprocess, the standard cefpython3 javascript <> python bindings cannot be used
* instead, for seamless user experience:
    1. user interaction with app can be recorded in javascript (i.e. with Vue)
    2. before app close, store interaction results on local filesytem with javascript (i.e. with fs)
    3. on app close, any code after ironJS.run() will run...
    4. load results in python (i.e. with json.loads()) and process
