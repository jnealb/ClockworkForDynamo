import clr
from System import Environment, Version
OSnames = ["Windows XP","Windows Vista","Windows 7","Windows 8.1","Windows 10"]
OSversions = [Version(5,1,2600),Version(6,0,6000),Version(6,1,7600),Version(6,3,9600),Version(10,0,10240)]
for OSname, OSversion in zip(OSnames, OSversions):
	if Environment.OSVersion.Version.CompareTo(OSversion) >= 0:
		thisOS = OSname
OUT = (thisOS,Environment.OSVersion.Version.ToString(),Environment.OSVersion.ServicePack)