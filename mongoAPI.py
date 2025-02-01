from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb+srv://aumkarmali539:AM20060305!_ilovesushi@clusterdata.gmzht.mongodb.net/?retryWrites=true&w=majority&appName=ClusterData")  

# 2. Select database & collection
db = client["RobotMotion"]  # Database name
collection = db["motion"]  # Collection name

# 3. Insert motion data
data = {
    "name": "Q-tip",
    "data": 0,
}
collection.insert_one(data)

# 4. Find and print the inserted data by name
user = collection.find_one({"name": "Q-tip"})  # Retrieve by name
if user:
    print("Data for Q-tip:", user.get("data"))
else:
    print("No data found for Q-tip.")

# 5. Close the connection (optional)
client.close()
