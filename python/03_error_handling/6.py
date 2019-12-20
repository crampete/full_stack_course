MONGO_ENGINE_AVAILABLE = True
try:
    import mongoengine
except ImportError:
    print("mongoengine not available so using pymongo")
    MONGO_ENGINE_AVAILABLE = False
    import pymongo