# Copyright 2023 Lia Toumazi

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests
import os

# This script sends a GET request to the specified URL and then 
# writes the contents of the response (the CSS file) to a local file 
# named after the css and javascript files of the website. 
# You can also use the urllib library that comes with Python, 
# it has a method urlretrieve() that can be used to download the 
# files.

url = "http://www.catoumazis.com"  # replace with the URL of the target website

# find the css files of the website
css_files = ["skin_man.css", "lightbox.css", "site.css", "style.css", "skin.css"]

for css in css_files:
    response = requests.get(url + "/{}".format(css))
    with open(css, "wb") as f:
        f.write(response.content)

# find the javascript files of the website
js_files = ["functions.js", "jquery.js", "addthis_widget.js", "functions.js", 
            "moatframe.js", "jquery.jcarousel.js", "jquery.lightbox.js"]

for js in js_files:
    response = requests.get(url + "/{}".format(js))
    with open(js, "wb") as f:
        f.write(response.content)



