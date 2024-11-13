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

