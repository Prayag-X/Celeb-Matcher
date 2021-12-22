from jina import Document, DocumentArray, Flow

d1 = (
    Document(uri='Dataset/Aamir_Khan/Aamir.51.jpg')
    .load_uri_to_image_blob()
    .set_image_blob_shape(shape=(224, 224))
    .set_image_blob_normalization()
)

d2 = (
    Document(uri='Dataset/Akshaye_Khanna/Akshaye_Khanna.12.jpg')
    .load_uri_to_image_blob()
    .set_image_blob_shape(shape=(224, 224))
    .set_image_blob_normalization()
)

q = (
    Document(uri='Dataset/Aamir_Khan/Aamir.68.jpg')
    .load_uri_to_image_blob()
    .set_image_blob_shape(shape=(224, 224))
    .set_image_blob_normalization()
)

docs = DocumentArray(
    [
        d1,d2,
    ]
)


flow = (
    Flow()
    .add(uses="jinahub://ImageTorchEncoder", uses_with={'model_name': 'resnet50'}, name="encoder", install_requirements=True)
    # .add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer")
)

with flow:
    flow.index(inputs=docs)
    # response = flow.search(inputs=q, return_results=True)