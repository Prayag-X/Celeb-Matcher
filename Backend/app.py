from jina import Document, DocumentArray, Flow
import pickle
import os
import time


# NOTE
# NOTE
# NOTE
'''
IF OS.SYSTEM SHOWS ERROR THEN MANUALLY RUN Utilities/Data_To_DocArr.py

I will fix it later T_T
'''
# NOTE
# NOTE
# NOTE


try:
    with open("Utilities/Data_Store", "rb") as fp:
        doc = DocumentArray(pickle.load(fp))

except:
    os.system('Utilities/Data_To_DocArr.py')
    time.sleep(60)
    with open("Utilities/Data_Store", "rb") as fp:
        doc = DocumentArray(pickle.load(fp))

# doc.plot_image_sprites('Working.png')

q = (
    Document(uri='Aamir.68.jpg')
    .load_uri_to_image_blob()
    # .set_image_blob_normalization()
    # .set_image_blob_shape(shape=(224, 224))
    # .set_image_blob_channel_axis(-1, 0)
)

f = (
    Flow()
    .add(uses='jinahub://CLIPImageEncoder/latest', install_requirements=True)
    .add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer")
)

with f:
    f.index(inputs=doc, show_progress=True)
    response = f.search(inputs=q, return_results=True, show_progress=True)

matches = response[0].data.docs[0].matches

for match in matches:
    print(match)

