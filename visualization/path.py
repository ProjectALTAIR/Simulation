def generate_path(path,setup):
	f = open('flightpath.kml','w')
	#for testing
	#path=["-123.3319354330095,48.46286026082066,1234","-123.3314097881247,48.46291576120517,1234","-123.3314317628628,48.4636185759673,1654","-123.3207315926024,48.46360507458775,1544","-123.3184295971455,48.46297666872875,1784","-123.3118938125541,48.4632502031565,1714"]
	message = """<?xml version="1.0" encoding="UTF-8"?>
	<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
	<Document>
		<name>Untitled Path.kml</name>
		<Style id="s_ylw-pushpin_hl">
			<IconStyle>
				<scale>1.3</scale>
				<Icon>
					<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
				</Icon>
				<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
			</IconStyle>
		</Style>
		<StyleMap id="m_ylw-pushpin">
			<Pair>
				<key>normal</key>
				<styleUrl>#s_ylw-pushpin</styleUrl>
			</Pair>
			<Pair>
				<key>highlight</key>
				<styleUrl>#s_ylw-pushpin_hl</styleUrl>
			</Pair>
		</StyleMap>
		<Style id="s_ylw-pushpin">
			<IconStyle>
				<scale>1.1</scale>
				<Icon>
					<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
				</Icon>
				<hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
			</IconStyle>
		</Style>
		<Placemark>
			<name>Untitled Path</name>
			<styleUrl>#m_ylw-pushpin</styleUrl>
			<LineString>
				<tessellate>1</tessellate>
				<altitudeMode>relativeToGround</altitudeMode>
				<coordinates>""" + " ".join(path) + """
				</coordinates>
			</LineString>
		</Placemark>
	</Document>
	</kml>"""


	f.write(message)
	f.close()