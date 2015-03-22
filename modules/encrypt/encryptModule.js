var crypto = require('crypto');
var config = require('./config.js');

/*function createKey(user){
	return user.regDate + user.name + user.loginName;
}*/

module.exports = {
	encyptPass: function(password){
		//var SecretKey = createKey(user);
		return crypto.createHmac(config.algorithm ,config.secretKey).update(password).digest('base64')
	}	
};