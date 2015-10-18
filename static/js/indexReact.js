// Used in the post app
function AddPostEvent(){
	var event = document.createEvent('Event');
	event.initEvent('addPostNav', true, true);
	document.dispatchEvent(event);
}

var AddPost = React.createClass({
	getInitialState: function(){
		return { showModal: 'none' }
	},
	componentDidMount: function(){
		var self = this;
		document.addEventListener('addPostNav', function(e){
			self.showModal();
		}, false);
	},
	showModal: function(){
		this.setState({ showModal: 'inherit' });
	},
	closeModal: function(){
		this.setState({ showModal: 'none' });
	}
	// function responsible for the ajax call
	addPost: function(){
		var self = this;
		var date = new Date();
		date = date.toISOString();

		// Serializer passed to the api
		// Used jquery to grab the value
		var sendData = {author: "", tags: $('#addPostModalTags	').val(), title: $("#addNewsModalTitle").val(), article: $('#addNewsModalArticle').val(), date: date}
		$.ajax({
			url: 'http://127.0.0.1:8000/post/api/',
			dataType: 'json',
			method: 'POST',
			data: sendData,
			success: function(data){
				var id = data.id;
				window.location.href = "http://127.0.0.1:8000/post/"+id+"/";
			}.bind(this),
			// error: function
		});
	}
});
// Used in the post app




// Used in the bands app
var bands = [
	{name: "Bayside", image: "http://cdn.idigitaltimes.com/sites/idigitaltimes.com/files/2015/07/31/naruto.jpg"},
	{name: "Paramore", image: "http://i.ytimg.com/vi/wf1z3k2hgjM/hqdefault.jpg"},
	{name: "Bring Me the Horizon", image: "http://vignette4.wikia.nocookie.net/naruto/images/f/f6/Naruto_as_the_Seventh_Hokage.png/revision/latest/scale-to-width-down/300?cb=20150208132430"},
]

var BandComponent = React.createClass({

	getInitialState: function(){
		return {CustomText: "Text before the click"};
	},
	CustomClickFunction: function(){
		this.setState({CustomText: "Text After Click"});
	},
	render: function() {
		var testStyle = { fontSize: '18px', marginRight: '20px' };
		return (
			<div style = {testStyle}>
				<h1>{this.state.CustomText}</h1>
				<button onClick={this.CustomClickFunction}>Click Me!</button>
				{this.props.bands.map(function(band){
					return(
						<Band name={band.name} image={band.image} />
					)
				})}
			</div>
		);
	}

});

var Band = React.createClass({

	render: function() {
		return (
			<div>
				<h2>{this.props.name}</h2>
				<img src={this.props.image} />
			</div>
		);
	}

});

React.render(
	<BandComponent bands={bands} />,
	document.getElementById('content')
	)
// Used in the bands app