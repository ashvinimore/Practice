const WebSocket = require('ws');
const fs = require('fs');
const mongodb = require('mongodb');
var ObjectID = require('mongodb').ObjectID;
var mongo =  require('../models/model');
var getfields =require('../models/form');
var ObjectID = require('mongodb').ObjectID;

const uri = 'mongodb://localhost:27017';
const dbName = 'ActualDB';

const client = new mongodb.MongoClient(uri);
var i = 0;
var chunkdata = ''
const server = new WebSocket.Server({ port: 8089 });
  server.on('connection',  function(socket) {
    socket.on('message',  async function ( msg1) {     
      if (msg1){      
        var msg = JSON.parse(msg1)          
        if(msg.action == "UploadFile"){
            if (msg.Chunknum == 'First'){                 
                i = i+1;
                if (msg.FileName)
                    global. filename = (msg.FileName).toString();
                    global. ModuleID = msg.ModuleID;
                    global. TenantID = msg.TenantID;
                    global.RoleID = msg.RoleID;
                    global. doctype = msg.DocType;
                    global.sr = msg.Sr;
                    global.UserID = msg.UserID;
                    // global.userid = "5d43d6f7660f37728613b723"
                    global.FileType = ".pdf"
                    global.IsProcessed = '0';
                    chunkdata = chunkdata + msg.Chunks 
                socket.send(JSON.stringify({'Completed': "1"}))
            }
            else if (msg.Chunknum == 'Last'){                               
                var bitmap = new Buffer(chunkdata, 'base64');
                fs.writeFileSync(filename, bitmap);
                const uri = 'mongodb://localhost:27017';
                const dbName = 'ActualDB';
                const client = new mongodb.MongoClient(uri);
                var submodules={}                
            
            client.connect(function(error) {
            const db = client.db(dbName);
            var bucket = new mongodb.GridFSBucket(db); 
            fs.createReadStream(filename).
            pipe(bucket.openUploadStream(filename)).
            on('error', function(error) {
            assert.ifError(error);
            }).
            on('finish', async function() {                   
            var filenameid = await db.collection("fs.files").find({'filename':filename}).toArray();            
            //updated code here                    
            const token = UserID.replace("Bearer","")
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const buff = new Buffer.from(base64, 'base64');
            const payloadinit = buff.toString('ascii');
            const deoded_token = JSON.parse(payloadinit);                        
            var userid = deoded_token.userid.toString()
            var filters = {"ModuleID":ModuleID,"TenantID":TenantID,"RoleID":RoleID}
            let pagename = await new getfields().getpages(filters)                    
            Object.keys(pagename).forEach(async function(p){
                modulename = pagename[0].DisplayName                      
                if("SubModule" in pagename[p]){
                    for(var subm=0;subm<pagename[p].SubModule.length;subm++){                            
                    submodules[pagename[p].SubModule[subm].SubModuleID]=pagename[p].SubModule[subm].Name  
                }
                }
                
            });  

            if(ModuleID == 6){
              let dialcode = await mongo.actual.collection("Users").find({ "UserID": new ObjectID(userid) }, { fields: { "DialCode": 1 } }).toArray()
              let documents = await mongo.control.collection("CountryMaster").find({ "DialCode": dialcode[0].DialCode }, { fields: { "IDDocuments": 1 } }).toArray()


              var subdoc = {}
              for (var doc = 0; doc < documents[0].IDDocuments.length; doc++) {
                  subdoc[parseInt(documents[0].IDDocuments[doc].ID, 10)] = documents[0].IDDocuments[doc].Name
              }
              submodules = {}
              submodules = subdoc
            }
            
            

            var count = 0;               
            var submodid1 = await new getfields().getKeyByValue(submodules,sr);            
            var submodid = parseInt(submodid1,10);                               
            var userprofile = await db.collection("UserProfile").find({'UserID':new ObjectID(userid)},{fields:{"_id":0,"Modules":1}}).toArray();                                           
            Object.keys(userprofile[0].Modules).forEach(async function(p){
            if (userprofile[0].Modules[p].ModuleID == ModuleID){           
                   
                for(var subm=0;subm<userprofile[0].Modules[p].SubModule.length;subm++){                             
                    if (sr == "null" && ModuleID == 10 ){ 
                                       
                      submodid = userprofile[0].Modules[p].SubModule.length 
                      userprofile[0].Modules[p].SubModule[subm].Sr = userprofile[0].Modules[p].SubModule.length 
                    } 
                    else if(sr != "null" && ModuleID == 10 ){

                      submodid = sr;
                      userprofile[0].Modules[p].SubModule[subm].Sr = sr;
                    }  
                                     
                    if(userprofile[0].Modules[p].SubModule[subm].Sr == submodid){                       
                    var attachedfiles = ("submoduleid",userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles)                                
                    var flag = 0; 
                                  
                    //when attached files are empty

                    if(attachedfiles.length == 1 ){   
                        
                        value = {"DocType": doctype,"FileName":filename,"FileID":filenameid[0]._id,"FileType":FileType,"IsProcessed":IsProcessed,"Status":null,"Result":null}                                         
                        var fil = {"UserID": new ObjectID(userid),"TenantID":TenantID,Modules:{$elemMatch:{"ModuleID":ModuleID,"SubModule.Sr":submodid}}} 
                        
                        try {
                                                            
                            // await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$.SubModule":userprofile[0].Modules[0].SubModule}},{"fields":{"Modules.$":1}}); 
                           
                            await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$[i].SubModule.$[j].Fields.AttachedFiles.$[k]":value}},{arrayFilters:[{"i.ModuleID":ModuleID},{"j.Sr":submodid},{"k.DocType":doctype}]}); 
                            // await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$[i].SubModule.$[j].Fields.AttachedFiles": 2}},{"arrayFilters": [{"i":0}, {"j":0}]});
                            let a = await db.collection("UserProfile").find(fil).toArray();   
                                    

                        }
                        catch(e){
                       
                        }
                    }     
                        
                    //when attached file contain atleast one document
                    else{
                      
                    // Object.keys(userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles).forEach(async function(q){
                        //when doctype is not same            
                        for(var q in  Object.keys(userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles)){                          
                          if (userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles[q].DocType != doctype )
                              flag = 1;
                          else{
                              flag = 2;
                              break;
                          }                        
                        }         
                        if(flag == 2){
                        count = count + 1
                        a = parseInt(q,10)                       
                        
                        var iddelete = {"_id":new ObjectID(userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles[a].FileID)}
                        try{
                            await db.collection("fs.files").deleteOne(iddelete);
                        }
                        catch(e){
                            // console.log(e)
                        }       
                                                                  
                        userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles[a] = {"DocType": doctype,"FileName":filename,"FileID":filenameid[0]._id,"FileType":FileType,"IsProcessed":IsProcessed,"Status":null,"Result":null}
                        
                        value = {"DocType": doctype,"FileName":filename,"FileID":filenameid[0]._id,"FileType":FileType,"IsProcessed":IsProcessed,"Status":null,"Result":null}
                                                    
                        var fil = {"UserID": new ObjectID(userid),"TenantID":TenantID,Modules:{$elemMatch:{"ModuleID":ModuleID,"SubModule.Sr":submodid}}} 
                        
                        try {
                                                            
                            // await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$.SubModule":userprofile[0].Modules[0].SubModule}},{"fields":{"Modules.$":1}}); 
                           
                            await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$[i].SubModule.$[j].Fields.AttachedFiles.$[k]":value}},{arrayFilters:[{"i.ModuleID":ModuleID},{"j.Sr":submodid},{"k.DocType":doctype}]}); 
                            // await db.collection("UserProfile").updateOne(fil,{"$set": {"Modules.$[i].SubModule.$[j].Fields.AttachedFiles": 2}},{"arrayFilters": [{"i":0}, {"j":0}]});
                            let a = await db.collection("UserProfile").find(fil).toArray();   
                                    

                        }
                        catch(e){
                            // console.log(e)
                        }
                        }        
                        
                        if(flag == 1){                               
                        // userprofile[0].Modules[p].SubModule[subm].Fields.FirstName = "ashini else"
                        userprofile[0].Modules[p].SubModule[subm].Fields.AttachedFiles.push({"DocType": doctype,"FileName":filename,"FileID":filenameid[0]._id,"FileType":".pdf","IsProcessed":"0","Status":null,"Result":null})
                        var fil = {"UserID": new ObjectID(userid),"TenantID":TenantID,Modules:{$elemMatch:{"ModuleID":ModuleID,"SubModule.Sr":submodid}}} 
                        try {                                                                   
                            await db.collection("UserProfile").updateOne(fil,{"$push": {"Modules.$.SubModule":userprofile[0].Modules[0].SubModule}},{"fields":{"Modules.$":1}});                                                                 
                                

                        }
                        catch(e){
                            // console.log(e)
                        }                              
                        }                        
                    
                    }  
                }                    
            } 
            }
            });
            
            
            flteruserid = [];
            socket.send(JSON.stringify({'Completed': "Last","FileID":filenameid[0]._id,"Sr":msg.Sr}))                   
            });
            }); 
            chunkdata = "" 
            
        }
        else{
            i = i+1;
            chunkdata = chunkdata + msg.Chunks 
            socket.send(JSON.stringify({'Completed': i.toString()}))
        } 
          }      
    
          if (msg.action == 'GetData' && msg.Chunknum == "Start"){
            var fileid = msg.FileID.toString() ; 
            var file = msg.FileName          
            client.connect( async function() {          
              //   debugger
                const db = client.db(dbName);                   
                    let id = await db.collection("fs.files").find({'filename':file}).toArray();
                    var name = id[0].filename                   
                      const bucket =   new mongodb.GridFSBucket(db, {
                        chunkSizeBytes: 1024, 
                        });       
                        bucket.openDownloadStreamByName(file).pipe(fs.createWriteStream(name));    
                        socket.send(JSON.stringify({"Completed":"Downloaded!","FileName":name}))                                
                                                   
                  });
              }
        
          if (msg.action == 'GetData' && msg.Chunknum != "Start"){//   debugger
            setTimeout(() => {   
              // console.log(msg.FileName);
                var filename = (msg.FileName).toString();
                var imagedata =  base64_encode(filename);            
                var chunks =   createChunks(imagedata) ;  
                if (chunks.length > 0 || typeof(chunks) == "object")  { 
                  //           
                      if(chunks.length == 1 && msg.Chunknum == 'First'){
                        socket.send(JSON.stringify({'Completed':"Last","TotalChunks" : chunks.length,filedata:chunks[0]})) 
                        chunks = " " ;
                        i = 0; 
                        fs.unlinkSync(msg.FileName);     
                      }
                      else if (chunks.length > 1 && msg.Chunknum == 'First'){ 
                        i = 0
                        // console.log(JSON.stringify({'Completed':i.toString(),"TotalChunks" : chunks.length}))              
                        socket.send(JSON.stringify({'Completed':i.toString(),"TotalChunks" : chunks.length,filedata:chunks[0]}))
                        i = i+1  
                      
                      }
                      else if ( msg.Chunknum == 'Next' && (chunks.length-1) == i){               
                        socket.send(JSON.stringify({'Completed':'Last',"TotalChunks" : chunks.length,filedata:chunks[i]}))
                        chunks = " ";                       
                        i = 0 ;
                        fs.unlinkSync(msg.FileName);     
                       
                       
                      }
                      else if (chunks.length > 1 && msg.Chunknum == 'Next'){    
                                               
                        socket.send(JSON.stringify({'Completed':i.toString(),"TotalChunks" : chunks.length,filedata:chunks[i]}))
                        i = i+1;
                        // chunks.shift();
                      }
                    
                }
                
                }, 1000);
                   
             }          
          
              
                   
            }
                 
       
          
  });
        
});   
    // }



   function createChunks(imageData) {
    const chunkSize = 1024 * 512;
    const chunks = [];
   
    while (imageData) {    
      if (imageData.length < chunkSize) {
       
        chunks.push(imageData);
        break;
      } else {
      
        chunks.push(imageData.substr(0, chunkSize));
       
        imageData = imageData.substr(chunkSize);
      }
    } 
    return chunks
  }  
  
   function base64_encode(file) {    
    let path2 = process.cwd();
  
    var path = require('path');
    var x = path.join(path2, file);
   
    var bitmap = fs.readFileSync(x);
    // convert binary data to base64 encoded string
    return new Buffer(bitmap).toString('base64');
  }



  




  

