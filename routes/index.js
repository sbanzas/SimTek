var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    sess = req.session;
    console.log(sess);
    if (!sess.usrName){
        sess.usrName = "pepe";
        res.render('index', { title: 'Aun no estas logueado' });
    }else{
        res.render('index', { title: 'ya estas logueado' });
    }
});

module.exports = router;