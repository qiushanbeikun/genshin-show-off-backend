let express = require('express');
let router = express.Router();
let childProcess = require('child_process')

/* GET home page. */
router.post('/', function (req, res, next) {
    let config = JSON.stringify(req.body);
    console.log(config);
    // let config = req.body
    // console.log(config, config['mode']);
    // let [mode, levelP, position, mainProp] = [config.mode, config,level, config.position, config.mainProp]
    let process = childProcess.spawn('python', ['./routes/blender.py', config]);
    let imageString = '';
    process.stdout.on('data', function (data) {
        // console.log(data.substring(0, 50))
        imageString += data.toString();
        // console.log(data.toString());

    });
    console.log(imageString)
    process.stdout.on('end', () => {
        res.send(imageString);
    });
    // res.send(imageString);
});

module.exports = router;
