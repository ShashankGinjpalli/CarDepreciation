# CarDepreciation

### Setting Up Mongo DB Locally

Create a /Data/db where you want to store the database 

`brew tap mongodb/brew`
`brew install mongodb-community@4.4`

To start the server: 
`mongod --dbpath Absolute Path to /Data/db folder`

Create New Database: 
- Open a new Terminal
- `mongo`
- `use CarData`

Create a .env file in Server Folder
paste: `DATABASE_URL=mongodb://localhost:27017/CarData`

### Setting up and Starting the Server
- Using Node v15.12.0
- Navigate to the Server Directory run: 
- `npm install`

- `npm start` to start the server

### Application Routes: 
__GET: `http://localhost:3000/carListings/specific`__
requestbody:
`
{
    "make": "String",
    "title": "String", 
    "year": "String"
}
`

- gets cars of a specific make and model from the database


__Get: `http://localhost:3000/carListings/all`__
- Gets all of the listings from the database

__Get: `http://localhost:3000/carListings/zip`__
requestbody: 
`
{
    zipcode: Number
}
`
- gets the cars in the database that are in the zipcode


POST: `http://localhost:3000/carListings`

requestbody:
`
{
    "make": "String",
    "title": "String",
    "year": "String", 
    "price": "String",
    "mileage": "String", 
    "condition": "String", 
    "specifications": "String",
    "zipcode": "String"
}
`

