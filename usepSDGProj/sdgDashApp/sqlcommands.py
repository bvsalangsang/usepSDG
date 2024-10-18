
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
    