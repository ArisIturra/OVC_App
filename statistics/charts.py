from django.utils.safestring import mark_safe
#from .models import *


class Bars:
	def get_bars(self,data = None):
		values = ''
		count = 0
		for d in sorted(data.iterkeys()):
			values += "data.setValue(%s,0,'%s');\n"%(count,d)
			values += "data.setValue(%s,1,%s);\n"%(count,data[d])
			count = count +1
		data_txt = """
			data.addColumn('string', 'Year');
		        data.addColumn('number', 'Actividad');
		        data.addRows(%s);
				%s
		"""%(len(data),values)
		
		return mark_safe("""
	        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        	<script type="text/javascript">
	        google.load("visualization", "1", {packages:["corechart"]});
	        google.setOnLoadCallback(drawChart);
        	function drawChart() {
                	var data = new google.visualization.DataTable();
			%s
		        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
		        chart.draw(data, {width: 640, height: 480, title: 'Actividad Mensual',
			hAxis: {title: 'Estaciones', titleTextStyle: {color: 'red'},

			}
                         });}
    		</script>
		"""%(data_txt))
		

	def get_histogram(self):
	
		data_set_choice = ''	
		for c in Choice.objects.all():
			data_set_choice += "data.addColumn('number','%s');\n"%c.name
		stations = Station.objects.all()
		data_rows = len(stations)
		
		s = stations[0]

		script =mark_safe("""

	<script type="text/javascript" src="https://www.google.com/jsapi"></script>
	<script type="text/javascript">
      	google.load("visualization", "1", {packages:["corechart"]});
      	google.setOnLoadCallback(drawChart);
      	function drawChart() {
        	var data = new google.visualization.DataTable();
        	data.addColumn('string','string');
		%s
		data.addRows(%s);
        	data.setValue(0, 0, 'AYSE');
        	data.setValue(0, 1, 100);
        	data.setValue(0, 2, 500);
        	data.setValue(0, 3, 400);
        	data.setValue(0, 4, 300);
		

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, {width: 400, height: 240, title: 'Company Performance',
                          hAxis: {title: 'Year', titleTextStyle: {color: 'red'}}
                         });
      }
    </script>

		"""%(data_set_choice,data_rows)

)

		return script
