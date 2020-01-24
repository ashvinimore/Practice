__author__ = "Sunil Barve"
__copyright__ = ""
__credits__ = [""]
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = "Development"

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from bson import ObjectId
import pymongo
import pandas as pd
# import rintegration
from scripts.comm.config import SCRIPT_PATH

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

def createframe(fileid,userid):

    try:
        scriptpath = SCRIPT_PATH + 'scripts/'
        mongo_upruf = MongoConn({"HOST": "192.168.10.13", "PORT": 27017, "DATABASE": "ActualDB"})
        # userid = '5c80b8b1dfe3be7f2e4996ae'
        Pipeline =            [

                {
                    "$unwind": {
                        "path" : "$Modules",
                        "preserveNullAndEmptyArrays" : False
                    }
                },


                {
                    "$unwind": {
                        "path" : "$Modules.SubModule",
                        "preserveNullAndEmptyArrays" : False
                    }
                },


                {
                    "$unwind": {
                        "path" : "$Modules.SubModule.Fields.AttachedFiles",
                        #"preserveNullAndEmptyArrays" : false // optional
                    }
                },

                {
                    "$match": {

                    "Modules.SubModule.Fields.AttachedFiles.FileID":fileid,
                    }
                },


                {
                    "$project": {
                        # // specifications
                        # "FileNumber":"$Modules.SubModule.Fields.AttachedFiles.FileNumber",
                        "FileID":"$Modules.SubModule.Fields.AttachedFiles.FileID",
                        "Sr":"$Modules.SubModule.Sr",
                        "DocType":"$Modules.SubModule.Fields.AttachedFiles.DocType",
                        "AdharNumber":"$Modules.SubModule.Fields.Number",
                        "UserID":"$UserID"
                    }
                },

            ]
        filter = mongo_upruf.db_obj['UserProfile'].aggregate(Pipeline)
        # print (list(filter))




        pipeline_name = [
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
                    "path": "$Modules.SubModule.Fields",
                    # "preserveNullAndEmptyArrays" : false // optional
                }
            },

            {
                "$match": {
                    "UserID": userid,
                    "Modules.ModuleID":8,
                    "Modules.SubModule.Sr": 1


                }
            },

            {
                "$project": {
                    # // specifications
                   "Fields":"$Modules.SubModule.Fields",
                }
            },
        ]
        filtername = mongo_upruf.db_obj['UserProfile'].aggregate(pipeline_name)
        name = (list(filtername))
        namedict = (name[0]['Fields'])
        Parameters = list(namedict.keys())
        parameterspan = list(namedict.keys())
        Information = list(namedict.values())
        InformationPan = list(namedict.values())

        try:
            if Parameters.index("AttachedFiles"):
                ind = Parameters.index("AttachedFiles")
                # print(ind)
                Parameters.remove("AttachedFiles")
                parameterspan.remove("AttachedFiles")
                del InformationPan[9]
                # print(Parameters)
                del Information[9]
                # print(Information)
        except Exception as e:
            pass

        d = {"Parameters":Parameters,"Information":Information}
        dpan = {"Parameters":parameterspan,"Information":InformationPan}
        # print(d)
        df = pd.DataFrame(d)
        dfpan = pd.DataFrame(dpan)
        # print(dfpan)
        export_csvaadhar = df.to_csv(r'/home/bluecrest/Unipruf/Uni_backend/Offline/scripts/UserClass.csv', index=None,
                               header=True)
        export_csvpan = dfpan.to_csv(r'/home/bluecrest/Unipruf/Uni_backend/Offline/scripts/PanName.csv', index=None,
                                     header=True)
        # Don't forget to add '.csv' at the end of the path


        pipeline_address = [
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
                    "path": "$Modules.SubModule.Fields",
                    # "preserveNullAndEmptyArrays" : false // optional
                }
            },

            {
                "$match": {
                    "UserID":userid,
                    "Modules.ModuleID": 8,
                    "Modules.SubModule.Sr": 3

                }
            },

            {
                "$project": {
                    # // specifications
                    "Fields": "$Modules.SubModule.Fields"
                }
            },
        ]
        filteraddress = mongo_upruf.db_obj['UserProfile'].aggregate(pipeline_address)
        address = (list(filteraddress))
        # print(address)
        addressdict = (address[0]['Fields'])
        Parameters = list(addressdict.keys())
        Information = list(addressdict.values())
        d = {"Parameters": Parameters, "Information": Information}
        # print(d)
        df = pd.DataFrame(d)
        # print(df)
        export_csv = df.to_csv(r'/home/bluecrest/Unipruf/Uni_backend/Offline/scripts/address.csv', index=None,
                               header=True)  # Don't forget to add '.csv' at the end of the path
    except Exception as e:
#        print(str(e))5d70b9ea49375e50e147c0de
#         raise e
        pass

    return filter

# check()
