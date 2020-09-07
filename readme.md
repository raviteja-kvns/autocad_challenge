Following are the libraries considered for AutoCAD drawings .dxf, .dwg:
> SDXF 1.1 - Not going ahead as it is from 2005 and no recent release history exists
> dxfwrite - Official documents say it is old and suggested a new one : ezdxf  
> ezdxf - Probably a good one. Has recent release history, and active work is being done. 
>         But the version number is < 1. So wouldn't prefer it for production unless absolutely necessary
> dxf_fix - seems like built on top of ezdxf 
> dxf - Again, an old one
> Fiona - looks promising but not specialized towards Autocad

Finally selected ezdxf - 
> Documentation Reference: https://ezdxf.mozman.at/docs/addons/odafc.html
Other references :
> https://paulcrickard.wordpress.com/2012/10/29/shapefiles-to-revit-or-autocad-using-python-to-write-dxf/

Revit Files - 
> rjm 1.4.0 - 
>https://primer.dynamobim.org/10_Custom-Nodes/10-5_Python-Revit.html
> pyrevit
> https://github.com/eirannejad/pyRevit, https://www.notion.so/pyRevit-bd907d6292ed4ce997c46e84b6ef67a0
> Dynamo - 

Resources in Javascript: 
For .dxf - https://www.npmjs.com/package/dxf-writer