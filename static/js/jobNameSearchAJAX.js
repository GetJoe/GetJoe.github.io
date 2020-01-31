
$(document).ready(function(){
	$('form').on('submit', function(event){
		$.ajax( {
			data : {
				jobname: $('#search-field').val(),
			},
			type: "POST",
			url: "/"
		}).done(function(data){
			console.log(data);
			const entries = Object.entries(data);
			console.log(entries[0][0]); //get the name of the state from the dictonary looping through the first [0] will iterate through each state
						
			//console.log(entries2[0][1]); // get totaljobs from the dictionary
			//console.log(entries2[1][1]); // get the Zscore from the dictionary
						
						
			var totalJobsDictionary = {}
			var zscoreDictionary = {}
						
			for(i=0; i < entries.length; i++){
				const dataEntries = Object.entries(entries[i][1]);
				console.log("State: " + entries[i][0] +
							" Jobs: " + dataEntries[0][1] +
							" ZScore: " + dataEntries[1][1]
				);
				totalJobsDictionary[entries[i][0]] = dataEntries[0][1];
				zscoreDictionary[entries[i][0]] = dataEntries[1][1];
							
			}
						
						
			//separate dictionaries for each type of data so we can toggle them depending on what we are interested in
			var totalJobsDictionaryKeys = Object.keys(totalJobsDictionary);
			var zscoreDictionaryKeys = Object.keys(zscoreDictionary);
			
		
			//recreate the map with the data included from the AJAX request
			
			var mapObject = $('#map').vectorMap('get', 'mapObject');
			mapObject.remove();
			
			$(function(){
				$('#map').vectorMap({
					map: 'us_mill',
					backgroundColor: '#ffffff',
					regionStyle: {
						initial: {
							fill: 'white',
							stroke: 'black',
							'stroke-width': 0.65
						},
						hover: {
							cursor: 'default',
							fill: '#A3A3A3',
							'fill-opacity': 0.3
						}
					},
					series: {
						regions: [{
							attribute: 'fill',
							scale: ['#FFDBDB', '#900000'],
							values: totalJobsDictionary
						}]
					},
					onRegionTipShow: function(event, label, code){
						label.html(
							'<b>'+ label.html() +'</b></br>'+'<b>Total Jobs: </b>' + totalJobsDictionary[code] + '</br>' +
							'<b>Z-Score: </b>' + zscoreDictionary[code]
						);
					}
				});
	
			});
			
			
			//mapObject.series.regions[0] = totalJobsDictionary;
			//mapObject.series.regions[1] = 'fill';
			//mapObject.series.regions[2] = ['#BFB4FF', '#7400FF'];
						
		});
		event.preventDefault();	
	});
});