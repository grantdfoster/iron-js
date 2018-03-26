# ironJS
*an iron python module to serve Javascript Applications in pyRevit*

## Usage
* a pyRevit module for rendering a Javascript Application
* uses cefpython3 (chromium library) and a Python35 subprocess (doesn't support iron python)
* Python35 must have the cefpython3 library installed in site-packages!

* clone (the base app)[https://github.com/grantdfoster/javascript-app-template] to begin your Javascript project!
* after building your app, copy the following files to your pyRevit tool
```
dist
    build.js
    build.js.map
index.html
```

``` python
import pyjs
pyjs.run(app=path_to_index.html, port=1111)
```

## Note:
* because this library uses a python subprocess, the standard cefpython3 javascript <> python bindings cannot be used
* instead, for seamless user experience:
    1. user interaction with app can be recorded in javascript (i.e. with Vue)
    2. before app close, store interaction results on local filesytem with javascript (i.e. with fs)
    3. on app close, any code after pyjs.run() will continue to run...
    4. load results in python (i.e. with json.loads()) and process
