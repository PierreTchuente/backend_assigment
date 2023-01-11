# backend_assignments

# How To Use Repo
This is the backend api runing a pyramid app on uwsgi server with nginx as proxy server


### Setup on local machine
You will need to have docker running on your machine:
This app is running on python 3.7
1. `docker-compose build`, to build the api, nginx and mysql image
2. `docker-compose up` to start the proxy server and the api
3. `docker-compose down` to stop all containers
4. Connect to the db using the credential available in the `docker-compose.yaml file`. you can use any mysql client
5. run the `create_data_table.sql` script to create the table.
6. Test the application using postman for example.

## Making request to the API
The API can be tested using postman
1. receiving endpoint, create the data in the db
 - Http Method: POST
 - uri 127.0.0.1/receive/message
 - sample payload
``
{
      "message": {
          "attributes": {
              "key": "value"
          },
          "data": "ewoic2VyaWFsIjogIjAwMDEwMDAwMDEwMCIsCiJhcHBsaWNhdGlvbiI6IDExLAoiVGltZSI6ICIyMDIyLTExLTA4VDA0OjAwOjA0LjMxNzgwMSIsCiJUeXBlIjogInhrZ3ciLAoiZGV2aWNlIjogIlRlc3REZXZpY2UiLAoidjAiOiAxMDAwMTMsCiJ2MSI6IDAuNjksCiJ2MiI6IDEuMzEsCiJ2MyI6IDAuMTgsCiJ2NCI6IDAsCiJ2NSI6IDAuOCwKInY2IjogMCwKInY3IjogMjY5NjUsCiJ2OCI6IDAuMSwKInY5IjogOTc3NTc0OTYsCiJ2MTAiOiAwLAoidjExIjogMCwKInYxMiI6IDEuODQsCiJ2MTMiOiAwLAoidjE0IjogMC43LAoidjE1IjogMTAwMTAsCiJ2MTYiOiAxMDAwMTMsCiJ2MTciOiAyNjk2NSwKInYxOCI6IDIuNzIKfQ==",
          "messageId": "2070443601311540",
          "message_id": "2070443601311540",
          "publishTime": "2021-02-26T19:13:55.749Z",
          "publish_time": "2021-02-26T19:13:55.749Z"
      },
     "subscription": "projects/myproject/subscriptions/mysubscription"
}
``
2. retrieve the data in the db
   1. retrieve a single data
   - Http Method: GET
   - uri 127.0.0.1/{id} (id = 1, 2, ..)
   2. retrieve the list of data
   - Http Method: GET
   - uri 127.0.0.1/data?page_number=0&page_size=5
   - take page_number and page_size as query parameter
