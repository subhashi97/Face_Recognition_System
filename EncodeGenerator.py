import os
import cv2
import face_recognition
import pickle
import firebase_admin
from firebase_admin import credentials, db, storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "database_Link",
    'storageBucket': "Storage_Link"
})

# Importing member images into a list
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []

memberIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    memberIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    #print(path)
    #print(os.path.splitext(path)[0])

print(memberIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, memberIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")