from helperJinja2 import renderTemplateWithJson
from helperJson import getJsonFromFile


def fetchEntitledServiceList(mainDataJsonFile, datacenterFile):
    resultServices = getJsonFromFile(mainDataJsonFile)
    resultDCs = getJsonFromFile(datacenterFile)
    btpservicelist = resultServices["services"]

    resultDCs = sorted(resultDCs, key=lambda d: (d['region'].lower()), reverse=False)

    thisResult = {"btpservicelist": btpservicelist, "datacenterslist": resultDCs}
    return thisResult
