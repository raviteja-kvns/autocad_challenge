# Approach:
> I have taken a surrogate approach. i.e. since drawing files like .dwg and revit files like .rvt are proprietary, I did not find robust python libraries to deal with them.
> So instead I looked at open source versions similar to them and built it and then used some convertors to convert into the Autodesk formats.

I am not completely satisfied by the above approach as we will be limited at each step of the process. But it gets the job done and I had to settle with it for the time being. So, if I need to go to production, I would take a different route. I will use Autodesk Forge which provides the cloud API @ https://forge.autodesk.com/blog/design-automation-api-revit-inventor-3ds-max-now-available.
It is a cloud based API to directly create, edit and write Autodesk Inventor and Revit files. I haven't taken that route as there seems to be a lot of overhead to get started. 

# Progress Made
* Task 1: Converting to drawing files formats .dwg and .dxf - Compeleted. It is done using ezdxf package and ODAFileConvertor. The results are available under results folder

* Task 2: Converting to revit files .rvt etc - Incomplete. Since revit is proprietary format, it was difficult to find python packages to get the task done. So I tried approaching surrogate approach and tried to build IFC format, an open source one and then convert it to revit. One software by ODA can do this conversion - https://www.opendesign.com/blog/2019/july/oda-releases-bimrv-sdk-2020. 
However, I was running into issues as it was only available for windows and I couldn't find a windows machine that works for this install  

# Environment Setup
* Install pip package ezdxf @ https://pypi.org/project/ezdxf/
* If using mac, the library ezdxf probably throws error. To avoid error, set the exec_path = "/Applications/ODAFileConverter.app" and temp_path = "/tmp"
* Install ODAFileConverter - shttps://www.opendesign.com/guestfiles/oda_file_converter

# Running the code
* python main.py -f './data/csv/sample_blueprint.csv' -cs autocad -cf dxf

# Project Structure: 
* Converters: Has all the file converters from csv to other formats, eg. AutoCADConverter and RevitConverter
* utils: Contans commonly used stateless functions
* config.py: Configurations like invocation flags to libraries, paths of results, data etc. are set up here. A common place from which the whole app reads and implements accordingly
* main.py: parses the input arguments, loads input file and invokes appropriate file converter and saves the result 
 data: Home to input data. 
* results: Results will be placed in it

# Libraries Considered
Following are the libraries considered for AutoCAD drawings .dxf, .dwg:
* SDXF 1.1 - Not going ahead as it is from 2005 and no recent release history exists
* dxfwrite - Official documents say it is old and suggested a new one : ezdxf  
* ezdxf - Probably a good one. Has recent release history, and active work is being done. But the version number is < 1. So wouldn't prefer it for production unless absolutely necessary
* dxf_fix - seems like built on top of ezdxf 
* dxf - Again, an old one
* Fiona - looks promising but not specialized towards Autocad

Following are the libraries considered for Revit Files - 
* rjm 1.4.0 - Need dynamo
* https://primer.dynamobim.org/10_Custom-Nodes/10-5_Python-Revit.html - Not standalone
* pyrevit -  Not standalone. 
> None of the above revit libraries are up for the task