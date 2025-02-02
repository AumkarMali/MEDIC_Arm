from pymongo import MongoClient
from pymongo.errors import PyMongoError  # Use PyMongoError for handling connection issues

# Replace with your MongoDB connection string
mongo_uri = "mongodb+srv://aumkarmali539:AM20060305!_ilovesushi@clusterdata.gmzht.mongodb.net/?retryWrites=true&w=majority&appName=ClusterData"

try:
    # Create a MongoClient object and connect to MongoDB
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)  # Timeout set to 5 seconds

    # Try to access a test database
    client.admin.command('ping')  # Ping MongoDB to see if the server is responding
    print("MongoDB connection successful!")

except PyMongoError as e:
    print(f"Failed to connect to MongoDB. Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
