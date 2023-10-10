import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# This function creates a new user.
@app.route("/users", methods=["POST"])
def create_user():
  """
  Creates a new user.

  Request body:
    {
      "name": "string"
    }

  Response body:
    {
      "id": int,
      "name": "string"
    }
  """

  user_data = json.loads(request.data)

  # Validate the request body.
  if not user_data or not user_data.get("name"):
    return jsonify({"error": "Invalid request body."}), 400

  # Create the new user in the database.
  # ...

  # Return the new user.
  return jsonify({
    "id": user.id,
    "name": user.name
  }), 201

# This function gets all users from the database.
@app.route("/users", methods=["GET"])
def get_all_users():
  """
  Gets all users from the database.

  Response body:
    [{
      "id": int,
      "name": "string"
    }]
  """

  # Get all users from the database.
  # ...

  # Return the users.
  return jsonify([user.to_dict() for user in users])

# This function gets a single user by ID.
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
  """
  Gets a single user by ID.

  Request path variable:
    user_id: int

  Response body:
    {
      "id": int,
      "name": "string"
    }
  """

  # Get the user from the database.
  # ...

  # If the user does not exist, return a 404 error.
  if not user:
    return jsonify({"error": "User does not exist."}), 404

  # Return the user.
  return jsonify(user.to_dict())

# This function updates a user's information.
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
  """
  Updates a user's information.

  Request path variable:
    user_id: int

  Request body:
    {
      "name": "string"
    }

  Response body:
    {
      "id": int,
      "name": "string"
    }
  """

  # Get the user from the database.
  # ...

  # If the user does not exist, return a 404 error.
  if not user:
    return jsonify({"error": "User does not exist."}), 404

  # Update the user's information.
  # ...

  # Return the updated user.
  return jsonify(user.to_dict())

# This function deletes a user.
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
  """
  Deletes a user.

  Request path variable:
    user_id: int

  Response body:
    {
      "message": "User deleted successfully."
    }
  """

  # Get the user from the database.
  # ...

  # If the user does not exist, return a 404 error.
  if not user:
    return jsonify({"error": "User does not exist."}), 404

  # Delete the user from the database.
  # ...

  # Return a success response.
  return jsonify({"message": "User deleted successfully."})

# This function starts the Flask server.
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
                    
