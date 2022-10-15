db.createUser(
{
    user: "christhoval",
    pwd: "S3cr3tP4ssW0rD",
    roles: [
      { role: "readWrite", db: "college" }
    ]
})

print("Started Adding the Users.");
db = db.getSiblingDB("admin");
db.createUser({
  user: "christhoval",
  pwd: "S3cr3tP4ssW0rD",
  roles: [{ role: "readWrite", db: "admin" }],
});
print("End Adding the User Roles.");

/*
use admin;
db.grantRolesToUser('devA', ['readWriteAnyDatabase']);
db.grantRolesToUser('devB', ['readWriteAnyDatabase']);
 */

// db.grantRolesToUser('devB', [{ role: 'readWrite', db: 'client' }]);