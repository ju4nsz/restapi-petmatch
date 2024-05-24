# REST API using FastAPI
##### This project is an REST API using the FastAPI technology, contains methods HTTP such as GET, POST, PUT and DELETE.
##### This REST API have authentication with JWT, authorization with roles ("user", "admin") and I try to follow the REST architecture in the APIs.
#### I make a endpoint "/authenticate" for the login, this endpoint return an access token bearer, first verify the credentials in the db, and verify if the user is active, if all it's good, return the token.
#### Then, this REST API have endpoints for users, memberships, pets, pets type, roles and matchs.
#### The users can create pets, obtain pets and update pets.
#### The admins can do CRUD operations with the roles and memberships.
### The pets can have matchs with other pets.
## Authentication
- **POST /authenticate**: Authenticates the user and returns an access token.
  - Request Body: OAuth2PasswordRequestForm

## Matches
- **GET /matches**: Returns a list of matches.
- **POST /matches**: Creates a new match.
  - Request Body: schemes.MatchCreate
- **GET /matches/{id}**: Returns matches for a specific pet.
  - Parameter: id (Pet ID)
  
## Memberships
- **GET /memberships**: Returns a list of memberships.
- **POST /memberships**: Creates a new membership.
  - Request Body: schemes.MemberShipCreate
- **GET /memberships/{id}**: Returns a specific membership.
  - Parameter: id (Membership ID)
- **PUT /memberships**: Updates a specific membership.
  - Request Body: schemes.MemberShip
- **DELETE /memberships/{id}**: Deletes a specific membership.
  - Parameter: id (Membership ID)

## Pets
- **GET /pets**: Returns a list of pets.
- **POST /pets**: Creates a new pet.
  - Request Body: schemes.PetBase
- **GET /pets/{id}**: Returns a specific pet.
  - Parameter: id (Pet ID)
- **PUT /pets**: Updates a specific pet.
  - Request Body: schemes.PetUpdate
- **DELETE /pets/{id}**: Deletes a specific pet.
  - Parameter: id (Pet ID)

## Pet Types
- **GET /petstype**: Returns a list of pet types.
- **POST /petstype**: Creates a new pet type.
  - Request Body: schemes.PetTypeCreate
- **GET /petstype/{id}**: Returns a specific pet type.
  - Parameter: id (Pet Type ID)
- **PUT /petstype**: Updates a specific pet type.
  - Request Body: schemes.PetType
- **DELETE /petstype/{id}**: Deletes a specific pet type.
  - Parameter: id (Pet Type ID)

## Roles
- **GET /roles**: Returns a list of roles.
- **POST /roles**: Creates a new role.
  - Request Body: schemes.RoleCreate
- **GET /roles/{id}**: Returns a specific role.
  - Parameter: id (Role ID)
- **PUT /roles**: Updates a specific role.
  - Request Body: schemes.Role
- **DELETE /roles/{id}**: Deletes a specific role.
  - Parameter: id (Role ID)

## Users
- **GET /users**: Returns a list of users.
- **POST /users**: Creates a new user.
  - Request Body: schemes.UserCreate
- **GET /users/{id}**: Returns a specific user.
  - Parameter: id (User ID)
- **PUT /users**: Updates a specific user.
  - Request Body: schemes.UserUpdate
- **DELETE /users/{id}**: Deletes a specific user.
  - Parameter: id (User ID)

