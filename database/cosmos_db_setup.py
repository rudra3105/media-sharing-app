from azure.cosmos import CosmosClient, exceptions

client = CosmosClient('COSMOS_ENDPOINT', 'COSMOS_KEY')
database_name = 'mediaDB'
container_name = 'mediaMetadata'

try:
    db = client.create_database_if_not_exists(id=database_name)
    container = db.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/id"),
        offer_throughput=400
    )
    print("Cosmos DB setup complete.")
except exceptions.CosmosResourceExistsError:
    print("Database or container already exists.")
