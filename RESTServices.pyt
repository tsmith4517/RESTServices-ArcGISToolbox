# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "REST Services"
        self.alias = "REST Services"

        # List of tool classes associated with this toolbox
        self.tools = [Crawl,
                      AddCrawlReport,
                      GetSources]


class Crawl:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "REST Server Crawl"
        self.description = "Crawls an ArcGIS REST Server and returns a report of available services. Optional Saptial Query"

    def getParameterInfo(self):
        """Define the tool parameters."""
        server_path = arcpy.Parameter(
            displayName="REST Server Path",
            name="server_path",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        
        username = arcpy.Parameter(
            displayName="Username",
            name="username",
            datatype="GPString",
            parameterType="Optional",
            direction="Input",
            category="Authentication")
        
        password = arcpy.Parameter(
            displayName="Password",
            name="password",
            datatype="GPStringHidden",
            parameterType="Optional",
            direction="Input",
            category="Authentication")
        
        search_feature = arcpy.Parameter(
            displayName="Search Feature",
            name="search_feature",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        
        output_excel = arcpy.Parameter(
            displayName="Output Excel Path",
            name="output_excel",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        output_excel.filter.list = ['xlsx']

        params = [server_path, username, password, search_feature ,output_excel]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return

class AddCrawlReport:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Add Report to Map"
        self.description = "Adds the generated report from the ArcGIS REST Server Crawl to chosen Map"
        self.aprx = arcpy.mp.ArcGISProject("CURRENT")

    def getParameterInfo(self):
        """Define the tool parameters."""
        report_path = arcpy.Parameter(
            displayName="Crawl Report Path",
            name="report_path",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")
        report_path.filter.list = ['xlsx']

        map_document = arcpy.Parameter(
            displayName="Map Document",
            name="map_document",
            datatype="GPMap",
            parameterType="Required",
            direction="Input")
        


        

        params = [report_path, map_document]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return


class GetSources:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Get Web App Sources"
        self.description = "Input the Web App Item Id and retrieve the Maps and Layers used in the Web App"
        self.aprx = arcpy.mp.ArcGISProject("CURRENT")

    def getParameterInfo(self):
        """Define the tool parameters."""
        item_id = arcpy.Parameter(
            displayName="Web App Item Id",
            name="item_id",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        app_type = arcpy.Parameter(
            displayName="Web App Type",
            name="app_type",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        
        app_type.filter.type = "ValueList"
        app_type.filter.list = ["Story Map", 
                                "Experience Builder",
                                "Web App Builder",
                                "Instant App",
                                "Dashboard",
                                "Other"]
        
        output_excel = arcpy.Parameter(
            displayName="Output Excel Path",
            name="output_excel",
            datatype="DEFile",
            parameterType="Required",
            direction="Output")
        output_excel.filter.list = ['xlsx']

        

        params = [item_id, app_type, output_excel]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
