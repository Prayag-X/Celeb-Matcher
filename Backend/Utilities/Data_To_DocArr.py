from jina import Document, DocumentArray
import glob
import pickle

doc_list=[]

for filename in glob.glob('Dataset/*/*.jpg'):
    doc_list.append(
        Document(uri=filename)
        .load_uri_to_image_blob()
        # .set_image_blob_normalization()
        # .set_image_blob_shape(shape=(224, 224))
        # .set_image_blob_channel_axis(-1, 0)
    )

with open("Data_Store", "wb") as fp:
    pickle.dump(doc_list, fp)
