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
		}
	});
	
});