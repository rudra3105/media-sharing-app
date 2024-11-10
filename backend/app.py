from flask import Flask, request, jsonify
import azure.storage.blob as azure_blob
import cosmos_client  # Custom module for Cosmos DB

app = Flask(__name__)

# Upload endpoint
@app.route('/upload', methods=['POST'])
def upload_media():
    file = request.files['media']
    blob_service = azure_blob.BlobServiceClient.from_connection_string('AZURE_BLOB_CONNECTION_STRING')
    container_client = blob_service.get_container_client('media-container')
    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(file.read(), overwrite=True)
    return jsonify({"message": "Upload successful", "filename": file.filename})

# CRUD operations here (get, update, delete)

if __name__ == '__main__':
    app.run(debug=True)
