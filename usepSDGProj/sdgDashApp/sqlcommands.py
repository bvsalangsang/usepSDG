
"""
SQL Command for sdgDashboard.

List of CRUD functions for sdgDashboard 
"""

#SDG
def fetchSDG():
    sql = ("SELECT * from man_sdg WHERE isActive = 'Y'")
    return sql

def saveUpdateSDG(**sgdParams):

    sql = ( "INSERT INTO man_sdg " 
           " SET sdgId = '{0}', "
           " sdgName = '{1}', "
           " description = '{2}', "
           " isActive = '{3}' " 
           "ON DUPLICATE KEY UPDATE " 
           " sdgName = '{1}', "
           " description = '{2}', "
           " isActive = '{3}' " ).format(sgdParams['sdgId'],
                                         sgdParams['sdgName'],
                                         sgdParams['description'],
                                         sgdParams['isActive'])
    return sql 

def deleteSDG(**sgdParams):
    sql=("UPDATE man_sdg SET isActive = 'N' WHERE sdgId = '{0}'").format(sgdParams['sdgId'])
    return sql

#SDG Target 
def fetchSDGTarget():
    sql = ("""SELECT 
           target.targetId, 
           sdg.sdgId,
           sdg.sdgName,
           target.targetCode,
           target.targetDesc,
           target.isActive
           FROM man_sdg_target target 
           LEFT JOIN man_sdg sdg ON target.sdgId = sdg.sdgId
           WHERE target.isActive = 'Y'
           """)
    return sql

def saveUpdateSDGTarget(**sgdTargetParams):

    sql = ( "INSERT INTO man_sdg_target " 
           " SET targetId = '{0}', "
           " sdgId = '{1}', "
           " targetCode = '{2}', "
           " targetDesc = '{3}', "
           " isActive = '{4}' " 
           "ON DUPLICATE KEY UPDATE " 
            " sdgId = '{1}', "
           " targetCode = '{2}', "
           " targetDesc = '{3}', "
           " isActive = '{4}' " ).format(sgdTargetParams['targetId'],
                                         sgdTargetParams['sdgId'],
                                         sgdTargetParams['targetCode'],
                                         sgdTargetParams['targetDesc'],
                                         sgdTargetParams['isActive'])
    return sql 

def deleteSDGTarget(**sgdTargetParams):
    sql=("UPDATE man_sdg_target SET isActive = 'N' WHERE targetId = '{0}'").format(sgdTargetParams['targetId'])
    return sql

#SDG Indicator
def fetchSDGIndicator():
    sql = ("""SELECT 
           ind.indId, 
           target.targetDesc,
           ind.indCode,
           ind.indDesc,
           ind.isActive
           FROM man_sdg_indicator ind 
           LEFT JOIN man_sdg_target target ON ind.targetId = target.targetId
           WHERE ind.isActive = 'Y'
           """)
    return sql

def saveUpdateIndicatorTarget(**sgdIndicatorParams):

    sql = ( "INSERT INTO man_sdg_indicator " 
           " SET indId = '{0}', "
           " targetId = '{1}', "
           " indCode = '{2}', "
           " indDesc = '{3}', "
           " isActive = '{4}' " 
           "ON DUPLICATE KEY UPDATE " 
           " targetId = '{1}', "
           " indCode = '{2}', "
           " indDesc = '{3}', "
           " isActive = '{4}' " ).format(sgdIndicatorParams['indId'],
                                         sgdIndicatorParams['targetId'],
                                         sgdIndicatorParams['indCode'],
                                         sgdIndicatorParams['indDesc'],
                                         sgdIndicatorParams['isActive'])
    return sql 

def deleteIndicatorTarget(**sgdIndicatorParams):
    sql=("UPDATE man_sdg_indicator SET isActive = 'N' WHERE indId = '{0}'").format(sgdIndicatorParams['indId'])
    return sql

#SDG Parent Child
def sdgDetailsView():
    sql = ("""
            SELECT
            sdg.sdgId AS sdgId,
            sdg.sdgName AS sdgName, 
            sdg.description AS sdgDesc,
            sdg.isActive AS sdgIsActive,
            target.targetId AS targetId,
            target.sdgId AS tgtsdgId,
            target.targetCode AS targetCode,
            target.targetDesc AS targetDesc,
            target.isActive AS targetIsActive,
            ind.indId AS indId, 
            ind.targetId AS indTId, 
            ind.indCode AS indCode, 
            ind.indDesc AS indDesc,
            ind.isActive AS indIsActive
            FROM man_sdg sdg
            LEFT JOIN man_sdg_target target ON target.sdgId = sdg.sdgId
            LEFT JOIN man_sdg_indicator ind ON ind.targetId = target.targetId
            WHERE sdg.IsActive = 'Y'
          """);  

    return sql

#Sustainability Strategy
def fetchSusStrat():
    sql = ("SELECT * FROM man_sustian_strat WHERE isActive = 'Y'")
    return sql 

def saveUpdateSusStrat(**susStratParams):
    sql = ("""
            INSERT INTO man_sustian_strat
            set susStratId = '{0}',
            susStratName = '{1}',
            isActive = '{2}'
            ON DUPLICATE KEY UPDATE 
             susStratName = '{1}',
            isActive = '{2}'
        """).format(susStratParams['susStratId'],
                    susStratParams['susStratName'],
                    susStratParams['isActive'])
    
    return sql 

def deleteSusStrat(**susStratParams):
    sql = ("UPDATE man_sustian_strat set isActive = 'N' WHERE susStratId = '{0}'").format(susStratParams['susStratId'])
    return sql 
    
#UI green matric
def fetchUIGreen():
    sql = ("SELECT * FROM man_green_metric WHERE isActive = 'Y'")
    return sql 

def saveUpdateUIGreen(**uiGreenParams):
    sql = ("""
            INSERT INTO man_green_metric
            set greenMetId = '{0}',
            greenName = '{1}',
            isActive = '{2}'
            ON DUPLICATE KEY UPDATE 
            greenName = '{1}',
            isActive = '{2}'
        """).format(uiGreenParams['greenMetId'],
                    uiGreenParams['greenName'],
                    uiGreenParams['isActive'])
    
    return sql 

def deleteUIGreen(**uiGreenParams):
    sql = ("UPDATE man_green_metric set isActive = 'N' WHERE greenMetId = '{0}'").format(uiGreenParams['greenMetId'])
    return sql 
    
#SDG scorecard
def fetchSdgScorecard():
    sql =  ("""
                SELECT 
                sdg.sdgScoreId,
                sus.susStratName,
                green.greenName,
                sdg.sdgInitName,
                sdg.sdgImpYear,
                sdg.sdgDesc,
                sdg.outputs,
                sdg.outcome,
                sdg.personnel,
                sdg.links,
                sdg.enCodedBy,
                sdg.enCodedDate,
                sdg.isActive,
                GROUP_CONCAT(DISTINCT ms.sdgName) AS sdgName, 
                GROUP_CONCAT(DISTINCT mst.targetCode) AS targetCode,
                GROUP_CONCAT(DISTINCT mst.targetDesc) AS targetDesc,
                GROUP_CONCAT(DISTINCT msi.indCode) AS indCode,
                GROUP_CONCAT(DISTINCT msi.indDesc) AS indDesc
                FROM sdg_scorecard sdg
                LEFT JOIN man_sustian_strat sus ON sus.susStratId = sdg.susStratId
                LEFT JOIN  man_green_metric green ON green.greenMetId = sdg.greenMetId
                LEFT JOIN sdg_scorecard_det scd ON scd.sdgScoreId = sdg.sdgScoreId
                LEFT JOIN man_sdg ms ON FIND_IN_SET(ms.sdgId, scd.sdgId) > 0
                LEFT JOIN man_sdg_target mst ON FIND_IN_SET(mst.targetId, scd.targetId) > 0
                LEFT JOIN man_sdg_indicator msi ON FIND_IN_SET(msi.indId, scd.indId) > 0
                WHERE sdg.isActive = 'Y' 
                GROUP BY sdg.sdgScoreId;
            """)
    return sql

def fetchSdgScorecardDet():
    sql = ("""
            SELECT 
                sdg.sdgScoreId,
                scd.sdgScoreId, 
                GROUP_CONCAT(DISTINCT ms.sdgName) AS sdgName, 
                GROUP_CONCAT(DISTINCT mst.targetCode) AS targetCode,
                GROUP_CONCAT(DISTINCT mst.targetDesc) AS targetDesc,
                GROUP_CONCAT(DISTINCT msi.indCode) AS indCode,
                GROUP_CONCAT(DISTINCT msi.indDesc) AS indDesc
            FROM 
                sdg_scorecard_det scd
            LEFT JOIN  
                sdg_scorecard sdg ON sdg.sdgScoreId = scd.sdgScoreId
            LEFT JOIN 
                man_sdg ms ON FIND_IN_SET(ms.sdgId, scd.sdgId) > 0
            LEFT JOIN 
                man_sdg_target mst ON FIND_IN_SET(mst.targetId, scd.targetId) > 0
            LEFT JOIN 
                man_sdg_indicator msi ON FIND_IN_SET(msi.indId, scd.indId) > 0
            WHERE 
                sdg.isActive = 'Y' 
            GROUP BY 
                scd.sdgScoreId;
               
             """)

    sqlTemp = ("""
    SELECT 
    sdg.sdgScoreId,
    sus.susStratName,
    green.greenName,
    sdg.sdgInitName,
    sdg.sdgImpYear,
    sdg.sdgDesc,
    sdg.outputs,
    sdg.outcome,
    sdg.personnel,
    sdg.links,
    sdg.enCodedBy,
    sdg.enCodedDate,
    sdg.isActive,
    GROUP_CONCAT(DISTINCT ms.sdgName) AS sdgName, 
    GROUP_CONCAT(DISTINCT mst.targetCode) AS targetCode,
    GROUP_CONCAT(DISTINCT mst.targetDesc) AS targetDesc,
    GROUP_CONCAT(DISTINCT msi.indCode) AS indCode,
    GROUP_CONCAT(DISTINCT msi.indDesc) AS indDesc
    FROM sdg_scorecard sdg
    LEFT JOIN man_sustian_strat sus ON sus.susStratId = sdg.susStratId
    LEFT JOIN  man_green_metric green ON green.greenMetId = sdg.greenMetId
    LEFT JOIN sdg_scorecard_det scd ON scd.sdgScoreId = sdg.sdgScoreId
    LEFT JOIN man_sdg ms ON FIND_IN_SET(ms.sdgId, scd.sdgId) > 0
    LEFT JOIN man_sdg_target mst ON FIND_IN_SET(mst.targetId, scd.targetId) > 0
    LEFT JOIN man_sdg_indicator msi ON FIND_IN_SET(msi.indId, scd.indId) > 0
    WHERE sdg.isActive = 'Y'
    GROUP BY sdg.sdgScoreId;
    """)

    return sql

def saveUpdateSdgScorecard(**sdgScorecard):
    sql = ("""
           INSERT INTO sdg_scorecard 
           SET sdgScoreId = '{0}',
           susStratId = '{1}',
           greenMetId = '{2}',
           sdgInitName = '{3}',
           sdgImpYear = '{4}',
           sdgDesc = '{5}',
           outputs = '{6}',
           outcome = '{7}',
           personnel = '{8}',
           links = '{9}',
           enCodedBy = '{10}',
           enCodedDate = '{11}',
           isActive = '{12}'
           ON DUPLICATE KEY UPDATE 
           susStratId = '{1}',
           greenMetId = '{2}',
           sdgInitName = '{3}',
           sdgImpYear = '{4}',
           sdgDesc = '{5}',
           outputs = '{6}',
           outcome = '{7}',
           personnel = '{8}',
           links = '{9}',
           enCodedBy = '{10}',
           enCodedDate = '{11}',
           isActive = '{12}'
           """).format(sdgScorecard['sdgScoreId'],
                       sdgScorecard['susStratId'],
                       sdgScorecard['greenMetId'],
                       sdgScorecard['sdgInitName'],
                       sdgScorecard['sdgImpYear'],
                       sdgScorecard['sdgDesc'],
                       sdgScorecard['outputs'],
                       sdgScorecard['outcome'],
                       sdgScorecard['personnel'],
                       sdgScorecard['links'],
                       sdgScorecard['enCodedBy'],
                       sdgScorecard['enCodedDate'],
                       sdgScorecard['isActive'],)
    
    return sql
    
def saveUpdateSdgScorecarDet(**sdgScorecardDet):
    sql=("""
         INSERT INTO sdg_scorecard_det 
         SET sdgScoreId = '{0}',
         sdgId  = '{1}',
         targetId = '{2}',
         indId = '{3}',
         isActive = '{4}' 
         ON DUPLICATE KEY UPDATE 
         sdgId  = '{1}',
         targetId = '{2}',
         indId = '{3}',
         isActive = '{4}' 
         """).format(sdgScorecardDet['sdgScoreId'],
                     sdgScorecardDet['sdgId'],
                     sdgScorecardDet['targetId'],
                     sdgScorecardDet['indId'],
                     sdgScorecardDet['isActive'])

    return sql

def deleteScorecard(**sdgScorecard):
    sql = ("UPDATE sdg_scorecard set isActive = 'N' WHERE sdgScoreId = '{0}'").format(sdgScorecard['sdgScoreId'])
    return sql 

def deleteScorecardDet(**sdgScorecardDet):
    sql = ("UPDATE sdg_scorecard_det set isActive = 'N' WHERE sdgScoreId = '{0}'").format(sdgScorecardDet['sdgScoreId'])
    return sql 

def getTargetPerGoal(**sgdTargetParams):
    sql = ("""
           SELECT * FROM man_sdg_target WHERE sdgId = '{0}'
           """).format(sgdTargetParams['sdgId'])
    
    return sql 

def getIndPerTarget(**sgdIndicatorParams):
    sql = ("""
          SELECT * FROM `man_sdg_indicator` WHERE `targetId`  = '{0}'
           """).format(sgdIndicatorParams['targetId'])
    
    return sql 

#Vegetation Map
def fetchVegMap():
    sql = ("""SELECT 
           vegId,
           campus,
           campAreaSqm,
           campAreaHas,
           forestVegSqm,
           forestVegHas,
           forestVegPctTotArea,
           plantVegSqm,
           plantVegHas,
           plantVegPctTotArea,
           waterAbsSqm,
           waterAbsHas,
           waterAbsPctTotArea,
           isActive 
           FROM man_vegetation_map 
           WHERE isActive  = 'Y'
           """)
    return sql

def saveUpdateVegMap(**vegMap):
    sql = ("""
            INSERT INTO man_vegetation_map
            SET vegId = '{0}',
            campus = '{1}',
            campAreaSqm = '{2}',
            campAreaHas = '{3}',
            forestVegSqm = '{4}',
            forestVegHas = '{5}',
            forestVegPctTotArea = '{6}',
            plantVegSqm = '{7}',
            plantVegHas = '{8}',
            plantVegPctTotArea = '{9}',
            waterAbsSqm = '{10}',
            waterAbsHas = '{11}',
            waterAbsPctTotArea = '{12}',
            isActive = '{13}'  
            ON DUPLICATE KEY UPDATE 
            campus = '{1}',
            campAreaSqm = '{2}',
            campAreaHas = '{3}',
            forestVegSqm = '{4}',
            forestVegHas = '{5}',
            forestVegPctTotArea = '{6}',
            plantVegSqm = '{7}',
            plantVegHas = '{8}',
            plantVegPctTotArea = '{9}',
            waterAbsSqm = '{10}',
            waterAbsHas = '{11}',
            waterAbsPctTotArea = '{12}',
            isActive = '{13}'  
        """).format(vegMap['vegId'],
                    vegMap['campus'],
                    vegMap['campAreaSqm'],
                    vegMap['campAreaHas'],
                    vegMap['forestVegSqm'],
                    vegMap['forestVegHas'],
                    vegMap['forestVegPctTotArea'],
                    vegMap['plantVegSqm'],
                    vegMap['plantVegHas'],
                    vegMap['plantVegPctTotArea'],
                    vegMap['waterAbsSqm'],
                    vegMap['waterAbsHas'],
                    vegMap['waterAbsPctTotArea'],
                    vegMap['isActive'])


#sdg policy
def fetchSDGPolicy():
    sql = ("""
            SELECT 
            sdgPolId,
            title, 
            description,
            imgPath,
            linkPath,
            isActive 
            FROM man_sdg_policy
            WHERE isActive = 'Y'  
          """)
    return sql

def saveUpdateSdgPolicy(**sdgPolicy):
    sql = ("""
           INSERT INTO man_sdg_policy
           SET sdgPolId = '{0}',
           title = '{1}',
           description = '{2}',
           imgPath = '{3}',
           linkPath = '{4}',
           isActive = '{5}'
           ON DUPLICATE KEY UPDATE
           title = '{1}',
           description = '{2}',
           imgPath = '{3}',
           linkPath = '{4}',
           isActive = '{5}'
          """).format(sdgPolicy['sdgPolId'],
                      sdgPolicy['title'],
                      sdgPolicy['description'],
                      sdgPolicy['imgPath'],
                      sdgPolicy['linkPath'],
                      sdgPolicy['isActive'])
    return sql 