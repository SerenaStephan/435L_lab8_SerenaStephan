## Version 1: Lab 5 API
- Port: 5000
- Preserves existing Lab 5 routes: GET /api/users, GET /api/users/<user_id>, POST /api/users/add, PUT /api/users/update, DELETE /api/users/delete/<user_id>.

## Version 2: get_users
- Port: 3000
- GET /get_users (also GET /api/get_users) returns a JSON list of names from SQLite users table.

## Database
- Database is stored inside each container; the two images do NOT share live state. Each begins with its own copy of the source database. 




