import mongoengine

# mongodb://<admin>:<admin123>@ds111623.mlab.com:11623/mangahub

host = "ds111623.mlab.com" 
port = 11623
db_name = "mangahub"
user_name = "admin"
password = "admin123"

def connect():
    mongoengine.connect(
        db_name,
        host=host,
        port=port,
        username=user_name,
        password=password
    )