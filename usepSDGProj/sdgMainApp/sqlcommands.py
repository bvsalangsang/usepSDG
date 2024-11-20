#SDG Parent Child
def sdgDetailsViewPerId(**sgdParams):
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
            WHERE sdg.IsActive = 'Y' and sdg.sdgId ={0} 
          """).format(sgdParams['sdgId']);  

    return sql


def getGoalList(**sgdParams):
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
                WHERE sdg.isActive = 'Y' AND ms.sdgId = '{0}'
                GROUP BY sdg.sdgScoreId;
            """).format(sgdParams['sdgId'])
    return sql


def getSdgScorecard(**sdgScorecard):
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
                WHERE sdg.isActive = 'Y' AND sdg.sdgScoreId = '{0}'
                GROUP BY sdg.sdgScoreId;
            """).format(sdgScorecard['sdgScoreId'])
    return sql


