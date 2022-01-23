from jina import Document, DocumentArray, Flow
import os
import glob
from Utilities import *


f = (
    Flow()
    .add(uses='jinahub://CLIPImageEncoder/latest', install_requirements=True)
    .add(uses="jinahub://SimpleIndexer", install_requirements=True, name="indexer")
)

def index():
    doc_list=[]

    for filename in glob.glob('Dataset/*/*.jpg'):
        doc_list.append(
            Document(uri=filename)
            .load_uri_to_image_blob()
        )

    doc = DocumentArray(doc_list)
    
    with f:
        f.index(inputs=doc, show_progress=True)


def Jina_run(filename):
    if(not os.path.isdir('workspace')):
        index()

    upload='static/uploads/'+filename
    Crop(upload)

    q = (
        Document(uri=upload)
        .load_uri_to_image_blob()
    )

    with f:
        response = f.search(inputs=q, return_results=True, show_progress=True)

    matches = response[0].data.docs[0].matches
    return(matches[0].uri)