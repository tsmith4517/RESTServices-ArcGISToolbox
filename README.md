# RESTServices-ArcGISToolbox
REST Crawler Overview
Features
This project is intended to provide a base resource that allows someone to crawl an ArcGIS Server REST endpoint using Python, and retrieve all of the service URLs that are either publicly available, or available via a token. The functions.py script contains functions that perform an optional token generation and the actual crawling of the REST endpoint. getServices.py takes the results from functions.py and writes them to a text file (services.txt) that can be parsed by downstream scripts or processes to send additional requests, check status, or administrate.

This repository uses the 'urllib' libraries so as to be compatible with out-of-the-box functionality. Upon request, this sample can be converted to use the much more pythonic 'requests' module instead.

Instructions
Download the RESTCrawler ZIP file.
Open getServices.py and edit the restURL and protocol parameters as desired (protocol can be "SOAP" or "REST").
If you wish to use a token, set getToken to True, and specify the appropriate tokenURL,username, and password values.
Save getServices.py and execute it. The included services.txt file will be updated with all of the services available at the specified REST endpoint.
Requirements
An internet connection
Access to a REST endpoint
A python editor
Issues
If you find or bug or think of a feature you'd like to see, please let me know by submitting an issue.

Contributing
I follow the Esri Github guidelines for contributing. Please see guidelines for contributing.

Licensing
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

A copy of the license is available in the repository.
