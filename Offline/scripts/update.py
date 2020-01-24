__author__ = "Sunil Barve"
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

import os
import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bson import ObjectId
import pymongo

class MongoConn(object):
    """
        Class to handle operations on Mongodb
    """
    def __init__(self, connection_obj, collection="test"):
        """
            Constructor of Mongo Connection.
        """
        self.database = connection_obj['DATABASE']
        self.collection = collection
        self.conn = pymongo.MongoClient(host=connection_obj['HOST'], port=connection_obj['PORT'])
        self.db_obj = self.conn[self.database]

        # self.conn["UPruf"].authenticate(connection_obj['USERNAME'], connection_obj['PASSWORD'],
        #                                 mechanism=connection_obj['MECHANISM'])
    def __del__(self):
        if self.conn is not None:
            self.conn.close()
def updates(userid,type1,ImageForgeFlag,IsProcessed,OCRStatus,num):
    # print("in updates")
    try:
        mongo_upruf = MongoConn({"HOST": "localhost", "PORT": 27017, "DATABASE": "ActualDB"})
        # userid = '5d76297e9f2bbb34585e628d'
        # print(userid)

        Pipeline = [

            {
                "$unwind": {
                    "path": "$Modules",
                    "preserveNullAndEmptyArrays": False
                }
            },

            {
                "$unwind": {
                    "path": "$Modules.SubModule",
                    "preserveNullAndEmptyArrays": False
                }
            },

            {
                "$unwind": {
                    "path": "$Modules.SubModule.Fields.AttachedFiles",
                    # "preserveNullAndEmptyArrays" : false // optional
                }
            },

            {
                "$match": {

                    "Modules.ModuleID":6,
                    "Modules.SubModule.Fields.AttachedFiles.DocType":type1
                }
            },

            {
                "$project": {
                    # // specifications
                    # "FileNumber":"$Modules.SubModule.Fields.AttachedFiles.FileNumber",
                    # "FileID": "$Modules.SubModule.Fields.AttachedFiles.FileID",
                    "Sr": "$Modules.SubModule.Sr",
                    "UserID": "$UserID"
                }
            },

        ]
        filter = mongo_upruf.db_obj['UserProfile'].aggregate(Pipeline)
        fi = (list(filter))
        sr = int(fi[0]['Sr'])
        UserID = filter[0]['UserID']
        # print("sr",sr)
        PipelineAllSr = [

            {
                "$unwind": {
                    "path": "$Modules",
                    "preserveNullAndEmptyArrays": False
                }
            },

            {
                "$unwind": {
                    "path": "$Modules.SubModule",
                    "preserveNullAndEmptyArrays": False
                }
            },

            {
                "$unwind": {
                    "path": "$Modules.SubModule.Fields.AttachedFiles",
                    # "preserveNullAndEmptyArrays" : false // optional
                }
            },

            {
                "$match": {
                    "Modules.ModuleID": 6,
                    "UserID": UserID

                }
            },

            {
                "$project": {
                    # // specifications
                    #

                    "Sr": "$Modules.SubModule.Sr",

                }
            }
        ]

        counts = 0
        filterallsr = mongo_upruf.db_obj['UserProfile'].aggregate(PipelineAllSr)
        fi = (list(filterallsr))
        for val in fi:
            if (val['Sr'] == sr):
                # print(counts)
                break
            else:
                counts = counts + 1
        print("vount",counts)

        filterupdtae = {"UserID": ObjectId(UserID), "Modules.ModuleID": 6}

        if type1 == 'Aadhar Card':
            adharnum = num.strip('\n')
            try:
                mongo_upruf.db_obj['UserProfile'].update_one(filterupdtae,
                                                                 {"$set": {
                                                                    "Modules.$.SubModule."+str(counts)+".Fields.AttachedFiles.0.IsProcessed":IsProcessed,
                                                                     "Modules.$.SubModule."+str(counts)+".Fields.AttachedFiles.0.ImageForgeStatus":ImageForgeFlag,
                                                                      "Modules.$.SubModule."+str(counts)+".Fields.AttachedFiles.0.OCRStatus":OCRStatus,
                                                                     "Modules.$.SubModule."+str(counts)+".Fields.AttachedFiles.0.ExtractedNum":adharnum

                                                                 }})
                # print("queryyy executeddd")
            except Exception as e:
                pass
                # print("mongo updtae", str(e))
        elif type1 == 'PAN Card':
            try:
                mongo_upruf.db_obj['UserProfile'].update_one(filterupdtae,
                                                             {"$set": {
                                                                 "Modules.$.SubModule." + str(
                                                                     counts) + ".Fields.AttachedFiles.0.IsProcessed": IsProcessed,
                                                                 "Modules.$.SubModule." + str(
                                                                     counts) + ".Fields.AttachedFiles.0.ImageForgeStatus": ImageForgeFlag,
                                                                 "Modules.$.SubModule." + str(
                                                                     counts) + ".Fields.AttachedFiles.0.OCRStatus": OCRStatus

                                                             }})
                # print("queryyy executeddd")
            except Exception as e:
                pass
                        # print("mongo updtae", str(e))
                # raise e
        elif type1 == 'Passport':
            mongo_upruf.db_obj['UserProfile'].update_one(filterupdtae,
                                                         {"$set": {
                                                             "Modules.$.SubModule." + str(
                                                                 counts) + ".Fields.AttachedFiles.0.IsProcessed": IsProcessed,
                                                             "Modules.$.SubModule." + str(
                                                                 counts) + ".Fields.AttachedFiles.0.ImageForgeStatus": ImageForgeFlag,
                                                             "Modules.$.SubModule." + str(
                                                                 counts) + ".Fields.AttachedFiles.0.OCRStatus": OCRStatus,
                                                             "Modules.$.SubModule." + str(
                                                                 counts) + ".Fields.AttachedFiles.0.ExtractedNum": num

                                                         }})

        return {"message": "updated successfully"}

    except Exception as e:
        print("e",str(e))
        raise e

# updates('5d76297e9f2bbb34585e628d', 'Aadhar Card', True,1, False)

