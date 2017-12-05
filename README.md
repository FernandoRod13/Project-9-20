# Project-9-20
Project 9/20 is the easy way to manage resources for disaster relief efforts in Puerto Rico after hurricane Maria
## Overview
Currently the project consist on implementing and testing the backend of an application used to manage resources on a Disaster Site, such as Puerto Rico after hurricane Maria. The data in the application is managed by a relational database system, and exposed to client applications through a REST API. You will build the database application and REST API, which form the backend of the system. Your database engine must be relational, and you must implement the code in either Java, Python, or JavaScript. The backend site will enable the user to browse categories for resources (i.e., water, food, medications, tools, heavy equipment, etc.), search for specific items, specify who is supplying items, and who needs the items. Also, add the location (GPS) and address of the person in need and that of the supplier. The project will eventually include a web-based application wich will be used as a dashboard to manage resources, view statistics among other things.

## REST API
### Details
We have opted to host our project using [Google Cloud App Engine](https://cloud.google.com/appengine/ "App Engine Homepage") and [Google Cloud SQL](https://cloud.google.com/sql/ "Cloud SQL Homepage"). Currently you may access the REST API using the base URL: 
>[https://project-9-20-187720.appspot.com/](https://project-9-20-187720.appspot.com/ "REST API Base URL")

### Documentation
#### Resources
##### Get all resources
`https://<baseURL>/resources`
##### Get all requested resources
`https://<baseURL>/resources/requested`
##### Get all available resources
`https://<baseURL>/resources/available`
##### Find all available resources by keyword
`https://<baseURL>/resources/available/find/<keyword>`
##### Find all requested resources by keyword
`https://<baseURL>/resources/requested/find/<keyword>`
##### Get all requested resource categories
`https://<baseURL>/resources/requested/category`
##### Get all resources requested by category with a keyword
`https://<baseURL>/resources/requested/category/<keyword>`
##### Get all resources available by category with a keyword
`https://<baseURL>/resources/available/category/<keyword>`
#### Statistics
##### Get daily statistics of available resources
`https://<baseURL>/dashboard/daily_statistics/resources_available`
##### Get daily statistics of requested resources
`https://<baseURL>/dashboard/daily_statistics/resources_inneed`
##### Get weekly statistics of available resources
`https://<baseURL>/dashboard/trending_statistics/resources_available`
##### Get weekly statistics of requested resources
`https://<baseURL>/dashboard/trending_statistics/resources_inneed`
##### Get regional statistics of available resources
`https://<baseURL>/dashboard/trending_statistics/resources_available/findBySenate/<region>`
##### Get regional statistics of requested resources
`https://<baseURL>/dashboard/trending_statistics/resources_inneed/findBySenate/<region`