import mysql.connector
import pandas as pd
import sqlalchemy


def starshema():
    engine = sqlalchemy.create_engine('mysql://root:Bluecrest@192.168.10.13/DWHDB')
    df = pd.read_sql_table('DWStarSchema', engine)

    try:
        #
        frame = df.to_sql('DWStarSchemaMultipleCompany', engine, if_exists='append',index=False);

        #
    except ValueError as vx:

        print(vx)

    except Exception as ex:

      print(ex)



def ID():
    try:
        connection = mysql.connector.connect(host='192.168.10.13',
                                             database='DWHDB',
                                             user='root',
                                             password='Bluecrest')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL database... MySQL Server version on ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Your connected to - ", record)

            dwcoid = "select distinct DWCoID from DWDerivedCompany where DWCoID > 5001 and DWCOID not in (9,11569,3545,6918,9020) limit 1000"
            cursor.execute(dwcoid)
            res = cursor.fetchall()

            count = 0
            for coid in res:
                count = count + 1
                mul = count * 0.5
                print(coid[0])
                try:
                    insertmultiple = "INSERT INTO DWEleIDSchemaNewMultipleCompany\
(`PeriodID`,`ReportedDateID`,`DWCoID`,`ID1`,`ID2`,`ID3`,`ID4`,`ID5`,`ID6`,`ID7`,`ID8`,`ID9`,`ID10`,\
`ID11`,`ID12`,`ID13`,`ID14`,`ID15`,`ID16`,`ID17`,`ID18`,`ID19`,`ID20`,`ID21`,`ID22`,`ID23`,`ID24`,\
`ID25`,`ID26`,`ID27`,`ID28`,`ID29`,`ID30`,`ID31`,`ID32`,`ID33`,`ID34`,`ID35`,`ID36`,`ID37`,`ID38`,\
`ID39`,`ID40`,`ID41`,`ID42`,`ID43`,`ID44`,`ID45`,`ID46`,`ID47`,`ID48`,`ID49`,`ID50`,`ID51`,`ID52`,`ID53`,`ID54`,`ID55`,`ID56`,`ID57`,\
`ID58`,`ID59`,`ID60`,`ID61`,`ID62`,`ID63`,`ID64`,`ID65`,`ID66`,`ID67`,`ID68`,`ID69`,`ID70`,`ID71`,`ID72`,\
`ID73`,`ID74`,`ID75`,`ID76`,`ID77`,`ID78`,`ID79`,`ID80`,`ID81`,`ID82`,`ID83`,`ID84`,`ID85`,`ID86`,`ID87`,\
`ID88`,`ID89`,`ID90`,`ID91`,`ID92`,`ID93`,`ID94`,`ID95`,`ID96`,`ID97`,`ID98`,`ID99`,`ID100`,`ID101`,\
`ID102`,`ID103`,`ID104`,`ID105`,`ID106`,`ID107`,`ID108`,`ID109`,`ID110`,`ID111`,`ID112`,`ID113`,`ID114`,\
`ID115`,`ID116`,`ID117`,`ID118`,`ID119`,`ID120`,`ID121`,`ID122`,`ID123`,`ID124`,`ID125`,`ID126`,\
`ID127`,`ID128`,`ID129`,`ID130`,`ID131`,`ID132`,`ID133`,`ID134`,`ID135`,`ID136`,`ID137`,`ID138`,`ID139`,`ID140`,`ID141`,\
`ID142`,`ID143`,`ID144`,`ID145`,`ID146`,`ID147`,`ID148`,`ID149`,`ID150`,`ID151`,`ID152`,`ID153`,`ID154`,\
`ID155`,`ID156`,`ID157`,`ID158`,`ID159`,`ID160`,`ID161`,`ID162`,`ID163`,`ID164`,`ID165`,`ID166`,`ID167`,`ID168`,\
`ID169`,`ID170`,`ID171`,`ID172`,`ID173`,`ID174`,`ID175`,`ID176`,`ID177`,`ID178`,`ID179`,`ID180`,`ID181`,`ID182`,\
`ID183`,`ID184`,`ID185`,`ID186`,`ID187`,`ID189`,`ID190`,`ID191`,`ID192`,`ID193`,`ID194`,`ID195`,`ID196`,\
`ID197`,`ID198`,`ID199`,`ID200`,`ID201`,`ID202`,`ID203`,`ID204`,`ID205`,`ID206`,`ID207`,`ID208`,`ID209`,`ID210`,\
`ID211`,`ID212`,`ID213`,`ID214`,`ID215`,`ID216`,`ID217`,`ID218`,`ID219`,`ID220`,`ID221`,`ID222`,`ID223`,`ID224`,\
`ID225`,`ID226`,`ID228`,`ID229`,`ID230`,`ID231`,`ID232`,`ID233`,`ID234`,`ID235`,`ID236`,`ID237`,`ID238`,\
`ID239`,`ID240`,`ID241`,`ID242`,`ID243`,`ID244`,`ID245`,`ID246`,`ID247`,`ID248`,`ID249`,`ID250`,`ID251`,\
`ID252`,`ID253`,`ID254`,`ID255`,`ID256`,`ID257`,`ID258`,`ID259`,`ID260`,`ID261`,`ID262`,\
`ID263`,`ID264`,`ID265`,`ID266`,`ID267`,`ID268`,`ID269`,`ID270`,`ID271`,`ID272`,`ID273`,`ID274`,\
`ID275`,`ID276`,`ID277`,`ID278`,`ID279`,`ID280`,`ID281`,`ID282`,`ID283`,`ID284`,`ID285`,\
`ID286`,`ID287`,`ID288`,`ID289`,`ID290`,`ID291`,`ID292`,`ID293`,`ID294`,`ID295`,`ID296`,`ID297`,`ID298`,`ID299`,`ID300`,`ID301`,`ID302`,`ID303`,`ID304`,\
`ID305`,`ID306`,`ID307`,`ID308`,`ID309`,`ID310`,`ID311`,`ID312`,`ID313`,`ID314`,`ID315`,`ID316`,`ID317`,`ID318`,`ID319`,`ID320`,\
`ID321`,`ID322`,`ID323`,`ID324`,`ID325`,`ID326`,`ID327`,`ID328`,`ID329`,`ID330`,`ID331`,`ID332`,`ID333`,\
`ID334`,`ID335`,`ID336`,`ID337`,`ID338`,`ID339`,`ID340`,`ID341`,`ID342`,`ID343`,`ID344`,`ID345`,`ID346`,`ID347`,\
`ID348`,`ID349`,`ID350`,`ID351`,`ID352`,`ID353`,`ID354`,`ID355`,`ID356`,`ID357`,`ID358`,`ID359`,`ID360`,`ID361`) select\
                `PeriodID`,`ReportedDateID`,'%s',`ID1`* %s,`ID2`* %s,`ID3`* %s,`ID4`* %s,`ID5`* %s,`ID6`* %s,`ID7`* %s,`ID8`* %s,`ID9`* %s,`ID10`* %s, \
                `ID11`* %s,`ID12`* %s,`ID13`* %s,`ID14`* %s,`ID15`* %s,`ID16`* %s,`ID17`* %s,`ID18`* %s,`ID19`* %s,`ID20`* %s,`ID21`* %s,`ID22`* %s,`ID23`* %s,`ID24`* %s, \
                `ID25`* %s,`ID26`* %s,`ID27`* %s,`ID28`* %s,`ID29`* %s,`ID30`* %s,`ID31`* %s,`ID32`* %s,`ID33`* %s,`ID34`* %s,`ID35`* %s,`ID36`* %s,`ID37`* %s,`ID38`* %s, \
                `ID39`* %s,`ID40`* %s,`ID41`* %s,`ID42`* %s,`ID43`* %s,`ID44`* %s,`ID45`* %s,`ID46`* %s,`ID47`* %s,`ID48`* %s,`ID49`* %s,`ID50`* %s,`ID51`* %s,`ID52`* %s,`ID53`* %s,`ID54`* %s,`ID55`* %s,`ID56`* %s,`ID57`* %s, \
                `ID58`* %s,`ID59`* %s,`ID60`* %s,`ID61`* %s,`ID62`* %s,`ID63`* %s,`ID64`* %s,`ID65`* %s,`ID66`* %s,`ID67`* %s,`ID68`* %s,`ID69`* %s,`ID70`* %s,`ID71`* %s,`ID72`* %s, \
                `ID73`* %s,`ID74`* %s,`ID75`* %s,`ID76`* %s,`ID77`* %s,`ID78`* %s,`ID79`* %s,`ID80`* %s,`ID81`* %s,`ID82`* %s,`ID83`* %s,`ID84`* %s,`ID85`* %s,`ID86`* %s,`ID87`* %s, \
                `ID88`* %s,`ID89`* %s,`ID90`* %s,`ID91`* %s,`ID92`* %s,`ID93`* %s,`ID94`* %s,`ID95`* %s,`ID96`* %s,`ID97`* %s,`ID98`* %s,`ID99`* %s,`ID100`* %s,`ID101`* %s, \
                `ID102`* %s,`ID103`* %s,`ID104`* %s,`ID105`* %s,`ID106`* %s,`ID107`* %s,`ID108`* %s,`ID109`* %s,`ID110`* %s,`ID111` * %s* %s,`ID112`* %s,`ID113`* %s,`ID114`* %s, \
                `ID115`* %s* %s,`ID116`* %s,`ID117`* %s,`ID118`* %s,`ID119`* %s,`ID120`* %s,`ID121`* %s,`ID122`* %s,`ID123`* %s,`ID124`* %s,`ID125`* %s,`ID126`* %s, \
                `ID127`* %s,`ID128`* %s,`ID129`* %s,`ID130`* %s,`ID131`* %s,`ID132`* %s,`ID133`* %s,`ID134`* %s,`ID135`* %s,`ID136`* %s,`ID137`* %s,`ID138`* %s,`ID139`* %s,`ID140`* %s,`ID141`* %s, \
                `ID142`* %s,`ID143`* %s,`ID144`* %s,`ID145`* %s,`ID146`* %s,`ID147`* %s,`ID148`* %s,`ID149`* %s,`ID150`* %s,`ID151`* %s,`ID152`* %s,`ID153`* %s,`ID154`* %s, \
                `ID155`* %s,`ID156`* %s,`ID157`* %s,`ID158`* %s,`ID159`* %s,`ID160`* %s,`ID161`* %s,`ID162`* %s,`ID163`* %s,`ID164`* %s,`ID165`* %s,`ID166`* %s,`ID167`* %s,`ID168`* %s, \
                `ID169`* %s,`ID170`* %s,`ID171`* %s,`ID172`* %s,`ID173`* %s,`ID174`* %s,`ID175`* %s,`ID176`* %s,`ID177`* %s,`ID178`* %s,`ID179`* %s,`ID180`* %s,`ID181`* %s,`ID182`* %s, \
                `ID183`* %s,`ID184`* %s,`ID185`* %s,`ID186`* %s,`ID187`* %s,`ID189`* %s,`ID190`* %s,`ID191`* %s,`ID192`* %s,`ID193`* %s,`ID194`* %s,`ID195`* %s,`ID196`* %s, \
                `ID197`* %s,`ID198`* %s,`ID199`* %s,`ID200`* %s,`ID201`* %s,`ID202`* %s,`ID203`* %s,`ID204`* %s,`ID205`* %s,`ID206`* %s,`ID207`* %s,`ID208`* %s,`ID209`* %s,`ID210`* %s, \
                `ID211`* %s,`ID212`* %s,`ID213`* %s,`ID214`* %s,`ID215`* %s,`ID216`* %s,`ID217`* %s,`ID218`* %s,`ID219`* %s,`ID220`* %s,`ID221`* %s,`ID222`* %s,`ID223`* %s,`ID224`* %s, \
                `ID225`* %s,`ID226`* %s,`ID228`* %s,`ID229`* %s,`ID230`* %s,`ID231`* %s,`ID232`* %s,`ID233`* %s,`ID234`* %s,`ID235`* %s,`ID236`* %s,`ID237`* %s,`ID238`* %s, \
                `ID239`* %s,`ID240`* %s,`ID241`* %s,`ID242`* %s,`ID243`* %s,`ID244`* %s,`ID245`* %s,`ID246`* %s,`ID247`* %s,`ID248`* %s,`ID249`* %s,`ID250`* %s,`ID251`* %s, \
                `ID252`* %s,`ID253`* %s,`ID254`* %s,`ID255`* %s,`ID256`* %s,`ID257`* %s,`ID258`* %s,`ID259`* %s,`ID260`* %s,`ID261`* %s,`ID262`* %s, \
                `ID263`* %s,`ID264`* %s,`ID265`* %s,`ID266`* %s,`ID267`* %s,`ID268`* %s,`ID269`* %s,`ID270`* %s,`ID271`* %s,`ID272`* %s,`ID273`* %s,`ID274`* %s, \
                `ID275`* %s,`ID276`* %s,`ID277`* %s,`ID278`* %s,`ID279`* %s,`ID280`* %s,`ID281`* %s,`ID282`* %s,`ID283`* %s,`ID284`* %s,`ID285`* %s, \
                `ID286`* %s,`ID287`* %s,`ID288`* %s,`ID289`* %s,`ID290`* %s,`ID291`* %s,`ID292`* %s,`ID293`* %s,`ID294`* %s,`ID295`* %s,`ID296`* %s,`ID297`* %s,`ID298`* %s,`ID299`* %s,`ID300`* %s,`ID301`* %s,`ID302`* %s,`ID303`* %s,`ID304`* %s, \
                `ID305`* %s,`ID306`* %s,`ID307`* %s,`ID308`* %s,`ID309`* %s,`ID310`* %s,`ID311`* %s,`ID312`* %s,`ID313`* %s,`ID314`* %s,`ID315`* %s,`ID316`* %s,`ID317`* %s,`ID318`* %s,`ID319` * %s* %s,`ID320`* %s, \
                `ID321`* %s,`ID322`* %s,`ID323`* %s,`ID324`* %s,`ID325`* %s,`ID326`* %s,`ID327`* %s,`ID328`* %s,`ID329`* %s,`ID330`* %s,`ID331`* %s,`ID332`* %s,`ID333`* %s, \
                `ID334`* %s,`ID335`* %s,`ID336`* %s,`ID337`* %s,`ID338`* %s,`ID339`* %s,`ID340`* %s,`ID341`* %s,`ID342`* %s,`ID343`* %s,`ID344`* %s,`ID345`* %s,`ID346`* %s,`ID347`* %s, \
                `ID348`* %s,`ID349`* %s,`ID350`* %s,`ID351`* %s,`ID352`* %s,`ID353`* %s,`ID354`* %s,`ID355`* %s,`ID356`* %s,`ID357`* %s,`ID358`* %s,`ID359`* %s,`ID360`* %s,`ID361` * %s from  DWEleIDSchemaNew where DWCoID = 6918"%(str(coid[0]),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),
                                    str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul),str(mul))






                    cursor.execute(insertmultiple)
                    connection.commit()
                    print("execute")
                    # break
                except Exception as e:
                    print("Error while connecting to MySQL", e)
    except Exception as e:
        print("Error while connecting to MySQL", e)

    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# starshema()
ID()

