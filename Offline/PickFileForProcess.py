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
import rintegration

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

        # self.conn["UPruf"].authenticate(mechanism=connection_obj['MECHANISM'])
    def __del__(self):
        if self.conn is not None:
            self.conn.close()

def checkcron():

    try:
        mongo_upruf = MongoConn({"HOST": "localhost", "PORT": 27017, "DATABASE": "ActualDB"})
        # userid = '5c80b8b1dfe3be7f2e4996ae'
        #
        # filter = list( mongo_upruf.db_obj['UserProfile'].find({"Modules.SubModule.Fields.AttachedFiles.IsProcessed":"0","Modules.ModuleID":6,},{"UserID":1}))
        # print("filter",filter)
        PipelineExistingFile = [

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
                    # "Modules.SubModule.Sr": 1,
                    "Modules.SubModule.Fields.AttachedFiles.FileID": {
                        "$ne": None
                    },
                    "Modules.SubModule.Fields.AttachedFiles.IsProcessed": "10",
                    # "Modules.SubModule.Fields.AttachedFiles.DocType": "Aadhar Card",


                }
            },

            {
                "$project": {
                    # // specifications
                    # "FileNumber":"$Modules.SubModule.Fields.AttachedFiles.FileNumber",
                    "FileID": "$Modules.SubModule.Fields.AttachedFiles.FileID",
                    "Sr": "$Modules.SubModule.Sr",
                    "DocType": "$Modules.SubModule.Fields.AttachedFiles.DocType",
                    "AdharNumber": "$Modules.SubModule.Fields.Number",
                    "UserID": "$UserID",
                    "Modules": "$Modules.ModuleID",
                }
            },

        ]
        filters = mongo_upruf.db_obj['UserProfile'].aggregate(PipelineExistingFile)
        filter = (list(filters))

        if  (filter) != []:
            print("not in filter")
            pass
        # else:
        #     print("in filter")
        else:
            # for val in filter:
        #     #     userid = (val['UserID'])
        #     #     break
        #
            PipelinePickingFile = [

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
                        # "Modules.SubModule.Sr": 1,
                        "Modules.SubModule.Fields.AttachedFiles.FileID" : {
                                                                            "$ne": None
                                                                            },
                        "Modules.SubModule.Fields.AttachedFiles.IsProcessed": "0",
                        # "Modules.SubModule.Fields.AttachedFiles.DocType": "Aadhar Card",


                    }
                },

                {
                    "$project": {
                        # // specifications
                        # "FileNumber":"$Modules.SubModule.Fields.AttachedFiles.FileNumber",
                        "FileID": "$Modules.SubModule.Fields.AttachedFiles.FileID",
                        "Sr": "$Modules.SubModule.Sr",
                        "DocType": "$Modules.SubModule.Fields.AttachedFiles.DocType",
                        "AdharNumber": "$Modules.SubModule.Fields.Number",
                        "UserID": "$UserID",
                        "Modules":"$Modules.ModuleID",
                    }
                },

            ]
            filterfileid = mongo_upruf.db_obj['UserProfile'].aggregate(PipelinePickingFile)
            filterdata =  (list(filterfileid))
            # print(filterdata)
            fileid = filterdata[0]['FileID']
            doctype =filterdata[0]['DocType']
            UserID = filterdata[0]['UserID']
            sr = int(filterdata[0]['Sr'])

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
                                "Modules.ModuleID":6,
                                "UserID":UserID


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
            filterallsr =  mongo_upruf.db_obj['UserProfile'].aggregate(PipelineAllSr)
            fi = (list(filterallsr))
            for val in fi:
                if(val['Sr'] == sr):
                    # print(counts)
                    break
                else:
                    counts = counts + 1


            filterupdtae = {"UserID":ObjectId(UserID),"Modules.ModuleID":6}
            try:
                # print("sr",sr)
                # print("sr",sr)
                mongo_upruf.db_obj['UserProfile'].update_one(filterupdtae,
                                                             {"$set": {
                                                                 "Modules.$.SubModule." + str(
                                                                     counts) + ".Fields.AttachedFiles.0.IsProcessed": '10'

                                                             }})
            except Exception as e:
                # print(e)
                rintegration.verification(fileid = fileid,doctype =doctype,UserID = UserID )
            # return (fileid,doctype,UserID)

    except Exception as e:
        print(str(e))
        pass
    # raise e












checkcron()
