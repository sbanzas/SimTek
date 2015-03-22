fucntion defineUserModel(mongoose, fn){

    var Schema = mongoose.Schema;
    var ObjectId = Schema.ObjectId;
    var crypto = required('../../encryptModule.js');

    function validatePresenceOf(value) {
        return value && value.length;
    }

    User = new Schema({
        'email': { type: String, validate: [validatePresenceOf, 'an email is required'], index: { unique: true } },
        'name': String,
        'last': String,
        'hashed_password': String
    });

    User.virtual('id').get(function() {
        return this._id.toHexString();
    });

    User.virtual('password').set(function(password) {
        this._password = password;
        this.hashed_password = crypto.encryptPass(password);
    })

    .get(function() { return this._password; });

    User.method('authenticate', function(plainText) {
        return crypto.encryptPass(plainText) === this.hashed_password;
    });

    User.pre('save', function(next) {
        if (!validatePresenceOf(this.password)) {
            next(new Error('Invalid password'));
        } else {
            next();
        }
    });

    mongoose.model('User', User);

    fn();
}

module.exports = defineUserModel;