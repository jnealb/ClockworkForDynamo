import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
import Autodesk

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
collector = FilteredElementCollector(doc)
views = collector.OfClass(View).ToElements()
viewlist = list()
for view in views:
	if view.ViewType == ViewType.ThreeD:
		if not(view.IsTemplate):
			viewlist.append(view)
	else:
		viewlist.append(view)
OUT = viewlist