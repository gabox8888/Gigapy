'''
This is an API to more easily interact with the gigaword dataset 
'''

import os
import tarfile

class Gigaword:

    def __init__(self,path):
        # Path to data
        self.path = path
        self.corpora = self.getCorpora()
        self.documents = self.getDocuments()

    def getDocuments(self):
        documents = {i:[] for i in self.corpora}
        for i in self.corpora:
            documents[i] += [name for name in os.listdir(os.path.join(self.path,i)) if os.path.isfile(os.path.join(self.path, i ,name))]
        return documents

    def getCorpora(self):
        return [name for name in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, name))]

    
    def getFile(self,corpus,index):
        if index > len(self.documents[corpus]) : 
            return None
        else:
            with tarfile.open(os.path.join(self.path,corpus,self.documents[corpus][index])) as tf:
                for entry in tf:  # list each entry one by one
                    fileobj = tf.extractfile(entry)
                    for i in fileobj:
                        print(i)