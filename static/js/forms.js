const pageData = JSON.parse(document.getElementById('pageData').textContent);

var app=new Vue({
	el: '#app',
	delimiters: ['[[',']]'],
	data(){
		return{
			legend: 'My ajax contact form',
			sender: this.resetSender()
		};
	},
	methods:{
		resetSender(){
			return{
				fullname: '',
				email: '',
				subject: '',
				message: ''
			};
		},
		submit(){
			var self=this,
				x=document.getElementsByName('csrfmiddlewaretoken');
			$.ajax({
				url: '/forms/ajax/',
				method: 'post',
				data: {
					csrfmiddlewaretoken: x[0].value,
					fullname: self.sender.fullname,
					email: self.sender.email,
					subject: self.sender.subject,
					message: self.sender.message
				}
			}).done(function(response){
				self.sender=self.resetSender();
				table.senders=response.senders;
				alert(response.msg);
			});
		}
	}
});


var table=new Vue({
	el: '#table',
	delimiters: ['[[',']]'],
	data(){
		return{
			senders: pageData.senders
		}
	}
});
