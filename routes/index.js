let express = require('express');
let router = express.Router();
let childProcess = require('child_process')

/* GET home page. */
router.post('/', async function (req, res, next) {
    let config = req.body;
    let process = childProcess.spawn('python', ['./routes/blender.py', 123, 234]);
    await process.stdout.on('data', function(data) {
        res.send(data.toString())
    })
});

module.exports = router;
